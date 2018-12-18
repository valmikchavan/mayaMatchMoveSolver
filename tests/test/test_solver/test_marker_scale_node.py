"""
Test the mmMarkerScale node for correctness.
"""

import unittest

try:
    import maya.standalone
    maya.standalone.initialize()
except RuntimeError:
    pass
import maya.cmds


import test.test_solver.solverutils as solverUtils
import mmSolver._api.utils as api_utils


# @unittest.skip
class TestMarkerScaleNode(solverUtils.SolverTestCase):

    @staticmethod
    def create_camera(name):
        cam_tfm = maya.cmds.createNode('transform', name=name)
        cam_tfm = api_utils.get_long_name(cam_tfm)
        cam_shp = maya.cmds.createNode('camera', name=name+'Shape',
                                       parent=cam_tfm)
        cam_shp = api_utils.get_long_name(cam_shp)
        return cam_tfm, cam_shp

    def test_marker_scale_node(self):
        node = maya.cmds.createNode('mmMarkerScale')
 
        maya.cmds.setAttr(node + '.focalLength', 35)
        maya.cmds.setAttr(node + '.horizontalFilmAperture', 36.0 / 25.4)
        maya.cmds.setAttr(node + '.verticalFilmAperture', 24.0 / 25.4)
        maya.cmds.setAttr(node + '.horizontalFilmOffset', 0.0)
        maya.cmds.setAttr(node + '.verticalFilmOffset', 0.0)
        maya.cmds.setAttr(node + '.depth', 1.0)

        scale = maya.cmds.getAttr(node + '.outScale')
        assert self.approx_equal(scale[0][0], 1.0285714285714285)
        assert self.approx_equal(scale[0][1], 0.6857129142857141)
        assert self.approx_equal(scale[0][2], 1.0)

        translate = maya.cmds.getAttr(node + '.outTranslate')
        print translate
        assert self.approx_equal(translate[0][0], 0.0)
        assert self.approx_equal(translate[0][1], 0.0)
        assert self.approx_equal(translate[0][2], 0.0)

        return


if __name__ == '__main__':
    prog = unittest.main()