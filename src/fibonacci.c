#include <stdint.h>

int64_t fibonacci(int n)
{
    int64_t a = 0, b = 1;
    for (int i = 0; i < n; ++i)
    {
        int64_t temp = a;
        a = b;
        b = temp + b;
    }
    return a;
}
