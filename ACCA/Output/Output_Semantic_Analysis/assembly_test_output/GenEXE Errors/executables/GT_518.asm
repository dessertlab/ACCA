section .data

shellcode_section equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        jmp short shellcode_section
        jmp myExitAddr