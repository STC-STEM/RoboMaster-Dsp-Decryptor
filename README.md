# RoboMaster Dsp Decryptor

rename your dsp file to `in.dsp`
drop it next to `decrypt.py`
run `decrypt.py`
DONE!

## Where I found the logic

ILSpy ->
C:\XXXX\DJI Education Hub\RoboMaster\RoboMaster_Data\Managed\Assembly-CSharp.dll
Module.InnerTools.View.ViewLab

for the keys and iv
install MelonLoader v0.5.7 to Robomaster
install UnityExplorer.MelonLoader.Mono to Robomaster
click C# Console on the panel
paste `Module.InnerTools.View.ViewLab.GetDspEncryptKey()` into C# Console
click Compile
record the key displayed in log window
paste `Module.InnerTools.View.ViewLab.GetDspEncryptVector()` into C# Console
click Compile
record the iv displayed in log window
