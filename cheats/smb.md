# smb

% windows, samba, smb, 139, 445

## nbtscan - scan network looking for hosts
```
nbtscan -r <ip_range>
```

## smbmap
```
smbmap -H <ip> -u "<user>%<pass>"
```

## smbclient with username and password
```
smbclient \\\\<ip>\\<share> -U "<user>%<pass>"
```

## smbclient sessions without password
```
smbclient \\\\<ip>\\<share> -U "<user>%"
```

## smbclient null session
```
smbclient \\\\<ip>\\<share> -U "%"
```