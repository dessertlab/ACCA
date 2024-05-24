section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x68732f2f 
        push 0x68732f2f 
        push 0x2f656c2d
        jmp myExitAddr