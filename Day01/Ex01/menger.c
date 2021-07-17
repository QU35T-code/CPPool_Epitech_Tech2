/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** menger
*/

#include "menger.h"

int menger(int size, int lv, int x, int y)
{
    size = size / 3;
    int x_global = size + x;
    int y_global = size + y;
    printf("%03d %03d %03d\n", size, x_global, y_global);
    if (lv > 1) {
        lv = lv - 1;
        menger(size, lv, x, y);
        menger(size, lv, x, y + size);
        menger(size, lv, x, y + 2 * size);
        menger(size, lv, x + size, y);
        menger(size, lv, x + size, y + 2 * size);
        menger(size, lv, x + 2 * size, y);
        menger(size, lv, x + 2 * size, y + size);
        menger(size, lv, x + 2 * size, y + 2 * size);
    }
    return (0);
}