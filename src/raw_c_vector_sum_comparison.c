#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "vec.h"

#define ARRAY_SIZE 1000000000 // Adjust the array size as needed

void addArrays(const float *array1, const float *array2, float *result, int size)
{
    for (int i = 0; i < size; i++)
    {
        result[i] = array1[i] + array2[i];
    }
}

int main()
{
    float *array1 = (float *)malloc(ARRAY_SIZE * sizeof(float));
    float *array2 = (float *)malloc(ARRAY_SIZE * sizeof(float));

    // Initialize arrays with some values
    for (int i = 0; i < ARRAY_SIZE; i++)
    {
        array1[i] = i * 1.5f;
        array2[i] = i * 2.0f;
    }

    float *result = (float *)malloc(ARRAY_SIZE * sizeof(float));

    // Start measuring time
    clock_t start = clock();

    // Add arrays together
    addArrays(array1, array2, result, ARRAY_SIZE);

    // Stop measuring time
    clock_t end = clock();

    // Calculate the time taken in seconds
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    // print the size of the arrays
    printf("Array size: %d\n", ARRAY_SIZE);

    // Print the first index of the result
    printf("Result: %.2f\n", result[0]);

    // Print the time taken
    printf("Time taken: %.9f seconds\n", time_taken);

    // Free memory
    free(array1);
    free(array2);
    free(result);

    return 0;
}
