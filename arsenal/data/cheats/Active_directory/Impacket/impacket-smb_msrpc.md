# impacket

## smbclient - connect to smb on the target
#platform/linux #target/remote #port/445 #protocol/smb #cat/ATTACK/CONNECT  

A generic SMB client that will let you list shares and files, rename, upload and download files and create and delete directories, all using either username and password or username and hashes combination.

-hashes : <LMHASH:NTHASH>
-no-pass -k : kerberos authentication

```
smbclient.py <domain>/<user>:<password>@<ip>
```

