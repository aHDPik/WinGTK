# How to create package
```powershell
Copy-Item -Path "C:\gtk-build\gtk\x64\release\bin" -Destination "C:\Sources\WinGTK\WinGTK\WinGTK\bin" -Recurse
Copy-Item -Path "C:\gtk-build\gtk\x64\release\share\icons" -Destination "C:\Sources\WinGTK\WinGTK\WinGTK\share\icons" -Recurse # or unzip icons.7z
Copy-Item -Path "C:\gtk-build\gtk\x64\release\lib\girepository-1.0" -Destination "C:\Sources\WinGTK\WinGTK\WinGTK\lib\girepository-1.0" -Recurse 
python setup.py bdist_wheel 
```
# How to use
```python
import sys
if sys.platform.startswith('win32'):
   import WinGTK
import gi
gi.require_version('Gtk', '3.0')
```