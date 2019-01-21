# Volume control plugin for Wox
A plugin for [Wox launcher](http://wox.one/) to control system volume of
currently active playback device from Wox rather than from system tray.  
## Usage:
(these examples assume plugin's keyword is the default `v`)
- `v m` — toggles mute status
- `v [value 0..100]` — sets device volume to given value. This also unmutes
device if it was muted, just like the default Windows tray slider.