section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov long [esi+26], eax
        jmp myExitAddr