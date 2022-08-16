#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <iostream>
#include<bits/stdc++.h>

using namespace std;
void error(const char *msg)
{
    perror(msg);
    exit(1);
}

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
            ret = ret + s[i];
    }
    // cout<<ret<<endl;
    for (auto i=0;i!=m+r;++i)
        if(ret[i] == '?'){
            ret[i] = get_paritybit(1,m+r+1,1<<k,ret);
            k++;
        }

    return ret;
}

int main(int argc, char *argv[])
{
    int sockfd, newsockfd, portno;
    socklen_t clilen;
    char buffer[256];
    struct sockaddr_in serv_addr, cli_addr;
    int n;
    if (argc < 2) {
        fprintf(stderr,"ERROR, no port provided\n");
        exit(1);
    }
    // create a socket
    // socket(int domain, int type, int protocol)
    sockfd =  socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");

    // clear address structure
    bzero((char *) &serv_addr, sizeof(serv_addr));

    portno = atoi(argv[1]);

    /* setup the host_addr structure for use in bind call */
    // server byte order
    serv_addr.sin_family = AF_INET;  

    // automatically be filled with current host's IP address
    serv_addr.sin_addr.s_addr = INADDR_ANY;  

    // convert short integer value for port must be converted into network byte order
    serv_addr.sin_port = htons(portno);

    if (bind(sockfd, (struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0) 
        error("ERROR on binding");

    listen(sockfd,10);
    while(true) {
       
        clilen = sizeof(cli_addr);

        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0) 
            error("ERROR on accept");
        //cout<<"-[Client Connected with IP addresss:- "<<inet_ntoa(serv_addr.sin_addr)<<" ]-"<<endl;

        // This send() function sends the 13 bytes of the string to the new socket

        bzero(buffer,256);

        // Read the message
        n = read(newsockfd,buffer,255);
        if (n < 0) error("ERROR reading from socket");
        printf("Message: %s\n",buffer);

        // -----------------------Start Solving Query-----------------------
        
        stringstream ss;
        ss<<buffer;
        string msg;
        ss>>msg;

        int error_cnt = 0;
        int idx = 0;
        string comp = generate_hammingcode(msg);
        // cout<<"Debug compare string : "<<comp<<endl;
        int l = comp.length();
        for (auto i = l-1; i != -1; i--)
            if((i+1 & i) == 0)
                idx = idx*2 + (int(comp[i])^int(msg[i]));

        idx--;
        // cout<<"Debug index corrected: "<<idx<<endl;
        
        if (msg[idx] == '0')
            msg[idx] = '1';
        else
            msg[idx] = '0';

        string ans = "";
        for (auto i = 0; i != l; ++i)
            if((i+1 & i) != 0)
                ans += msg[i];

        bzero(buffer,256);
        stringstream ss2;
        ss2<<ans;
        ss2>>buffer;

        // -----------------------End of Query-----------------------

        cout<<"After correcting error :"<< buffer <<" ]-"<<endl;
        send(newsockfd,buffer,strlen(buffer),0);
        send(newsockfd,"\n",1,0);
    }

    // close the connections
    close(newsockfd);
    close(sockfd);
    return 0; 
}
