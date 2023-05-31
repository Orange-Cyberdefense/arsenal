# systemctl

% systemctl, service
#platform/linux #target/local #cat/UTILS 

## Start service
```
systemctl start <service_inactive>
```

## Stop service
```
systemctl stop <service_active>
```

## Enable service
```
systemctl enable <service_disabled>
```

## Disable service
```
systemctl disable <service_enabled>
```

## Restart service
```
systemctl restart <service>
```

## Reload service
```
systemctl reload <service_active>
```

## Service status
```
systemctl status <service>
```

## List running services
```
systemctl list-units --type=service --state=running
```

## List enabled services
```
systemctl list-unit-files --type=service --state=enabled
```

## List disabled services
```
systemctl list-unit-files --type=service --state=disabled
```

$ service_inactive: systemctl list-units --type=service --state=inactive | awk '{print $1}' | grep .service | sed 's/.service$//'
$ service_active: systemctl list-units --type=service --state=active | awk '{print $1}' | grep .service | sed 's/.service$//'
$ service_enabled: systemctl list-unit-files --type=service --state=enabled | awk '{print $1}' | grep .service | sed 's/.service$//'
$ service_disabled: systemctl list-unit-files --type=service --state=disabled | awk '{print $1}' | grep .service | sed 's/.service$//'
$ service: systemctl list-units --type=service --all | awk '{print $1}' | grep .service | sed 's/.service$//'
