# winrm

% windows, remote, winrm, evilwinrm, 5985, 5986

## Enable winrm (powershell)
```powershell
Enable-PSRemoting -Force  
Set-Item wsman:\localhost\client\trustedhosts *  
```

## Enable winrm (wmic)
```batchfile
wmic /node:<REMOTE_HOST> process call create "powershell enable-psremoting -force"
```

## Test target is configure to use winrm (powershell)
```powershell
Test-WSMan -computername <computername>
```

## Execute a command on the target over winrm (powershell)
```powershell
Invoke-Command -computername <computername> -ScriptBlock {<cmd>} -credential <domain>\<username>
```

## Execute a script on the target over winrm (powershell)
```powershell
Invoke-Command -ComputerName <computername> -FilePath <path_to_script> -credential <domain>\<username>
```

## Get a powershell session with winrm (powershell)
```powershell
Enter-PSSession -ComputerName <computername> -Credential <domain>\<username>
```

## Enable winrm remotelly from psexec
```batchfile
.\PsExec.exe \\<computername> -u <domain>\<username> -p <password> -h -d powershell.exe "enable-psremoting -force"  
```

## evil-winrm install
```
gem install evil-winrm
```

## evil-winrm use
```
evil-winrm -i <ip>/<domain> -u <user> -p <password>
```

## evil-winrm use pass the hash
```
evil-winrm -i <ip>/<domain> -u <user> -H <hash>
```