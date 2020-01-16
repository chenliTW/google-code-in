#include<iostream>
#include<time.h>
#include<stdlib.h>

using namespace std;

int board[20];

void print_answer(){
    for(int i=0;i<20;++i){
        for(int j=0;j<20;++j){
            if(board[i]!=j){
                cout<<"_";
            }else{
                cout<<"Q";
            }
        }
        cout<<endl;
    }
    cout<<endl<<endl;
    exit(0);
}

bool triggered(int x,int y){
    for(int i=0;i<x;++i){
        if(board[i]==y){
            return 1;
        }
    }
    for(int i=x-1;i>=0;--i){
        if(board[i]==y-(x-i)||board[i]==y+(x-i)){
            return 1;
        }
    } 
    return 0;
}

void place_queen(int step){
    int random=rand()%15;
    for(int i=random;i<20;++i){
        if(triggered(step,i)==0){
            board[step]=i;
            if(step==19){
                print_answer();
            }else{
                place_queen(step+1);
            }
        }
    }
}

int main(){
    srand(time(NULL));
    place_queen(0);    


    return 0;
}