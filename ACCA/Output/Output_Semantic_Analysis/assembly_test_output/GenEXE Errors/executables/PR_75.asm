section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push word 0x68732f2f 
        push word 0x6e69622f 
        push word 0x69622f 
        push word 0x69622f
        jmp myExitAddr