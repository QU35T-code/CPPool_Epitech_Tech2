/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** main
*/

#include <stdlib.h>
#include "menger.h"

int main(int ac, char const *av[])
{
    if (ac != 3)
        return (84);
    else
        menger(atoi(av[1]), atoi(av[2]), 0, 0);
    return (0);
}
