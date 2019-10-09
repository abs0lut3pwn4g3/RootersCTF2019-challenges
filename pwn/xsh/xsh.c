#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char *poem = {
	"\n\t\tDylan Thomas - 1914-1953\n\n"
	"\tDo not go gentle into that good night,\n"
	"\tOld age should burn and rave at close of day;\n"
	"\tRage, rage against the dying of the light.\n"
	"\n"
	"\tThough wise men at their end know dark is right,\n"
	"\tBecause their words had forked no lightning they\n"
	"\tDo not go gentle into that good night.\n"
	"\n"
	"\tGood men, the last wave by, crying how bright\n"
	"\tTheir frail deeds might have danced in a green bay,\n"
	"\tRage, rage against the dying of the light.\n"
	"\n"
	"\tWild men who caught and sang the sun in flight,\n"
	"\tAnd learn, too late, they grieved it on its way,\n"
	"\tDo not go gentle into that good night.\n"
	"\n"
	"\tGrave men, near death, who see with blinding sight\n"
	"\tBlind eyes could blaze like meteors and be gay,\n"
	"\tRage, rage against the dying of the light.\n"
	"\n"
	"\tAnd you, my father, there on the sad height,\n"
	"\tCurse, bless, me now with your fierce tears, I pray.\n"
	"\tDo not go gentle into that good night.\n"
	"\tRage, rage against the dying of the light.\n"
};

void run(char *prompt){
	if(strncmp(prompt,"ls",2)==0){
		system("/bin/ls -las");
	}else if(strncmp(prompt,"echo",4)==0){
		printf(&prompt[5]);
	}else if(strncmp(prompt,"zooo",4)==0){
		printf("%s\n", poem);
	}else if(strncmp(prompt,"\n",1)==0){
		;
	}else if(strncmp(prompt,"q",1) == 0){
		exit(0);
	}else{
		printf("rsh: command not found: %s",strtok(prompt," "));
	}
}


void main(){
	setvbuf(stdout, NULL, _IONBF, 0);
	char prompt[0x128];
	char pwd[0x128];
	while(1){
		if(getcwd(pwd, 0x64) == NULL){
			puts("BYE");
			exit(1);
		}
		printf("\033[1;31m[xsh]\033[0m-\033[0;34m[%s]\033[0;32m$ ",pwd);
		fgets(prompt,0x128,stdin);
		fflush(stdout); 
		run(prompt);
	}
}
