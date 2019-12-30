#include <stdio.h>
#include <stdlib.h>

long w_subtract(long x)
{
    long ret;
    if (x % 10 == 0)
        ret = (x / 10);
    else
        ret = --x;
    return ret;
}

int main(int argc, char **argv)
{
    printf("%d\n", argc);

    long x = atol(argv[1]);
    long n = atol(argv[2]);
    long i;

    for (i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }

    for (i = 0; i < n; i++)
    {
        x = w_subtract(x);
    }

    printf("%d", x);

    return 0;
}