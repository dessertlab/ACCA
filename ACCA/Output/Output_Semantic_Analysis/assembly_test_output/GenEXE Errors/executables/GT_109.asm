section .data

write equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        call write
        jmp myExitAddr