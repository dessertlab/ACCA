section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov cl, 0x68732f2f 
        add cl, 0x68732f 
        add cl, 0x6e69622f 
        add cl, 0x69622f 
        add cl, 0x69622f 
        add cl, 0x69622f 
        add cl, 0x69622f 
        add cl, 0x6e69622f 
        add cl, 0x6e69622f 
        add cl, 0x69622f2f 
        add cl, 0x6
        jmp myExitAddr