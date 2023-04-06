# Postgres

% postgres, 5432, 5433
#plateform/linux  #target/remote  #protocol/postgres #port/5432 #port/5433

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

## postgres - dump database
#cat/ATTACK/DUMP
```
pg_dump -h <ip> -p <port> -U <user> -d <database> --no-owner > db-backup-"$(date +%d-%m-%Y)".sql
```

## postgres - dumb all tables as csv
#cat/ATTACK/DUMP
```
psql -h <ip> -p <port> -U <user> -Atc "select schema_name from information_schema.schemadata" | \
    while read -r SCHEMA; do
    if [[ "$SCHEMA" != "pg_catalog" && "$SCHEMA" != "information_schema" ]]; then
        echo "[+] Dumping ${SCHEMA} to .csv"
        psql -U <user> -h <ip> -p <port> -d <database> -Atc "select tablename from pg_tables where schemaname='$SCHEMA'" |\
            while read -r TBL; do
                echo "  -> dumping ${TBL}..."
                psql -U <user> -h <ip> -p <port> -d <database> \
                    -c "COPY $SCHEMA.$TBL TO STDOUT WITH CSV DELIMITER ';' HEADER ENCODING 'UTF-8'" > "${SCHEMA}"."${TBL}".csv
            done

            echo "[+] Done."
    fi
    done
```
