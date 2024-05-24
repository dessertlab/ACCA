section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push byte 0x50905090 
        push 0x50905090 
        push 0x50905090 
        push 0x50905090 
        push 0x50905090 
        push 0x50905090 
        push 0x50905090 
        push 0x509050905090 
        push 0x509050905090 
        push 0x509050905090 
        push 0x509050905090 
        push 0x5090509050905090 
        push 0x5090
        jmp myExitAddr