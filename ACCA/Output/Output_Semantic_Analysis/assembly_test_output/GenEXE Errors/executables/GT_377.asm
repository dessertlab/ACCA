section .data

while equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp ax, bx 
        jne l3 
        jmp while
        jmp myExitAddr