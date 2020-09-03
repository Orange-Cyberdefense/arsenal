# Arsenal

Arsenal is just a quick inventory, reminder and launcher for pentest commands.
<br>This project written by pentesters for pentesters simplify the use of all the hard-to-remember commands

![](arsenal.gif)

In arsenal you can search for a command, select one and it's prefilled directly in your terminal. This functionality is independent of the shell used. Indeed arsenal emulates real user input (with TTY arguments and IOCTL) so arsenal works with all shells and your commands will be in the history.

You have to enter arguments if needed, but arsenal supports global variables. <br>
For example, during a pentest we can set the variable `ip` to prefill all commands using an ip with the right one.

To do that you just have to enter the following command in arsenal:
```
>set ip=10.10.10.10
``` 

Authors: 
* Guillaume Muh
* mayfly

This project is inspired by navi (<https://github.com/denisidoro/navi>) because the original version was in bash and too hard to understand to add features


## Install

```
git clone https://github.com/Orange-Cyberdefense/arsenal.git
cd arsenal
python3 setup.py develop --user
```

Inside your .bashrc or .zshrc add the path to `arsenal/arsenal/app.py`
```
alias a='python3 $HOME/git/arsenal/arsenal/app.py'
```

## Troubleshooting
If you got on error on color init try : 
```
export TERM='xterm-256color'
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
