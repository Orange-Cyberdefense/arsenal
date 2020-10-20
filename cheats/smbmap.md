# smbmap

% samba, smb, enumeration, share


## smbmap
```
smbmap -H <ip> -u "<user>%<pass>"
```

## smbmap - null access
```
smbmap -u "" -p "" -P 445 -H <ip>
```

## smbmap - guest access
```
smbmap -u "guest" -p "" -P 445 -H <ip>
```

## smbmap - list root of all shares
```
smbmap -H <ip> -u <user> -p <password> -d <domain> -r
```

## smbmap - recursively list dirs, and files
```
smbmap -H <ip> -u <user> -p <password> -d <domain> -R <path> --depth 1
```

= ip: 192.168.1.0/24
