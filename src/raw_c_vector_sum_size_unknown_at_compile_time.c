#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "vec.h"

void addArrays(const float *array1, const float *array2, float *result, int size)
{
    for (int i = 0; i < size; i++)
    {
        result[i] = array1[i] + array2[i];
    }
}

int main()
{
    int arraySize;

    printf("Enter the size of the arrays: ");
    scanf("%d", &arraySize);

    if (arraySize <= 0)
    {
        printf("Invalid array size. Exiting program.\n");
        return 1;
    }

    float *array1 = (float *)malloc(arraySize * sizeof(float));
    float *array2 = (float *)malloc(arraySize * sizeof(float));

    // Initialize arrays with some values
    for (int i = 0; i < arraySize; i++)
    {
        array1[i] = i * 1.5f;
        array2[i] = i * 2.0f;
    }

    float *result = (float *)malloc(arraySize * sizeof(float));

    // Start measuring time
    clock_t start = clock();

    // Add arrays together
    addArrays(array1, array2, result, arraySize);

    // Stop measuring time
    clock_t end = clock();

    // Calculate the time taken in seconds
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    // print the size of the arrays
    printf("Array size: %d\n", arraySize);

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
