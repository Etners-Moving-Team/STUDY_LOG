#include <stdio.h>
#include <cs50.h>

float get_average(int, int []);

int main(void){
    // 사용자로부터 점수의 갯수 입력
    int n = get_int("과목 개수: ");

    int Scores[n];  // 점수 배열 할당
    for(int i=0; i<n; i++){ // 사용자가 입력한 값만큼 정수 입력 받기
        Scores[i] = get_int("점수 값 %i:", i);
    }
    printf("평균: %.1f", get_average(n, Scores));
}

float get_average(int n, int array[]){
    int sum = 0; // 합계

    for(int i=0; i<n; i++){
        sum += array[i];
    }
    return (float)sum / n;
}
