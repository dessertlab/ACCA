section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        sub byte [ebp+ecx],20h
        jmp myExitAddr