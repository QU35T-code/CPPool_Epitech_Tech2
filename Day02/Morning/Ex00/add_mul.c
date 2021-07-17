/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** add_mul
*/

#include "add_mul.h"

void add_mul_4param(int first, int second, int *sum, int *product)
{
    *sum = first + second;
    *product = first * second;
}

void add_mul_2param(int *first, int *second)
{
    *first = *first + *second;
    *second = *second * (*first - *second);
}