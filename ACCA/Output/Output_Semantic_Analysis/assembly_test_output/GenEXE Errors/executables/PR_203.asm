section .data

bucle equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        dec ecx 
        jns bucle
        jmp myExitAddr