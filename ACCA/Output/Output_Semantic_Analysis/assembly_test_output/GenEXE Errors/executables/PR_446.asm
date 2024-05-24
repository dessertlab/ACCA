section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        word1: db 65535
        jmp myExitAddr