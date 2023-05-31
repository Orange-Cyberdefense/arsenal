# Postgres

% postgres, 5432, 5433
#platform/linux  #target/remote  #protocol/postgres #port/5432 #port/5433

## postgres - connect
#cat/ATTACK/CONNECT 
```
psql -h <host> -U <user>
```

## postgres - connect database
#cat/ATTACK/CONNECT 
```
psql -h <ip> -U <user> -d <database>
```

## postgres - connect full options
#cat/ATTACK/CONNECT 
```
psql -h <ip> -p <port> -U <user> -W <password> <database>
```
