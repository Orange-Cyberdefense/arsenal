# Arsenal

- arsenal is just a quick inventory and launcher for hacking programs
- This project is inspired by navi (https://github.com/denisidoro/navi) because the original version was in bash and too hard to understand to add features
- We write this project for pentester to simplify all the commands to remember x)

## run in developement
```
python3 setup.py develop --user
```

## troubleshooting
- if you got on error on color init try : 
```
export TERM='xterm-256color'
```
## add alias
- inside your .bashrc or .zshrc add the path to app.py
```
alias a='python3 $HOME/git/arsenal/arsenal/app.py'
```

## TODO cheatsheets 

### reverse shell
- [x] msfvenom
- [x] php
- [x] python
- [x] perl
- ...

### Tools

#### smb
- [x] enum4linux 
- [x] smbmap
- [ ] smbget     
- [x] rpcclient
- [ ] rpcinfo
- [x] nbtscan
- [x] impacket

#### kerberos & AD
- [x] impacket

### bruteforce & pass cracking
- [x] hydra
- [x] hashcat
- [ ] john

#### scan
- [x] nmap

#### fuzz    
- [x] gobuster
- [x] ffuf
- [x] wfuzz

#### DNS
- [x] dig

#### host
- [ ] sublist3r
- [ ] subbrute

#### rpc
- [ ] rpcbind

#### netbios-ssn
- [ ] snmpwalk
- [ ] snmp-check
- [ ] onesixtyone

#### sql
- [x] sqlmap 

#### oracle
- [ ] oscanner
- [ ] sqlplus
- [ ] tnscmd10g

#### mysql
- [x] mysql

#### nfs
- [ ] showmount

#### rdp
- [x] xfreerdp
- [x] rdesktop
- [ ] ncrack

#### mssql
- [ ] tsql
- [ ] sqsh

#### winrm
- [x] evilwinrm

#### redis
- [ ] redis-cli

#### postgres
- [ ] psql
- [ ] pgdump

#### vnc
- [ ] vncviewer

#### x11
- [ ] xspy
- [ ] xwd
- [ ] xwininfo


#### ldap
- [x] ldapsearch

#### https
- [ ] sslscan

#### web 
- [ ] burp
- [ ] nikto
- [ ] tplmap

#### app web
- [ ] drupwn
- [x] wpscan
