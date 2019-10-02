#include "vm.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// flag rooters{4027431603}ctf

void check_bytecode(FILE *, char *);
void read_bytecode(FILE *, int *);
void usage(int , char *);
long int findsize(FILE *);

int main(int argc, char *argv[]){

	if( argc !=2 ){
		usage(0x00, argv[0]);
	}

	FILE *exe = fopen(argv[1] ,"rb");
	check_bytecode(exe, argv[0]); 


	
	printf("(xvm): ");
	scanf("%ld", &key);

	struct VM *vm = init_vm();

	read_bytecode(exe,&instructions[0]);
	int long size = findsize(exe)/4;


	uint32_t valid_key = runcpu(vm,size);

	if(!valid_key){
		puts(KRED"Fatal Error: invalid key (cannot decrypt flag)");
		return -1;
	}else{
		puts(KGRN"[!] flag decrypted");
		printf(KGRN"FLAG : rooters{%ld}ctf\n",key);
	}

	return 0;

}

void check_bytecode(FILE *exe, char * filename){
	if( exe == NULL ){
		usage(0x01, filename);
	}
	char magic_header[4];
	fread( magic_header , 1, 4, exe);
	if(strncmp(magic_header, "XVM2", 4) != 0){
		usage(0x02, filename);
	}
}

long int findsize(FILE * exe){

	fseek(exe, 0L, SEEK_END);
	long int size = ftell(exe);
	rewind(exe);
	return (size % MAX_SIZE)-4;
}

void read_bytecode(FILE *bytecode, int *instructions){

	
	long int size = findsize(bytecode);

	fseek(bytecode, 4, SEEK_SET);
	for (int i=0 ; i<(size)/4 ; i++){
		char instr[4];
		fread( instr, 4, 1, bytecode);
		memcpy(&instructions[i], instr, 4);
	}
	rewind(bytecode);
}	

void usage(int error , char *filename){
	printf(KRED);
	switch(error){
		case 0x00: {
			printf("Usage: %s < XVM bytecode file >\n", filename);
			break;
		}
		case 0x01: {
			printf("Fatal Error: Failed to open %s\n", filename);
			break;
		}
		case 0x02: {
			printf("Fatal Error: Currupted bytecode file %s\n", filename);
			break;
		}
		default:
			exit(-9);
	}

	exit(-(error-1));

}
