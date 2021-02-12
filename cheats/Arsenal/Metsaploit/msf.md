# MSF

% metasploit

## upgrade session to meterpreter
#plateform/linux #target/remote #cat/ATTACK/CONNECT  
```
sessions -u <session_id>
```

## show session list
#plateform/linux #target/remote #cat/ATTACK/CONNECT
```
sessions -l
```

## print route table
#plateform/linux #target/remote #cat/PIVOT/TUNNEL-PORTFW 
```
route print
```

## add pivot
#plateform/linux #target/remote #cat/PIVOT/TUNNEL-PORTFW 
```
use multi/manage/autoroute
```

## add socks proxy
#plateform/linux #target/remote #cat/PIVOT/TUNNEL-PORTFW 
```
use auxiliary/server/socks_proxy
```
