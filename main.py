from wox import Wox


class Main(Wox):
    """Class that works with the Wox API."""

    def query(self, parameters):
        """
        Returns list of results based on provided parameters.

        Parameters are provided as string stripped from plugin keyword, if any.
        For instance, input of "v 50 whatever" (assuming plugin keyword is v)
        will set parameters to "50 whatever".
        """
        # TODO actual results
        return []


# as required by Wox's docs
if __name__ == "__main__":
    Main()
