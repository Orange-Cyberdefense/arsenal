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

% bof, mona

## mona show modules info
```
!mona modules
```

## mona - find JMP ESP
```
!mona find -s "\xff\xe4" -m <dll_file>
```

% bof, ropgadget

## ropgadget - find gadgets
```
ROPgadget --binary <binary>
```

## ropgagdet - create a ROP chain
```
ROPgadget --binary <binary> --ropchain
```

## ropgagdet - search opcode in executable segment
```
ROPgadget --binary <binary> --opcode <opcode>
```

## ropgadget - search a string between two addresses (0x...-0x...)
```
ROPgadget --binary <binary> --string <string> --range <start_address>-<end_address>
```

## ropgadget - only show specific instructions
```
ROPgadget --binary <binary> --only="<instructions>"
```

## ropgadget - suppress specific mnemonics
```
ROPgadget --binary <binary> --filter="<instructions>"
```