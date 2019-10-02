section .data
feedback db 'Hey, can i get some feedback for the CTF?',0xa
len equ $-feedback

section .text
global _start

_vuln:
	push rbp
	mov rbp, rsp
	sub rsp, 0x40
	mov rax, 1
	mov rdi, 1
	lea rsi, [feedback]
	mov rdx, len
	syscall
	mov rdi, 0
	lea rsi, [rsp-0x40]
	mov rdx, 0x400
	push 0
	pop rax
	syscall
	leave
	ret
_start:
	call _vuln
	mov rax, 60
	mov rdi, 0
	syscall
