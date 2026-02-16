#include <stdlib.h>

typedef struct
{
    int size;
    float *elements;
} vector;

vector *vector_create(int size)
{
    if (size < 0)
    {
        return NULL;
    }

    vector *v = malloc(sizeof(vector));
    if (v == NULL)
    {
        return NULL;
    }

    v->size = size;
    v->elements = NULL;
    if (size > 0)
    {
        v->elements = malloc(sizeof(float) * size);
        if (v->elements == NULL)
        {
            free(v);
            return NULL;
        }
    }

    return v;
}

void vector_destroy(vector *v)
{
    if (v == NULL)
    {
        return;
    }
    free(v->elements);
    free(v);
}

void vector_set(vector *v, int index, float value)
{
    if (v == NULL || v->elements == NULL)
    {
        return;
    }

    // Explicit lower+upper bound checks prevent negative index memory corruption.
    if (index >= 0 && index < v->size)
    {
        v->elements[index] = value;
    }
}

float vector_get(vector *v, int index)
{
    if (v == NULL || v->elements == NULL)
    {
        return 0;
    }

    if (index >= 0 && index < v->size)
    {
        return v->elements[index];
    }
    return 0;
}

vector *vector_add(vector *v1, vector *v2)
{
    if (v1 == NULL || v2 == NULL || v1->size != v2->size)
    {
        return NULL;
    }
    vector *result = vector_create(v1->size);
    if (result == NULL)
    {
        return NULL;
    }
    for (int i = 0; i < v1->size; ++i)
    {
        result->elements[i] = v1->elements[i] + v2->elements[i];
    }
    return result;
}

vector *vector_sub(vector *v1, vector *v2)
{
    if (v1 == NULL || v2 == NULL || v1->size != v2->size)
    {
        return NULL;
    }
    vector *result = vector_create(v1->size);
    if (result == NULL)
    {
        return NULL;
    }
    for (int i = 0; i < v1->size; ++i)
    {
        result->elements[i] = v1->elements[i] - v2->elements[i];
    }
    return result;
}

float vector_sum(vector *v)
{
    if (v == NULL || v->elements == NULL)
    {
        return 0;
    }
    float sum = 0;
    for (int i = 0; i < v->size; ++i)
    {
        sum += v->elements[i];
    }
    return sum;
}

void vector_fill(vector *v, float value)
{
    if (v == NULL || v->elements == NULL)
    {
        return;
    }
    for (int i = 0; i < v->size; i++)
    {
        v->elements[i] = value;
    }
}

int vector_get_size(vector *v)
{
    if (v == NULL)
    {
        return 0;
    }
    return v->size;
}
