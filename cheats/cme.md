# crackmapexec

% windows, smb, enumeration, cme, 445

## crackmapexec - enumerate hosts, network

Exemple : cme smb 192.168.1.0/24

```
cme smb <ip>
```

## crackmapexec - enumerate null session
```
crackmapexec smb <ip> -u '' -p '' --pass-pol
```

## crackmapexec - enumerate anonymous login
```
crackmapexec smb <ip> -u 'a' -p ''
```

## crackmapexec - enumerate active sessions
```
crackmapexec smb <ip> -u <user> -p '<password>' --sessions
```

## crackmapexec - enumerate logged users
```
crackmapexec smb <ip> -u <user> -p '<password>' --loggedon-users
```

## crackmapexec - enumerate domain users
```
crackmapexec smb <ip> -u <user> -p '<password>' --users
```

## crackmapexec - enumerate users by bruteforce the RID
```
crackmapexec smb <ip> -u <user> -p '<password>' --rid-brute
```

## crackmapexec - enumerate domain groups
```
crackmapexec smb <ip> -u <user> -p '<password>' --groups
```

## crackmapexec - enumerate local groups
```
crackmapexec smb <ip> -u <user> -p '<password>' --local-groups
```

## crackmapexec - enumerate host with smb signing not required
```
crackmapexec smb <ip> --gen-relay-list <relaylistOutputFilename>
```

## crackmapexec - local-auth
```
crackmapexec smb <ip> -u <user> -p <password> --local-auth
```

## crackmapexec - local-auth with hash
```
crackmapexec smb <ip> -u <user> -H <hash> --local-auth
```

## crackmapexec - domain
```
crackmapexec smb <ip> -u <user> -p <password> -d <domain>
```

## crackmapexec - SAM
```
crackmapexec smb <ip> -u <user> -p <password> -d <domain> --sam
```

## crackmapexec - LSA
```
crackmapexec smb <ip> -u <user> -p <password> -d <domaine> --lsa
```

## crackmapexec - shares
```
crackmapexec smb <ip> -u <user> -p <password> -d <domain> --shares
```

## crackmapexec - enumerate disks
```
crackmapexec smb <ip> -u <user> -p '<password>' --disks
```

## crackmapexec - ntds.dit
```
crackmapexec smb <ip> -u <user> -p <password> -d <domain> --ntds
```

## crackmapexec - ntds.dit history
```
crackmapexec smb <ip> -u <user> -p <password> -d <domain> --ntds-history
```

= ip: 192.168.1.0/24
