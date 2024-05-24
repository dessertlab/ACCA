section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        push 0x04020a0a
        jmp myExitAddr