section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov al, 0x68732f2f 
        mov al, 0x68732f 
        mov al, 0x6e69622f 
        mov al, 0x69622f 
        mov al, 0x69622f 
        mov al, 0x69622f 
        mov al, 0x69622f 
        mov al, 0x6e69622f 
        mov al, 0x69622f 
        mov al, 0x6e69622f 
        mov al, 0x69622
        jmp myExitAddr