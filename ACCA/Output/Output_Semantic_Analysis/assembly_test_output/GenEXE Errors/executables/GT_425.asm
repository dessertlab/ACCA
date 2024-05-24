section .data

function_1 equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        F2: 
        call function_1
        jmp myExitAddr