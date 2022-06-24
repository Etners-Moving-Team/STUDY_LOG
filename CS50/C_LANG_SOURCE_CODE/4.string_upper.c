#include <stdio.h>
#include <ctype.h>  //toupper 존재
#include <cs50.h>
#include <string.h> //strlen 존재

int main(void){
    string s = get_string("String: ");
    printf("After: ");
    for(int i=0; i<strlen(s); i++){
        printf("%c", toupper(s[i]));
    }
}
