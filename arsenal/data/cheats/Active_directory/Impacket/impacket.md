# Impacket

% impacket, windows, smb, 445

## lookupsid - SID User Enumeration,  extract the information about what users exist and their data. 
#platform/linux #target/remote #cat/RECON 

```
lookupsid.py <domain>/<user>:<password>@<ip>
```

## reg - query registry info remotely
#platform/linux #target/remote #cat/RECON 
```
reg.py <domain>/<user>:<password>@<ip> query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s
```

## rpcdump - list rpc endpoint
#platform/linux #target/remote #cat/RECON 
```
rpcdump.py <domain>/<user>:<password>@<ip>
```

## services.py - (start, stop, delete, read status, config, list, create and change any service) remote
#platform/linux #target/remote #cat/RECON  #cat/ATTACK/EXPLOIT  
```
services.py <domain>/<user>:<password>@<ip> <action>
``` 

## getarch - find target architecture (64 or 32 bits)
#platform/linux #target/remote #cat/RECON 
```
getArch.py -target <ip>
```

## netview - enumeration tool (ip/shares/sessions/logged users) - need dns set
#platform/linux #target/remote #cat/RECON 
```
netview.py <domain>/<user> -target <ip> -users <users_file>
```


