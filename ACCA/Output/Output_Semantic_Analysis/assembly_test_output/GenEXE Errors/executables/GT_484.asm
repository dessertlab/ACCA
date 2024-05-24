section .data

zero_reg equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        lea ecx, [zero_reg+117]
        jmp myExitAddr