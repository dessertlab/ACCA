section .data

af_inet equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        push for 
        push af_inet
        jmp myExitAddr