# bof

% bof, buffer overflow

## bof, pattern creation
```
msf-pattern_create -l <size>
```

## bof, pattern offset
```
msf-pattern_offset -l <size> -q <pattern>
```

## bof, nasm - show opcode from asm
```
msf-nasm_shell # nasm > jmp esp
```

% bof, mona

## mona show modules info
```
!mona modules
```

## mona - find JMP ESP
```
!mona find -s "\xff\xe4" -m <dll_file>
```
