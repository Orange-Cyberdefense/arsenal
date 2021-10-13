# bof

% bof, buffer overflow
#plateform/linux #target/local #cat/PWN

## bof, pattern creation
```
msf-pattern_create -l <size>
```

## bof, pattern offset
```
msf-pattern_offset -l <size> -q <pattern>
```

## bof, nasm - show opcode from asm
```
msf-nasm_shell # nasm > jmp esp
```

% bof, ropgadget

## ropgadget - Specify a binary filename to analyze
```
ROPgadget --binary <binary>
```

## ropgagdet - Enable the ROP chain generation
```
ROPgadget --binary <binary> --ropchain
```

## ropgagdet - Search opcode in executable segment
```
ROPgadget --binary <binary> --opcode <opcode>
```

## ropgadget - Search string between two addresses (0x...-0x...)
```
ROPgadget --binary <binary> --string <string> --range <start_address>-<end_address>
```

## ropgadget - Only show specific instructions
```
ROPgadget --binary <binary> --only="<instructions>"
```

## ropgadget - Suppress specific mnemonics
```
ROPgadget --binary <binary> --filter="<instructions>"
```

% bof, mona

## mona - Show all loaded modules and their properties
```
!mona modules
```

## mona - Configure the log directory (no need to create it)
```
!mona config -set workingfolder <path|c:\logs\%p>
```

## mona - Verify the current the log directory
```
!mona config -get workingfolder
```

## mona - Create a cyclic pattern of a given size
```
!mona pc <pattern_size|400>
```

## mona - Find cyclic pattern in memory
```
!mona findmsp
```

## mona - Find location (offset) of 4 bytes in a cyclic pattern
```
!mona po <pattern_value|41346541>
```

## mona - Find bytes in memory (ex: eggs)
```
!mona find -s <pattern_value|"w00tw00t">
```

## mona - Find pointers that will allow you to jump to a register (without null bytes)
```
!mona jmp -r <reg_name|esp> -n
```

## mona - Find a function in IAT
```
!mona getiat -s <function_name|*strcpy*>
```

## mona - Show the current SEH chain
```
!mona sehchain
```

## mona - Set a breakpoint on all current SEH Handler function pointers
```
!mona bpseh
```

## mona - Find pointers to assist with SEH overwrite exploits (default: no aslr, no rebase, no safeseh)
```
!mona seh
```

## mona - Badchar hunting step 1 - Creates a byte array
```
!mona bytearray -cpb <excluded_bytes|'\x00\x0a\x0d'>
```

## mona - Badchar hunting step 3 - compare until "!!! Hooray, normal shellcode unmodified !!!" message
```
!mona compare -f <input_file|C:\BadChars\bytearray.bin> -a <bytesarray_address|esp>
```

## mona - Finds gadgets that can be used in a ROP exploit and do ROP magic with them (Note : can take 20 minutes)
```
!mona rop -cm aslr=false,rebase=false
```

## mona - Finds stackpivots (move stackpointer to controlled area)
```
!mona stackpivot -cm os=true -distance <min,max|12,12>
```

## mona - Show pointers to pointers to the pattern (might take a while !)
```
!mona find -type file -s <input_file|C:\stackpivot.txt> -p2p
```
