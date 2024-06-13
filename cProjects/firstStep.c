#include <stdio.h>

int main(void)
{
    /*  int usf, euf;
    printf("Enter US floor\n");
    scanf("%d", &usf);
    euf = usf - 1;
    printf("EU Floor %d\n", euf); */

    /* int i = 0;
    while (i < 5) {
        printf("%i\n", i);
        i++;
    } */

    /* int myInt;
    float myFloat;
    double myDouble;
    char myChar;

    printf("%d\n", sizeof(myInt));
    printf("%f\n", sizeof(myFloat));
    printf("%lf\n", sizeof(myDouble));
    printf("%lu\n", sizeof(myChar)); */

    /* int userScore = 442;
    int maxScore = 500;
    float percentage = (float)userScore / maxScore * 100.0;
    printf("Your score is %.2f\n", percentage); */

    char c = "pizza";
    while ((c = getchar()) != EOF)
        putchar(c);

    return 0;
}