section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        message: db 'hello world!'
        jmp myExitAddr