section .data

do_inject equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp al, 2 
        jne while 
        jmp do_inject
        jmp myExitAddr