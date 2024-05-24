section .data

byte_tbl equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        mov al, [byte_tbl+2]
        jmp myExitAddr