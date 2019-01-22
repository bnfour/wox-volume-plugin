import const as c


class ResultGenerator(object):
    """Class to generate JSON-like dicts to be used as results for query."""

    def generate_result(self, title, subtitle, icon_path, method, params):
        """Helper method to fill in the template of a dict with values.
        Parameters pretty much match customisable values of a result."""
        # haha this is ugly
        if not isinstance(title, str) or not isinstance(subtitle, str) \
           or not isinstance(icon_path, str) or not isinstance(method, str) \
           or not isinstance(params, list):
            raise TypeError("Invalid argument type.")
        return {
            "Title": title, "Subtitle": subtitle, "IcoPath": icon_path,
            "JsonRPCAction": {
                    "method": method, "parameters": params,
                    "dontHideAfterAction": False
                }
            }

    def generate_valid_result(self, value):
        """Generates a valid result for mute toggling or setting of voulme.
        Value is returned by InputParser: MUTE constant or 0-100 int."""
        if value == c.MUTE:
            title = c.MUTE_TITLE
            subtitle = c.MUTE_SUBTITLE
        elif 0 <= value <= 100:
            title = c.SET_VOLUME_TITLE.format(value)
            subtitle = c.SET_VOLUME_SUBTITLE
        else:
            raise ValueError("Invalid value to generate result for.")
        return self.generate_result(title, subtitle, c.ICON, "perform_action",
                                    [value, ])

    def generate_error(self):
        """Generates error result with link to page where it is explained."""
        return self.generate_result(
            c.ERROR_TITLE, c.ERROR_SUBTITLE, c.ICON_ERROR, "open_url",
            [c.ERROR_URL, ])
