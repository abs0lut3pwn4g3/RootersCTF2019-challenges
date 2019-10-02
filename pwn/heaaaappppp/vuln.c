#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

// create user, delete user, edit user's name, send user a message

struct user
{
    char *name;
    int age;
} * root=NULL;

char *message;

void beNice() {
    setvbuf(stdout,NULL,_IONBF,0);
}

void bye() {
    puts("You must create a user first");
    exit(0);
}

void createUser()
{
    root = malloc(sizeof(struct user));
    char buffer[32];
    printf("Enter age of user: ");
    scanf("%d", &(root->age));
    printf("Enter username: ");
    read(0, buffer, 31);
    root->name = strdup(buffer);
}

void editUsername()
{
    if (root==NULL)
        bye();
    printf("Enter age of user: ");
    scanf("%d", &(root->age));
    printf("Enter username: ");
    read(0, (root->name), 31);
}

void deleteUser()
{
    if (root==NULL)
        bye();
    free(root);
}

void sendMessage()
{
    char buffer[128];
    puts("Enter message to be sent: ");
    read(0, buffer, 127);
    puts("Message recieved: ");
    puts(buffer);
    puts("\nSaving it for admin to see!\n");
    message = strdup(buffer);
}

int main(int argc, char **argv)
{
    int choice;
    beNice();
    while(1) {
        puts("### USER ADMINISTRATION ###\n");
        puts("0) Create user");
        puts("1) Edit user name");
        puts("2) Delete user");
        puts("3) Send admin a message");
        puts("4) exit");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 0:
            createUser();
            break;
        case 1:
            editUsername();
            break;
        case 2:
            deleteUser();
            break;
        case 3:
            sendMessage();
            break;
        case 4:
            exit(0);
        default:
            puts("Wrong choice try again...");
        }
    }
}