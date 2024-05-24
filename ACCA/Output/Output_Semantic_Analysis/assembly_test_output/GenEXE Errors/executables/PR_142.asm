section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x68732f2f 
        push 0x6e69622f 
        push 0x69622f 
        mov eax, esp
        jmp myExitAddr