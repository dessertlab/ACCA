section .data

var1 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        mov byte [var1], 0x2f
        jmp myExitAddr