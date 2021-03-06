"""
Conversion functions between various types.
"""

import Qt.QtCore as QtCore

import mmSolver.logger


LOG = mmSolver.logger.get_logger()


# Words recognised as True or False.
TRUE_WORDS = ['1', 'y', 't', 'yes', 'on', 'ya', 'yeah', 'true']
FALSE_WORDS = ['0', 'n', 'f', 'no', 'off', 'nah', 'nope', 'false']


def stringToBoolean(value):
    """
    Convert a string into a boolean value, using list of 'TRUE_WORDS'
    """
    v = None
    if isinstance(value, bool):
        v = value
    elif isinstance(value, basestring):
        value = value.strip().lower()
        if value in TRUE_WORDS:
            v = True
        elif value in FALSE_WORDS:
            v = False
        else:
            return False
    else:
        raise TypeError
    return v


def booleanToString(value):
    """
    Convert boolean value to a string.
    """
    return str(value)


def stringToIntList(value):
    """
    Convert a string of integer ranges to a list of integers.

    value = '1001-1101'
    value = '1001,1002,1003-1005,1010-1012
    """
    if isinstance(value, basestring) is False:
        raise TypeError
    value = value.strip()
    int_list = []
    for v in value.split(','):
        v = v.strip()
        if v.isdigit() is True:
            i = int(v)
            int_list.append(i)
        if '-' not in v:
            continue

        dash_split = v.split('-')
        dash_split = filter(lambda x: x.isdigit(), dash_split)
        if len(dash_split) > 1:
            # Even if the user adds more than 1 dash character, we only take
            # the first two.
            s = int(dash_split[0])
            e = int(dash_split[1])
            if s == e:
                int_list.append(s)
                continue
            if s < e:
                int_list += list(range(s, e + 1))
    int_list = list(set(int_list))
    int_list = list(sorted(int_list))
    return int_list


def intListToString(value):
    """
    Convert a list of integers to a string.
    """
    if isinstance(value, list) is False:
        raise TypeError
    int_list = list(set(value))
    int_list = list(sorted(int_list))
    grps = []
    start = -1
    end = -1
    prev = -1
    for i, num in enumerate(int_list):
        first = i == 0
        last = (i + 1) == len(int_list)
        if first is True:
            # Start a new group.
            start = num
            end = num
        if (prev + 1) != num:
            # End old group.
            end = prev
            if end != -1:
                grps.append((start, end))
            # New group
            start = num
            end = num
        if last is True:
            # Close off final group.
            end = num
            if end != -1:
                grps.append((start, end))
        prev = num

    string_list = []
    for grp in grps:
        s, e = grp
        if s == e:
            string_list.append(str(s))
        else:
            string_list.append('{0}-{1}'.format(s, e))
    return ','.join(string_list)


def stringToStrategy(value):
    return value


def stringToAttrFilter(value):
    return value


def stringToInteger(value):
    return int(value)


def booleanToCheckState(value):
    if isinstance(value, bool) is False:
        msg = 'value is not bool type: %r'
        raise TypeError(msg % type(value))
    v = QtCore.Qt.CheckState.Unchecked
    if value is True:
        v = QtCore.Qt.CheckState.Checked
    return v


def checkStateToBoolean(value):
    v = False
    if value == QtCore.Qt.CheckState.Checked:
        v = True
    return v
