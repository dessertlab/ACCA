section .data

var3 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        mov ebx, var3
        jmp myExitAddr