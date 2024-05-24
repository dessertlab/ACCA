section .data

_encodedshellcode equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp cl, dl 
        je _encodedshellcode
        jmp myExitAddr