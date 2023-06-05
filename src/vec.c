#include <stdlib.h>

typedef struct
{
    int size;
    float *elements;
} vector;

vector *vector_create(int size)
{
    vector *v = malloc(sizeof(vector));
    v->size = size;
    v->elements = malloc(sizeof(float) * size);
    return v;
}

void vector_destroy(vector *v)
{
    free(v->elements);
    free(v);
}

void vector_set(vector *v, int index, float value)
{
    if (index < v->size)
    {
        v->elements[index] = value;
    }
}

float vector_get(vector *v, int index)
{
    if (index < v->size)
    {
        return v->elements[index];
    }
    return 0;
}

vector *vector_add(vector *v1, vector *v2)
{
    if (v1->size != v2->size)
    {
        return NULL;
    }
    vector *result = vector_create(v1->size);
    for (int i = 0; i < v1->size; ++i)
    {
        result->elements[i] = v1->elements[i] + v2->elements[i];
    }
    return result;
}

vector *vector_sub(vector *v1, vector *v2)
{
    if (v1->size != v2->size)
    {
        return NULL;
    }
    vector *result = vector_create(v1->size);
    for (int i = 0; i < v1->size; ++i)
    {
        result->elements[i] = v1->elements[i] - v2->elements[i];
    }
    return result;
}

float vector_sum(vector *v)
{
    float sum = 0;
    for (int i = 0; i < v->size; ++i)
    {
        sum += v->elements[i];
    }
    return sum;
}

void vector_fill(vector *v, float value)
{
    for (int i = 0; i < v->size; i++)
    {
        v->elements[i] = value;
    }
}

int vector_get_size(vector *v)
{
    return v->size;
}