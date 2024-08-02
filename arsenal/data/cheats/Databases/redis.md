# Redis

% databases
#plateform/linux #target/remote #cat/RECON #cat/ATTACK/CONNECT

## connect to the local server
```bash
redis-cli
```

## connect to a remote server on the default port (6379)
```bash
redis-cli -h <ip> -a <password>
```

## connect remotely specifying a port
```bash
redis-cli -h <ip> -p <port> -a <password>
```

## connect remotely over tls w/ server certificate
```bash
redis-cli -h <ip> --tls --cacert <redis_cert_path.pem>
```

## connect remotely over tls w/ server & client certificates
```bash
redis-cli -h <ip> --tls --cacert <redis_cert_path.pem> --cert <redis_user_path.crt> --key <redis_user_private_path.key>
```
