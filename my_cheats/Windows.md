# Windows

## winrm - start winrm service
```
winrm quickconfig
```

## PowerShell - allow winrm connections
```
Enable-PSRemoting -force
```

## netsh - enable network discovery
```
netsh advfirewall firewall set rule group=”network discovery” new enable=yes
```

## PowerShell - set network type to private
```
Set-NetConnectionProfile -NetworkCategory Private
```

## PowerShell - deactivate Windows Defender firewall
```
Set-NetFirewallProfile -Profile Domain,Private,Public -Enabled False
```

## PowerShell - set new password for <user>
```
$Password = ConvertTo-SecureString "<password>" -AsPlainText -Force;
Set-LocalUser -Name "<user>" -Password $Password
```

## PowerShell - disable Microsoft Defender
```
Set-MpPreference -DisableRealtimeMonitoring $true
```

## PowerShell - list running processes
#platform/windows #target/local #cat/[OWN]
```
Get-CimInstance -ClassName win32_service | Select Name,State,PathName | Where-Object {$_.State -like 'Running'}
```

## icacls - list permissions of file
```
icacls <file|C:\>
```

## wmic - list processes detailed
```
wmic process list full
```

## wmic - list services detailed
```
wmic service list full
```


FALSE        FALSE       Microsoft Defender Antivirus Network Inspection Service                             0           Win32_Service      FALSE             Helps guard against intrusion attempts targeting known and newly discovered vulnerabilities in network
protocols


                             FALSE            Microsoft Defender Antivirus Network Inspection Service                             Normal                   1077                   WdNisSvc                                   "C:\ProgramData\Microsoft\Windows
Defender\Platform\4.18.2207.7-0\NisSrv.exe"            0                                            0                        Own Process    FALSE          Disabled   NT AUTHORITY\LocalService    Stopped                      OK       Win32_ComputerSystem     DEV04
          0      0
FALSE        FALSE       Microsoft Defender Antivirus Service                                                0           Win32_Service      FALSE             Helps protect users from malware and other potentially unwanted software



                    FALSE            Microsoft Defender Antivirus Service                                                Normal                   1077                   WinDefend                                  "C:\ProgramData\Microsoft\Windows
Defender\Platform\4.18.2207.7-0\MsMpEng.exe"           0                                            0                        Own Process    FALSE          Disabled   LocalSystem                  Stopped                      OK       Win32_ComputerSystem     DEV04
          0      0