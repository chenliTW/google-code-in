I use systemd to start my flask app as service;)

the flask app consist these code:
```python
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
    return "ok"


if __name__=="__main__":
    app.run(host="0.0.0.0")

```

I put the code in ```/home/chen/web/```

first navigate to``` /lib/systemd/system/```
```bash
cd /lib/systemd/system/
```

then create  flask.service file with this content
```bash
[Unit]
Description=Flask web service

[Service]
User=chen
WorkingDirectory=/home/chen/web/
Type=simple
ExecStart=/usr/bin/python3 app.py
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

then reload daemon
```bash
sudo systemctl daemon-reload
```
enable the service start at boot
```bash
sudo systemctl enable flask.service
```

the reboot you will see you service autostarted on boot ;)
