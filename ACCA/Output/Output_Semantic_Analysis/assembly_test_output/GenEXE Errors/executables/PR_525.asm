section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push byte 0x68732f2f 
        push byte 0x6e69622f 
        push byte 0x69622f 
        push byte 0x69622f 
        push byte 0x69622f 
        mov ebx, esp
        jmp myExitAddr