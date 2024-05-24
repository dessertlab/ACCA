section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x65782e2f 
        push 0x706d742f
        jmp myExitAddr