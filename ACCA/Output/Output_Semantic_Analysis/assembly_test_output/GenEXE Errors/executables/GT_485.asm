section .data

myExitAddr db 0x56

section .text

global my_start

my_start:

        mov dword [esp-0x24], 0x732f636f
        jmp myExitAddr