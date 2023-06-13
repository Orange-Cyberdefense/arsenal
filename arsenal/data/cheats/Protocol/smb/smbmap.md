# smbmap
% smb, samba

## smbmap
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 

```
smbmap -H <ip> -u "<user>%<password>"
```

## smbmap - null access
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 

```
smbmap -u "" -p "" -P 445 -H <ip>
```

## smbmap - guest access
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 
```
smbmap -u "guest" -p "" -P 445 -H <ip>
```

## smbmap - list root of all shares
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 
```
smbmap -H <ip> -u <user> -p <password> -d <domain> -r
```

## smbmap - recursively list dirs, and files
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT 
```
smbmap -H <ip> -u <user> -p <password> -d <domain> -R <path> --depth 1
```

= ip: 192.168.1.0/24
