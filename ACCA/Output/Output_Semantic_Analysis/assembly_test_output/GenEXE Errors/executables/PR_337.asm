section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        for: dd 0x68732f 
        dd 0x68732f 
        dd 0x6e69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x69622f 
        dd 0x6
        jmp myExitAddr