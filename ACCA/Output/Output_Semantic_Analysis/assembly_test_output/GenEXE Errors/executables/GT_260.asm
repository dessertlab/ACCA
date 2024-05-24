section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        L1: 
        jmp short esp
        jmp myExitAddr