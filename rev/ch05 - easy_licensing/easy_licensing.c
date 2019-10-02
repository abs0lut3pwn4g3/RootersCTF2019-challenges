#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

// flag = rooters{1t_w4s_eazy_i_t0ld_ya__:P_}ctf;

bool check_password(char *, size_t);
char *enc_flag = "\x54\x49\x49\x52\x43\x54\x55\x5d\x17\x52\x79\x51\x12\x55\x79\x43\x47\x5c\x5f\x79\x4f\x79\x52\x16\x4a\x42\x79\x5f\x47\x79\x79\x1c\x76\x79\x5b\x45\x52\x40";

char fail_msgs[15][64] = {
	"Go book an appointment with a GOOD Doctor\n",
	"Are you really Trying hard? :P\n",
	"lol you are so slow.\n",
	"go learn some hacking.\n",
	"your cpu seems halted.\n",
	"Seriosly?\n",
	"Yes, I know what year it is.\n",
	"NO.\n",
	"You still here? LOL\n",
	"Just Enter the Correct Password, is it that hard?\n",
	"Are you on Drugs?\n",
	"Just get the fuck out\n",
	"My pet Dog is a better Reverse Engineer Than you\n",
	"You do that again and see what happens...",
	"I've seen penguins that can do better than this\n",
};



int main(int argc, char *argv[]){
	

	srand(time(NULL));
	// check for command line arguments
	if(argc < 2){
		printf("Usage: %s <key>\n",argv[0]);
		return -1;
	}

	// length of the user input
	size_t len = strlen(argv[1]);

	bool auth = check_password(argv[1],len);

	if(auth){
		puts("Correct Password!!!!!!!");
		return 0;
	} else {
		printf("%s",fail_msgs[rand()%14] );
		return -1;
	}

}


bool check_password(char *passwd, size_t len){
	int result = 0;

	for (int i=0; i<len; i++){
		result |= (passwd[i] ^ len) ^ enc_flag[i]; 
	}

	return result == 0;
}