# bloodhound

% bloodhound, Active directory enumeration

## launch neo4j server
```
neo4j console start
```

## launch bloodhound 
```
bloodhound
```

## launch capture bloodhound
```
bloodhound-python -d <domain> -u <user> -p <password> -c all
```

## launch capture bloodhound (2)
```
bloodhound-python -d <domain> -u <user> -p <password> -gc <global_catalog> -dc <domain_controler> -c all
```

## launch cypheroth - toolset that runs cypher queries against Bloodhound's Neo4j backend and saves output to spreadsheets.
cypheroth -u <bh_user|neo4j> -p <bh_password|exegol4thewin> -d <domain>

## aclpwn - from computer to domain - dry run
```
aclpwn -f <computer_name> -ft computer -d <domain> -dry
```


