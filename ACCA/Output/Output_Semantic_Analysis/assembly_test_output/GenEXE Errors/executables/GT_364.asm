section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        xor byte [esi + ecx - 1], 0x3
        jmp myExitAddr