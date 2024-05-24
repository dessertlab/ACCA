section .data

loop2 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        jns loop2
        jmp myExitAddr