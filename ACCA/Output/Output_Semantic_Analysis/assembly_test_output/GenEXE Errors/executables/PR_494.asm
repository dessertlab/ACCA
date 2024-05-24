section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov eax, 0x68732f2f 
        mov eax, 0x6e69622f
        jmp myExitAddr