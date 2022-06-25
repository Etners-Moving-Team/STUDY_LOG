#include <stdio.h>
#include <cs50.h>

int main(){
    float price = get_float("What's the price?\n");
    printf("It's %.2f\n", price);
}