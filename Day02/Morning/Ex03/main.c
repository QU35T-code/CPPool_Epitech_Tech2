/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** main
*/

#include "func_ptr.h"

int main(void)
{
    const char *str = "I'm using function pointers!";
    do_action(PRINT_NORMAL, str);
    do_action(PRINT_REVERSE, str);
    do_action(PRINT_UPPER, str);
    do_action(PRINT_42, str);
    return (0);
}