section .data

checkforfile equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        test eax, eax 
        jnz checkforfile
        jmp myExitAddr