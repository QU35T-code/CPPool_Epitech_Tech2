/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** pyramid
*/

#include "pyramid.h"

int pyramid_path(int size, const int **map)
{
    int total = 0;
    int y = 0;
    for (int i = 0; i < size - 1; i++)
    {
        int actual = map[i][y];
        int voisin1 = map[i + 1][y];
        int voisin2 = map[i + 1][y + 1];
        if (voisin1 < voisin2) {
            total = total + voisin1;
        } else {
            total = total + voisin2;
            y = y + 1;
        }
    }
    return (total);
}