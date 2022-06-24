#include <stdio.h>
#include <cs50.h>
/*
    set_positive_int : 사용자 정의함수
    main에서 100미만의 값이 들어올 때 계속 사용자 입력값을 받으며,
    음수일 때 양수로 반환해줌 
*/

int set_positive_int(int n);    //  n은 값이 들어오기 전까지 Garbage Value

int main(){
    int i;
    do{
        i = get_int("정수를 입력해주세요.\n");
        int p = set_positive_int(i);
        printf("%d\n", p);
    }
    while(i<100);   // 100이상 값 나올때까지 do 문 돎
}

int set_positive_int(int n){
    if(n>=0){
        return n;
    }else{
        return -n;
    }
}


