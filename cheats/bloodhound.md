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
