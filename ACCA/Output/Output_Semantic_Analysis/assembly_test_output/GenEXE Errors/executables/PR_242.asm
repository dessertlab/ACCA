section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        section 
        uninitialized: db 0x68732f2f 
        db 0x6e69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f 
        db 0x69622f2f 
        db 0x69622
        jmp myExitAddr