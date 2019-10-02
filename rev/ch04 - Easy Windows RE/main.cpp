#include <windows.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>
#define PSWD_ENTRD 0


// flag - rooters{6675636b}ctf


// Window declaration
HWND hEdit;

void AddControls(HWND);
char * wchar_to_char(wchar_t*);


LRESULT CALLBACK WindowProcedure(HWND,UINT,WPARAM,LPARAM);

char char_to_hex(char n){
    char j;

	if(n >= 0x61 && n <= 0x7a){
		j = (n - 0x57);
	}else if(n >= 0x41 && n <= 0x5a){
		j = (n - 0x37);
	}else if(n >= 0x30 && n <= 0x39){
		j = (n - 0x30);
	}
	return j;
}

void str_to_hex(char *src, char *dest){
	for(int i=strlen(src),j = 0; i>=0;i-=2){
		dest[j] = (char_to_hex(src[i])*16)  + char_to_hex(src[i+1]);
		j++;
	}
}

void number_sequence(int n, int *array){ 

	array[0] = 0;

	for (int i=1; i< n; i++){
		int curr = array[i-1] - i;
		int j;
		for (j = 0; j < i; j++){
			if ((array[j] == curr) || curr < 0){
				curr = array[i-1] + i;
				break;
			}
		}

		array[i] = curr;
	}
}

int check_password(char *passwd){
	size_t size = strlen(passwd);
	
	int result = 1;
	if(size!=8){
		return 1;
	}
	char k[16] = {};
	str_to_hex(passwd,k);
	
	uint32_t inp = *(uint32_t *)(k+1);

	uint32_t a	=	(inp & 0xff000000)>> 24;
	uint32_t b	=	(inp & 0x00ff0000)>> 16;
	uint32_t c	=	(inp & 0x0000ff00)>> 8;
	uint32_t d	=	(inp & 0x000000ff);

	int arr[4000];
	number_sequence(4000,arr);


	if((a==arr[383]) && (b==arr[166]) && (c==arr[389]) && (d==arr[373])){
		result = 0;
	}else{
		result = 1;
	}


	return result;

}



LRESULT CALLBACK WindowProcedure(HWND hWnd,UINT msg,WPARAM wp,LPARAM lp){
	
	
	switch(msg){
		case WM_COMMAND:
			switch(wp){
				case PSWD_ENTRD:
					wchar_t buff[100];
					GetWindowTextW(hEdit,buff,100);
					char * str = wchar_to_char(buff);
					if(check_password(str)){
						MessageBoxW(NULL,L"Wrong Password",L"Error",MB_OK);
					}else{
						MessageBoxW(NULL,L"Submit the flag as rooters{(password)}ctf",L"Correct",MB_OK);
					}
					break;

			}break;
		case WM_CREATE:
			AddControls(hWnd);
			break;
		case WM_DESTROY:
			PostQuitMessage(0);
			break;
	}
	return DefWindowProcW(hWnd,msg,wp,lp);
}

void AddControls(HWND hWnd){
	
	// Enter Password Label
	CreateWindowW(
		L"Static",
		L"Enter Password: ",
		WS_VISIBLE | WS_CHILD | SS_CENTER ,
		30,50,150,20,
		hWnd,
		NULL,
		NULL,
		NULL
	);

	// Password TextBox
	hEdit = CreateWindowW(
		L"Edit",
		L"",
		WS_VISIBLE|WS_CHILD|WS_BORDER,
		190,50,200,20,
		hWnd,
		NULL,
		NULL,
		NULL
	);

	// Login Button
	CreateWindowW(
		L"Button",
		L"Login",
		WS_VISIBLE | WS_CHILD,
		200,80,70,30,
		hWnd,
		NULL,
		NULL,
		NULL
	);
}

// convert wchar to char

char* wchar_to_char(wchar_t* pwchar){
	int currentCharIndex = 0;
	char currentChar = pwchar[currentCharIndex];

	while (currentChar != '\0'){
		currentCharIndex++;
		currentChar = pwchar[currentCharIndex];
	}

	const int charCount = currentCharIndex + 1;
	char* char_str = (char*)malloc(sizeof(char) * charCount);

	for (int i = 0; i < charCount; i++){
		char character = pwchar[i];
		*char_str = character;
		char_str += sizeof(char);
	}
	char_str += '\0';
	char_str -= (sizeof(char) * charCount);
	return char_str;
}

int WINAPI WinMain(HINSTANCE hInst, HINSTANCE hPrevInst, LPSTR args, int ncmdshow){
	
	

	WNDCLASSW wc = {0};

	wc.hbrBackground= (HBRUSH)COLOR_WINDOW;
	wc.hCursor 		= LoadCursor(NULL,IDC_ARROW);
	wc.hInstance 	= hInst;
	wc.lpszClassName= L"crackmewindow";
	wc.lpfnWndProc	= WindowProcedure ;
	
	if (!RegisterClassW(&wc)){
		return -1;
	}
	// Main Window
	CreateWindowW(
		L"crackmewindow",
		L"Crackme",
		WS_OVERLAPPEDWINDOW | WS_VISIBLE,
		100,70,500,200,
		NULL,
		NULL,
		NULL,
		NULL
	);

	MSG msg = {0};
	
	while(GetMessage(&msg,NULL,0,0)){
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}

	return 0;

}
