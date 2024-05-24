section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov byte [esi], 0x68732f2f 
        mov byte [esi], 0x68732f 
        mov byte [esi], 0x6e69622f 
        mov byte [esi], 0x69622f 
        mov byte [esi], 0x69622f 
        mov byte [esi], 0x6e69622f 
        mov byte [esi], 0x69622f2f 
        mov byte [esi], 0x69622f
        jmp myExitAddr