/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** tab_to_2dtab
*/

#include "tab_to_2dtab.h"

void tab_to_2dtab(const int *tab, int length, int width, int ***res)
{
    *res = malloc(sizeof(int *) * length + 2);
    for (int i = 0; i < length; i++) {
        (*res)[i] = malloc(sizeof(int) * length * width);
        for (int j = 0; j < width; j++) {
            int sum = i * width + j;
            (*res)[i][j] = tab[sum];
        }
    }
}