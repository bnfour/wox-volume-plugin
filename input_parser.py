from const import MUTE


class InputParser(object):
    """Class that processes user input into actual volume to set."""

    def parse(self, parameters_string):
        """
        Converts user input (parameters to plugin keyword) to actual value.

        Returns None on invalid inputs, MUTE constant if mute should be
        toggled, integer in 0-100 range as volume to set.
        Valid inputs are letter 'm' for mute toggle, or 0-100 int to set.
        """
        if not isinstance(parameters_string, str):
            raise TypeError("Parameters string is not a string.")
        parameters = parameters_string.split(" ")
        if len(parameters) != 1:
            return None
        p = parameters[0]
        # m is for mute
        if p.lower() == 'm':
            return MUTE
        # try to parse an integer
        else:
            try:
                value = int(p)
            except ValueError:
                return None
            if 0 <= value <= 100:
                return value
            else:
                return None
