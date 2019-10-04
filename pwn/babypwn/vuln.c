#include<string.h>
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

int main(int argc, char** argv) {
	char buffer[256];
	puts("What do you want me to echo back> ");
	read(0, buffer, 0x256);
	puts(buffer);
	return 0;	
}
