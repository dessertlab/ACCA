section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov eax, 0x68732f2f 
        jmp myExitAddr