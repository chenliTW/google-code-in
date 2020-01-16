#include<iostream>
#include<time.h>
#include<stdlib.h>

using namespace std;

int board[20];

void print_answer(){//print out the answer
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
    exit(0);//exit the program because we only need one answer
}

bool triggered(int x,int y){//check if the queen get killed
    for(int i=0;i<x;++i){//same column kill
        if(board[i]==y){
            return 1;
        }
    }
    for(int i=x-1;i>=0;--i){//cross kill
        if(board[i]==y-(x-i)||board[i]==y+(x-i)){
            return 1;
        }
    } 
    return 0;//safe for the queen
}

void place_queen(int step){//place the queen for row "step"
    int random=rand()%15;//random the start of i
    for(int i=random;i<20;++i){//try througth all coulmns
        if(triggered(step,i)==0){//check if this place is safe for now
            board[step]=i;
            if(step==19){//if placing is done
                print_answer();
            }else{
                place_queen(step+1);//place next row
            }
        }
    }
}

int main(){
    srand(time(NULL));
    place_queen(0);//start with row 0


    return 0;
}