section .data

__nr_execve equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        push __nr_execve 
        pop eax
        jmp myExitAddr