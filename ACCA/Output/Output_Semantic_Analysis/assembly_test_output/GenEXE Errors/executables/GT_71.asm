section .data

loop equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp edx, 0x43 
        ja loop 
        push edx
        jmp myExitAddr