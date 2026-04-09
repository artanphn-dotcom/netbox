# NetBox Quick Launch

Use these commands from **PowerShell** for the fastest local startup on this machine.

## Repo location in WSL
```text
/home/artan/netbox
```

## 1) Re-sync the repo into WSL
```powershell
wsl.exe -- bash -lc "mkdir -p ~/netbox && rsync -a --delete --exclude '.venv' --exclude '.venv-wsl' /mnt/c/Users/ArtanV/Desktop/netbox/ ~/netbox/"
```

## 2) Start PostgreSQL and Redis
```powershell
wsl.exe -u root -- systemctl start postgresql.service
wsl.exe -u root -- systemctl start redis-server.service
```

## 3) Start NetBox
```powershell
wsl.exe -u root -- systemctl start netbox-dev.service
```

## 4) Open NetBox
```text
http://127.0.0.1:8000/
```

> Use `http://` exactly. `https://127.0.0.1:8000/` will fail because Django's dev server is HTTP-only.

## Optional: run it manually instead of the service
```powershell
wsl.exe -- bash -lc "cd ~/netbox/netbox && /home/artan/.venvs/netbox/bin/python manage.py runserver --insecure 0.0.0.0:8000"
```

## Optional: create an admin user
```powershell
wsl.exe -- bash -lc "cd ~/netbox/netbox && /home/artan/.venvs/netbox/bin/python manage.py createsuperuser"
```

## Stop NetBox
```powershell
wsl.exe -u root -- systemctl stop netbox-dev.service
```
