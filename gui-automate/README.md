to make the script auto start.
create a new file named ```guiautomate.desktop```

with content:  
```
[Desktop Entry]
Type=Application
Exec=python3 [path to the python script]
Hidden=false
X-GNOME-Autostart-enabled=true
Name=guiautomate
```
the copy it into ``` ~/.config/autostart ```
```bash
cp guiautomate.desktop /home/chen/.config/autostart
```

And that all :)
