# network

% network, ip

## ip infos (hostname / city / country / isp )
#platform/linux  #target/remote  #cat/UTILS  
```
curl https://ipinfo.io/<ip>
```

## what is my ip
#platform/linux  #target/remote  #cat/UTILS  
```
curl https://ipinfo.io/
```

## what is my ip - plaintext
#platform/linux  #target/remote  #cat/UTILS 
```
curl https://ipecho.net/plain/
```

% network, portquiz

## test an internet port out allow - curl (no 445)
#platform/linux  #target/remote  #cat/UTILS 
```
curl portquiz.net:<port>
```

## test an internet port out allow - nc (no 445)
#platform/linux  #target/remote  #cat/UTILS 
```
nc -v portquiz.net <port>
```
