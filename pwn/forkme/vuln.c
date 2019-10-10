// Server side C/C++ program to demonstrate Socket programming
#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#define PORT 4444

void getMessage(int clientfd) {
    char buffer[128];
    char message[] = "What do you want?\n";
    write(1, message, strlen(message));
    read(0, buffer, 0x128);
}

void vuln(int clientfd) {
    char decline[] = "No way you are getting any flag!!!";
    close(0);
    close(1);
    dup(clientfd);
    dup(clientfd);
    getMessage(clientfd);
    write(1, decline, strlen(decline));
    close(clientfd);
    exit(0);
}


int main(int argc, char const *argv[])
{
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);
    char buffer[1024] = {0};
    int slavePid;

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Forcefully attaching socket to the port 4444
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
                   &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // Forcefully attaching socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address,
             sizeof(address)) < 0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 4096) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    while (1)
    {
        if ((new_socket = accept(server_fd, (struct sockaddr *)&address,
                                 (socklen_t *)&addrlen)) < 0)
        {
            perror("accept");
            exit(EXIT_FAILURE);
        }
        else
        {
            if((slavePid = fork()) == 0) {
                vuln(new_socket);
            } else if(slavePid < 0) {
                perror("Can't fork anymore");
                exit(EXIT_FAILURE);
            }
        }
    }
    return 0;
}
