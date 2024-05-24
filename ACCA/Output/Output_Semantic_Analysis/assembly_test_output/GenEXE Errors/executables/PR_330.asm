section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2 
        push dword 0x2
        jmp myExitAddr