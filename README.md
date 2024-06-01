# RoboMaster Dsp Decryptor

rename your dsp file to `in.dsp`</br>
drop it next to `decrypt.py`</br>
run `decrypt.py`</br>
DONE!

## Where I found the logic

ILSpy -></br>
C:\XXXX\DJI Education Hub\RoboMaster\RoboMaster_Data\Managed\Assembly-CSharp.dll</br>
Module.InnerTools.View.ViewLab

for the keys and iv</br>
install MelonLoader v0.5.7 to Robomaster</br>
install UnityExplorer.MelonLoader.Mono to Robomaster</br>
click C# Console on the panel</br>
paste `Module.InnerTools.View.ViewLab.GetDspEncryptKey()` into C# Console</br>
click Compile</br>
record the key displayed in log window</br>
paste `Module.InnerTools.View.ViewLab.GetDspEncryptVector()` into C# Console</br>
click Compile</br>
record the iv displayed in log window
