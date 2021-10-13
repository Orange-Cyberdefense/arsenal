# Mysql

% mysql, database, db, 3306
#plateform/linux  #target/remote  #protocol/mysql  #port/3306
## connect
#cat/ATTACK/CONNECT 
```
mysql -u <user> -p<password> -h <hostname> <database>
```

## Create database
#cat/UTILS 
```
mysql -u <user> -p -e "create database <database> character set UTF8mb4 collate utf8mb4_bin"
```

## Export database
#cat/UTILS 
```
mysqldump -u <user> -p <database> > <path>
```

## Import database
#cat/UTILS 
```
mysql -u <user> -p <database> <path>
```

## nmap - mysql enumeration
#cat/RECON 
```
nmap -sV -p 3306 --script mysql-audit,mysql-databases,mysql-dump-hashes,mysql-empty-password,mysql-enum,mysql-info,mysql-query,mysql-users,mysql-variables,mysql-vuln-cve2012-2122 <ip>
```
