#ifndef VM_H
#define VM_H
#include <stdint.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define MAX_SIZE 0x100
#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"

int instructions[0x100];
int long key;

struct VM {
	uint32_t	eip;
	uint32_t	eax, ebx, ecx, edx, esi, edi, r6, r7;
	uint32_t	*reg[10];

	bool	zf,cf;

	bool	is_running;

};

struct arch {
	uint32_t	enc_intr;
	uint32_t	opcode;
	uint32_t	operand_1;
	uint32_t	operand_2;
	uint32_t 	operand_3;
};


struct VM *init_vm();
uint32_t execute(struct VM *, uint32_t);
uint32_t runcpu(struct VM *, int long);
void debug(struct VM *,uint32_t, uint32_t, uint32_t, uint32_t);
#endif