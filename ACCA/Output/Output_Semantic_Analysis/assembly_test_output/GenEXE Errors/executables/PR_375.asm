section .data

stack equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        decoded_shellcode: 
        call stack
        jmp myExitAddr