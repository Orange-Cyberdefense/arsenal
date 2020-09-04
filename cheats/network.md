# network

% network, ip

## ip infos (hostname / city / country / isp )
```
curl https://ipinfo.io/<ip>
```

## what is my ip
```
curl https://ipinfo.io/
```

## what is my ip - plaintext
```
curl https://ipecho.net/plain/
```

% network, portquiz

## test an internet port out allow - curl (no 445)
```
curl portquiz.net:<port>
```

## test an internet port out allow - telnet (no 445)
```
telnet portquiz.net <port>
```

## test an internet port out allow - nc (no 445)
```
nc -v portquiz.net <port>
```
