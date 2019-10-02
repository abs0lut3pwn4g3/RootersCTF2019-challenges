#include "vm.h"
#include <stdio.h>

struct VM *init_vm(){
	struct VM *vm = malloc(sizeof(struct VM));
	vm->reg[0] =	&vm->eax;
	vm->reg[1] =	&vm->ebx;
	vm->reg[2] =	&vm->ecx;
	vm->reg[3] =	&vm->edx;
	vm->reg[4] =	&vm->esi;
	vm->reg[5] =	&vm->edi;
	vm->reg[6] =	&vm->r6;
	vm->reg[7] =	&vm->r7;
	vm->reg[8] = 	(uint32_t *) &vm->zf;
	vm->reg[9] = 	(uint32_t *) &vm->cf;
	vm->zf	=	false;
	vm->cf	=	false;

	vm->is_running	=	true;

	return vm;
}

struct arch decode(uint32_t instruction){

	struct arch arch_vm;

	arch_vm.opcode	  = (instruction & 0xff000000) >> 24;
	arch_vm.operand_1 = (instruction & 0x00ff0000) >> 16;
	arch_vm.operand_2 = (instruction & 0x0000ff00) >>  8;
	arch_vm.operand_3 = (instruction & 0x000000ff)		;

	return arch_vm;
}


uint32_t execute(struct VM *vm, uint32_t instruction){

	struct arch vm_arch = decode(instruction);
	uint32_t opcode = vm_arch.opcode;
	uint32_t operand_1 = vm_arch.operand_1 & 0xff;
	uint32_t operand_2 = vm_arch.operand_2 & 0xff;
	uint32_t operand_3 = vm_arch.operand_3 & 0xff;

//	debug(vm,opcode,operand_1,operand_2, operand_3);
	

	switch(opcode){
		case 0x0f: {
			/*
			 * load the global variable key to eax;
			 */

			vm->r7 = key;
			break;
		}
		case 0x01: {
			/*
			 * xor reg[operand_1], reg[operand_2];
			 */
			vm->eax = *vm->reg[operand_1] ^ *vm->reg[operand_2];
			break;
		}

		case 0x02: {
			/*
			 * and operand_1, operand_2; 
			 */
			vm->eax = operand_1 & operand_2;
			break;
		}

		case 0x03: {
			/*
			 * or operand_1, operand_2; 
			 */
			vm->eax = operand_1 | operand_2;
			break;
		}

		case 0x04: {
			/*
			 * movi reg_op1, imm32_op2;
			 */
			
			*vm->reg[operand_1] = instructions[++vm->eip];

			break;

		}

		case 0x05: {
			/*
			 * cmp reg[operand_1], reg[operand_2];
			 */

			if(*vm->reg[operand_1] < *vm->reg[operand_2]){
				vm->zf = false;
				vm->cf = true;
			}
			if(*vm->reg[operand_1] == *vm->reg[operand_2]){
				vm->zf = true;
				vm->cf = false;
			}


			break;

		}

		case 0x06: {
			/*
			 * return the value in edx and halt the vm
			 */
			vm->is_running = 0;
			return vm->zf;
		}

	}

	return 0;
	
}

/*
void	debug(struct VM *vm,uint32_t opc, uint32_t op1, uint32_t op2, uint32_t op3){
	puts("DEBUGGING MODE");
	printf("opc: 0x%x\n", opc);
	printf("op1: 0x%x\n", op1);
	printf("op2: 0x%x\n", op2);
	printf("op3: 0x%x\n", op3);
	printf("eax: 0x%x\n", vm->eax);
	printf("ebx: 0x%x\n", vm->ebx);
	printf("ecx: 0x%x\n", vm->ecx);
	printf("edx: 0x%x\n", vm->edx);
	printf("esi: 0x%x\n", vm->esi);
	printf("edi: 0x%x\n", vm->edi);
	printf("r6 : 0x%x\n", vm->r6);
	printf("r7 : 0x%x\n", vm->r7);
	printf("zf : 0x%x\n", (uint32_t) vm->zf);
	printf("cf : 0x%x\n", (uint32_t) vm->cf);

}
*/


uint32_t runcpu(struct VM *vm, int long size){

	uint32_t ret;

	while(vm->is_running){

		ret = execute(vm,instructions[vm->eip]);
		vm->eip++;
	}
	free(vm);
	return ret;
}