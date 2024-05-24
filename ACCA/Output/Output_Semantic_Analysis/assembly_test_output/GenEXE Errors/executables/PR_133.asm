section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov ax, 1000h
        jmp myExitAddr