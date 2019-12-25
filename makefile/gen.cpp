#include<iostream>

using namespace std;

int main(){
    int a=1,b=1,c=1;
    cout<<a<<endl<<b<<endl;
    for(int x=0;x<20;++x){
        c=a+b;
        cout<<c<<endl;
        a=b;
        b=c;
    }
    return 0;
}
