#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <iostream>
#include <sstream>
using namespace std;

int calc_r(int m)
{
    for(int i = 0; i <= m; ++i)
        if ((1 << i) >= m+i+1)
            return i;
}

char get_paritybit(int start, int end, int comp, string s)
{
    int cnt = 0,ans = 0, n = s.length();
    for(auto i = start;i!=end;i++)
    {
        if (i&comp)
            if (s[i-1] == '1')
                cnt++;
    }
    if ((cnt&1) == 0)
        return '0';
    return '1';
}

string generate_hammingcode(string s)
{
    int  m = s.length();
    int r = calc_r(m);
    int j = 0;
    string ret = "";
    int k=0;
    for(auto i=0;i!=m+r;i++){
        if ((i+1 & i) == 0)
            ret = ret + '?';
        else
            ret = ret + s[j++];
    }
    // cout<<ret<<endl;
    for (auto i=0;i!=m+r;++i)
        if(ret[i] == '?'){
            ret[i] = get_paritybit(1,m+r+1,1<<k,ret);
            k++;
        }

    return ret;
}

void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;
    char buffer[256];
    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, (char *)&serv_addr.sin_addr.s_addr, server->h_length);
    serv_addr.sin_port = htons(portno);
    if (connect(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
        error("ERROR connecting");

    // Input
    string msg = "";
    cout<<"Please enter the bitstring: ";
    // bzero(buffer,256);
    // fgets(buffer,255,stdin);
    cin>>msg;
    msg = generate_hammingcode(msg);
    cout<<"-[Bitstring generated after applying Hamming code algorithm: "<<msg<<" ]-"<<endl;
    // generate error
    int idx;
    idx = rand()%(msg.length());
    if (msg[idx] == '1')
        msg[idx] = '0';
    else
        msg[idx] = '1';
    cout<<"-[Bitstring after generating error: "<<msg<<" ]-"<<endl;

    stringstream ss;
    ss<<msg;
    ss>>buffer;

    // Send mssg to Server
    n = write(sockfd, buffer, strlen(buffer));
    if (n < 0)
         error("ERROR writing to socket");
    bzero(buffer,256);

    // Read the message got from Server
    n = read(sockfd, buffer, 255);
    if (n < 0) 
         error("ERROR reading from socket");
    else
        printf("Bitstring got from server :%s\n", buffer);

    // Close the connection
    close(sockfd);
    return 0;
}
