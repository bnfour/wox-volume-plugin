from const import MUTE
from ctypes import POINTER, cast

load_ok = True
try:
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
except ImportError:
    load_ok = False


class VolumeManager(object):
    """Class that hides away scary guts of core audio interaction behind
    more pythonic interface"""

    def __init__(self):
        """Constructor that sets up interface for other methods to use."""
        self.init_success = load_ok
        if self.init_success:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(
                IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            self.volume_interface = cast(
                interface, POINTER(IAudioEndpointVolume))
        else:
            self.volume_interface = None

    def get_volume(self):
        """Returns current volume as 0--100 integer as displayed in tray volume
        control."""
        volume = self.volume_interface.GetMasterVolumeLevelScalar()
        return round(volume * 100)

    def get_muted(self):
        """Returns True when current playback device is muted,
        False otherwise."""
        return self.volume_interface.GetMute()

    def set_volume(self, value):
        """Sets the volume to given value."""
        if not isinstance(value, int):
            raise TypeError("Volume is expressed as 0--100 integer.")
        if not (0 <= value <= 100):
            raise ValueError("Volume value must be within 0--100 range.")
        self.volume_interface.SetMasterVolumeLevelScalar(value / 100, None)

    def set_muted(self, value):
        """Sets muted status to given value."""
        if not isinstance(value, bool):
            raise TypeError("Mute status is expressed as a bool.")
        self.volume_interface.SetMute(value, None)

    def perform_action(self, value):
        """Method to call from outside to alter volume or mute status."""
        # argument checks are done in set_* methods, just pass on
        if value == MUTE:
            self.set_muted(not self.get_muted())
        else:
            self.set_volume(value)
            # also unmutes
            self.set_muted(False)
