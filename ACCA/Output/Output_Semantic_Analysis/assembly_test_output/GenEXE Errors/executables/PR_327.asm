section .data

__nr_fork equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        mov al, __nr_fork
        jmp myExitAddr