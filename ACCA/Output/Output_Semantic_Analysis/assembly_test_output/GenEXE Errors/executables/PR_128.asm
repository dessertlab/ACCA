section .data

_start equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        jns _start-0x24
        jmp myExitAddr