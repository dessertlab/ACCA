section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        xor eax, 0x68732f2f 
        xor eax, 0x68732f 
        xor eax, 0x6e69622f 
        xor eax, 0x69622f 
        xor eax, 0x69622f 
        xor eax, 0x69622f 
        xor eax, 0x69622f 
        xor eax, 0x69622f2f 
        xor eax, 0x69622f2f 
        xor eax, 0x69622f
        jmp myExitAddr