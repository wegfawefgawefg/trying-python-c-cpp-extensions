#ifndef VECTOR_H
#define VECTOR_H

typedef struct
{
    int size;
    float *elements;
} vector;

vector *vector_create(int size);
void vector_destroy(vector *v);
void vector_set(vector *v, int index, float value);
float vector_get(vector *v, int index);
vector *vector_add(vector *v1, vector *v2);
vector *vector_sub(vector *v1, vector *v2);
float vector_sum(vector *v);

#endif // VECTOR_H
