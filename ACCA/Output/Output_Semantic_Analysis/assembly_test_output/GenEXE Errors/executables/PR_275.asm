section .data

encodedshellcode equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        xor bl, 0xaa 
        jnz encodedshellcode
        jmp myExitAddr