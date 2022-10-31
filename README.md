# UNSUPPORTED Volume control plugin for Wox

No longer maintained, USE AT YOUR OWN RISK.  

A plugin for [Wox launcher](http://wox.one/) to control system volume of
currently active playback device from Wox rather than from system tray.  
Kinda slow (about 150 ms per query), but hey, it's python.
(only because I couldn't get C# API to work pepeHands)  
## Installation:
`wpm install Volume plugin` (the one with "Volume plugin" title, messed that up)
via [WPM](http://www.wox.one/plugin/254)    
or grab a zip from releases and extract to
`%appdata%\Local\Wox\app-[version]\Plugins\[whatever]\`
(this won't survive Wox updating, use WPM if you can)  
**Important:** this plugin needs [pycaw](https://github.com/AndreMiras/pycaw)
in your Python runtime.
You will be greeted with an error if it isn't present.
## Usage:
(these examples assume plugin's keyword is the default `v`)
- `v m` — toggles mute status
- `v [value 0..100]` — sets device volume to given value. This also unmutes
device if it was muted, just like the default Windows tray slider.
