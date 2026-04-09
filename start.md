# NetBox Manual Start / Recovery

Use these commands from **PowerShell** when NetBox does not start automatically in WSL.

## Repo location in WSL
```text
/home/artan/netbox
```

## 1) Re-sync the repo from Windows into WSL
```powershell
wsl.exe -- bash -lc "mkdir -p ~/netbox && rsync -a --delete --exclude '.venv' --exclude '.venv-wsl' /mnt/c/Users/ArtanV/Desktop/netbox/ ~/netbox/"
```

## 2) Restart WSL cleanly
```powershell
wsl --shutdown
```

## 3) Start required services
```powershell
wsl.exe -u root -- bash -lc "systemctl start postgresql.service redis-server.service"
```

## 4) Start NetBox manually from the WSL-native copy
```powershell
wsl.exe -- bash -lc "cd ~/netbox/netbox && /home/artan/.venvs/netbox/bin/python manage.py runserver --insecure 0.0.0.0:8000"
```

## 5) Start the auto-start service manually
```powershell
wsl.exe -u root -- bash -lc "systemctl restart netbox-dev.service && systemctl status netbox-dev.service --no-pager -l"
```

## 6) Check that it is up
```powershell
curl.exe -I http://127.0.0.1:8000/
curl.exe -I "http://127.0.0.1:8000/static/netbox.css?v=4.5.7"
```

## 7) View logs
```powershell
wsl.exe -- bash -lc "tail -n 100 ~/.netbox-dev.log"
wsl.exe -u root -- bash -lc "journalctl -u netbox-dev.service -n 100 --no-pager"
```

## Open NetBox
```text
http://127.0.0.1:8000/
```

> Use `http://` exactly. The Django development server here is **not HTTPS**.
