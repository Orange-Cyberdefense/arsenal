# impacket

% impacket, windows, exec, inital_access

Mssqlclient.py is an MSSQL client, supporting both SQL and Windows Authentications (including hashes) allowing the enumeration for Microsoft SQL servers including spawning an 'xp_cmdshell'. It also supports TLS.


## Attempts to connect to the SQL Server instance with valid credentials
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT

```
mssqlclient.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP>
```

## Attempts to use windows authentication. DEFAULT: FALSE
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT

```
mssqlclient.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP> -windows-auth
```

## Allow for the SQL Server instance without password
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT

```
mssqlclient.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP> -no-pass
```

## Attempts to use pass-the-hash method for authentication
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT

```
mssqlclient.py <DOMAIN>/<USERNAME>@<IP> -hashes <LMHASH:NTHASH>
```

## Attempts to use kerberos authentication
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT

```
mssqlclient.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP> -k
```

## Attempts to use the IP address of the domain controller to be used for authentication
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT

```
mssqlclient.py <DOMAIN>/<USERNAME>:<PASSWORD>@<IP> -dc-ip <IP>
```