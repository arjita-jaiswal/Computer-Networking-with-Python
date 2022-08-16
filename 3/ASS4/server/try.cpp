#include <iostream>
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
    cout<<ret<<endl;
    for (auto i=0;i!=m+r;++i)
        if(ret[i] == '?'){
            ret[i] = get_paritybit(1,m+r+1,1<<k,ret);
            k++;
        }

    return ret;
}
int main()
{
    string msg = "";
    cout<<"Please enter the bitstring: ";
    // bzero(buffer,256);
    // fgets(buffer,255,stdin);
    cin>>msg;
    msg = generate_hammingcode(msg);
    cout<<"-[Bitstring generated after applying Hamming code algorithm: "<<msg<<" ]-"<<endl;
}