section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x6d6f632e 
        push 0x656c676f 
        push 0x6f672031 
        push 0x2e312e31 
        push 0x2e373231
        jmp myExitAddr