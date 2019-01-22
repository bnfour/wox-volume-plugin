from wox import Wox
import webbrowser

from input_parser import InputParser
from result_generator import ResultGenerator
from volume_manager import VolumeManager


class Main(Wox):
    """Class that works with the Wox API."""

    parser = InputParser()
    generator = ResultGenerator()
    manager = VolumeManager()

    def query(self, parameters):
        """
        Returns list of results based on provided parameters.

        Parameters are provided as string stripped from plugin keyword, if any.
        For instance, input of "v 50 whatever" (assuming plugin keyword is v)
        will set parameters to "50 whatever".
        """
        value = self.parser.parse(parameters)
        if value is None:
            return []
        result = self.generator.generate_valid_result(value)
        return [result, ]

    def perform_action(self, value):
        """Method that reroutes user-defined value to VolumeManager."""
        self.manager.perform_action(value)

    def open_url(self, url):
        """Opens provided URL as a new tab in default browser."""
        # new=2 is a way of saying "new tab please, um, if that's possible"
        webbrowser.open(url, new=2)


# as required by Wox's docs
if __name__ == "__main__":
    Main()
