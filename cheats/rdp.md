# windows rdp

% rdp, windows, 3389

## enable RDP
```
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

## Add firewall authorisation RDP
```
netsh.exe advfirewall firewall add rule name="Remote Desktop - User Mode (TCP-In)" dir=in action=allow program="%%SystemRoot%%\system32\svchost.exe" service="TermService" description="Inbound rule for the Remote Desktop service to allow RDP traffic. [TCP 3389] added by LogicDaemon's script" enable=yes profile=private,domain localport=3389 protocol=tcp
```

# rdesktop
% rdp, windows

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

## xfreerdp - classic
```
xfreerdp /u:<user> /p:<pass> /d:<domain> /v:<ip> /size:1800x924
```

## xfreerdp - with share
```
xfreerdp /u:<user> /p:<pass> /d:<domain> /v:<ip> /size:1800x924 /drive:share,<share>
```
