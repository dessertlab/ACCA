section .data

loc_402B1D equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp bl, 78h 
        jge loc_402B1D
        jmp myExitAddr