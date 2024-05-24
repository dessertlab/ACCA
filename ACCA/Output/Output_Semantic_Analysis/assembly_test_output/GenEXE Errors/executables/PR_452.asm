section .data

_while_loop equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        test eax, eax 
        jns _while_loop
        jmp myExitAddr