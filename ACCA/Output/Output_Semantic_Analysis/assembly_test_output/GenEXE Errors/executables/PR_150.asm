section .data

child equ 0x42
myExitAddr db 0x56

section .text

global my_start

my_start:

        cmp eax, ebx 
        jne child
        jmp myExitAddr