section .data

af_inet6 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        push af_inet6
        jmp myExitAddr