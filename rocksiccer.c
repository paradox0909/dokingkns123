#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int you, com;
    char name[3][10] = {
        "가위", "바위", "보"
    };
    printf("가위(1)바위(2)보(3): ");
    scanf("%d", &you);

    you--;
    srand(time(NULL));
    com = rand() % 3;
    printf("당신: %s 컴:%s", name[you], name[com]);
    if ((you + 1) % 3 == com)
        printf("컴 Win!`n");
    else if ((com + 1) % 3 == you)
        printf("당신 Win!`n");
    else       
            printf("비김!₩n");
}