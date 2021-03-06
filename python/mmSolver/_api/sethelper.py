"""
Set Helper, creates, removes and manipulates Maya set nodes.

Any queries use the Maya Python API, but modifications are handled with
maya.cmds.* so that they support undo/redo correctly.
"""

import maya.cmds
import maya.OpenMaya as OpenMaya

import mmSolver.logger
import mmSolver._api.utils as api_utils


LOG = mmSolver.logger.get_logger()


class SetHelper(object):
    def __init__(self, name=None):
        if name is not None:
            if isinstance(name, (str, unicode)):
                obj = api_utils.get_as_object(name)
                self._mfn = OpenMaya.MFnSet(obj)
            else:
                msg = 'name argument must be a string.'
                raise TypeError(msg)
        else:
            self._mfn = OpenMaya.MFnSet()
        return

    def get_node(self):
        node = None
        try:
            obj = self._mfn.object()
        except RuntimeError:
            obj = None
        if obj is not None and obj.isNull() is False:
            try:
                node = self._mfn.name()
            except RuntimeError:
                pass
        if isinstance(node, (str, unicode)) and len(node) == 0:
            node = None
        return node

    def get_node_uid(self):
        node = self.get_node()
        if node is None:
            return None
        uids = maya.cmds.ls(node, uuid=True) or []
        return uids[0]

    def set_node(self, name):
        obj = api_utils.get_as_object(name)
        try:
            self._mfn = OpenMaya.MFnSet(obj)
        except RuntimeError:
            raise
        return

    def create_node(self, name):
        node = maya.cmds.sets(name=name, empty=True)
        self.set_node(node)
        return self

    def delete_node(self):
        node = self._mfn.name()
        maya.cmds.delete(node)
        return self

    def get_annotation(self):
        try:
            ret = self._mfn.annotation()
        except RuntimeError:
            ret = None
        return ret

    def set_annotation(self, value):
        assert isinstance(value, str)
        set_node = self.get_node()
        maya.cmds.sets(set_node, edit=True, text=value)
        return

    def add_members(self, name_list):
        assert isinstance(name_list, list)
        set_node = self.get_node()
        maya.cmds.sets(*name_list, edit=True, include=set_node, noWarnings=True)
        return

    def remove_members(self, name_list):
        assert isinstance(name_list, list)
        set_node = self.get_node()
        maya.cmds.sets(name_list, edit=True, remove=set_node)
        return

    def add_member(self, name):
        assert isinstance(name, (str, unicode))
        set_node = self.get_node()
        maya.cmds.sets(name, edit=True, include=set_node, noWarnings=True)
        return

    def remove_member(self, name):
        set_node = self.get_node()
        maya.cmds.sets(name, edit=True, remove=set_node)
        return

    def get_all_members(self, flatten=False, full_path=True):
        assert isinstance(flatten, bool)
        assert isinstance(full_path, bool)

        sel_list = OpenMaya.MSelectionList()
        try:
            self._mfn.getMembers(sel_list, flatten)
        except RuntimeError:
            return []

        ret = []
        sel_list.getSelectionStrings(ret)
        if full_path is True:
            ret = maya.cmds.ls(ret, long=True) or []

        return ret

    def clear_all_members(self):
        set_node = self.get_node()
        maya.cmds.sets(edit=True, clear=set_node)
        return

    def member_in_set(self, name):
        # NOTE: For attributes, you must use a MPlug, as testing with
        # an MObject only tests the dependency node
        if '.' in name:
            plug = api_utils.get_as_plug(name)
            ret = self._mfn.isMember(plug)
        else:
            obj = api_utils.get_as_object(name)
            ret = self._mfn.isMember(obj)
        return ret

    def length(self):
        return len(self.get_all_members())

    def is_empty(self):
        return len(self.get_all_members()) == 0
