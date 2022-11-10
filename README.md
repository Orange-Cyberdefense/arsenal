# Arsenal

![](img/logo.png)

Arsenal is just a quick inventory, reminder and launcher for pentest commands.
<br>This project written by pentesters for pentesters simplify the use of all the hard-to-remember commands

![](img/arsenal.gif)

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


## Arsenal new features

![](img/arsenal_update.png)

- New colors
- Add tmux new pane support (with -t)
- Add default values in cheatsheets commands with `<argument|default_value>`
- Support description inside cheatsheets
- New categories and Tags
- New cheatsheets
- Add yml support (thx @0xswitch )
- Add fzf support with ctrl+t (thx @mgp25)

## Install & Launch
- with pip :
```
python3 -m pip install arsenal-cli
```

- run (we also advice you to add this alias : `alias a='arsenal'`)
```
arsenal
```

- manually:
```
git clone https://github.com/Orange-Cyberdefense/arsenal.git
cd arsenal
python3 -m pip install -r requirements.txt
./run
```

Inside your .bashrc or .zshrc add the path to `run` to help you do that you could launch the addalias.sh script
```
./addalias.sh
```

- Also if you are an Arch user you can install from the AUR:
```bash
git clone https://aur.archlinux.org/arsenal.git
cd arsenal 
makepkg -si
```
- Or with an AUR helper like yay:
```bash
yay -S arsenal
```

## Launch in tmux mode

```
./run -t # if you launch arsenal in a tmux window with one pane, it will split the window and send the command to the otherpane without quitting arsenal
         # if the window is already splited the command will be send to the other pane without quitting arsenal
./run -t -e # just like the -t mode but with direct execution in the other pane without quitting arsenal
```

## Add external cheatsheets

You could add your own cheatsheets insode the my_cheats folder or in the ~/.cheats folder.

You could also add additional paths to the file `<arsenal_home>/arsenal/modules/config.py`,
arsenal reads `.md` (MarkDown) and `.rst` (RestructuredText).

```
CHEATS_PATHS = [
    join(BASEPATH, "cheats"), # DEFAULT
    join(HOMEPATH, "docs/my_cheats")
]
```

Cheatsheets examples are in `<arsenal_home>/cheats`: `README.md` and `README.rst`

## Troubleshooting

If you got on error on color init try : 
```
export TERM='xterm-256color'
```

--

If you have the following exception when running Arsenal:
```
ImportError: cannot import name 'FullLoader'
```
First, check that requirements are installed:
```
pip install -r requirements.txt
```
If the exception is still there:
```
pip install -U PyYAML
```

## Mindmap
- Active directory mindmap
  - Due to csp on github when you open the svg, we moved the AD mindmap and the source to this repository : [https://github.com/Orange-Cyberdefense/ocd-mindmaps](https://github.com/Orange-Cyberdefense/ocd-mindmaps)

[https://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2022_11.svg](https://orange-cyberdefense.github.io/ocd-mindmaps/img/pentest_ad_dark_2022_11.svg)

- AD mindmap black version
![](./mindmap/pentest_ad_black.png)

- Exchange Mindmap (thx to @snovvcrash)
![](./mindmap/Pentesting_MS_Exchange_Server_on_the_Perimeter.png)

- Active directory ACE mindmap
![](./mindmap/ACEs_xmind.png)

## TODO cheatsheets 

### reverse shell
- [X] msfvenom
- [X] php
- [X] python
- [X] perl
- [X] powershell
- [X] java
- [X] ruby

### whitebox analysis grep regex
- [X] php
- [X] nodejs
- [X] hash

### Tools

#### smb
- [X] enum4linux 
- [X] smbmap
- [ ] smbget     
- [X] rpcclient
- [ ] rpcinfo
- [X] nbtscan
- [X] impacket

#### kerberos & AD
- [X] impacket
- [X] bloodhound
- [X] rubeus
- [ ] powerview
- [ ] shadow credentials attack
- [ ] samaccountname attack

#### MITM
- [X] mitm6
- [X] responder

#### Unserialize
- [X] ysoserial
- [ ] ysoserial.net

### bruteforce & pass cracking
- [X] hydra
- [X] hashcat
- [X] john

#### scan
- [X] nmap
- [X] eyewitness
- [X] gowitness

#### fuzz    
- [X] gobuster
- [X] ffuf
- [X] wfuzz

#### DNS
- [X] dig
- [X] dnsrecon
- [X] dnsenum
- [X] sublist3r

#### rpc
- [ ] rpcbind

#### netbios-ssn
- [X] snmpwalk
- [X] snmp-check
- [X] onesixtyone

#### sql
- [X] sqlmap 

#### oracle
- [ ] oscanner
- [ ] sqlplus
- [ ] tnscmd10g

#### mysql
- [X] mysql

#### nfs
- [X] showmount

#### rdp
- [X] xfreerdp
- [X] rdesktop
- [ ] ncrack

#### mssql
- [X] sqsh

#### winrm
- [X] evilwinrm

#### redis
- [ ] redis-cli

#### postgres
- [X] psql
- [ ] pgdump

#### vnc
- [X] vncviewer

#### x11
- [X] xspy
- [X] xwd
- [X] xwininfo

#### ldap
- [X] ldapsearch

#### https
- [ ] sslscan

#### web 
- [ ] burp
- [X] nikto
- [ ] tplmap

#### app web
- [X] drupwn
- [X] wpscan
- [ ] nuclei
