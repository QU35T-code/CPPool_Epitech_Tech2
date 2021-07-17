/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** func_ptr
*/

#include "func_ptr.h"

void print_normal(const char *str)
{
    printf("%s\n", str);
}

void print_reverse(const char *str)
{
    char *my_str = malloc(sizeof(char) * strlen(str));
    int size = strlen(str);
    char temp_var;
    strcpy(my_str, str);
    for (int i = 0 ; i <= size - 2; i++) {
        size--;
        temp_var = my_str[i];
        my_str[i] = my_str[size];
        my_str[size] = temp_var;
    }
    printf("%s\n", my_str);
}

void print_upper(const char *str)
{
    char *chr = str;
    chr = malloc(sizeof(char) * strlen(str));
    strcpy(chr, str);
    int i = 0;
    char final;
    while (chr[i]) {
        final = chr[i];
        printf("%c", toupper(final));
        i++;
    }
    printf("\n");
}

void print_42(const char *str)
{
    printf("%d\n", 42);
}

void do_action(action_t action, const char *str)
{
    if (action == PRINT_NORMAL) {
        print_normal(str);
    }
    if (action == PRINT_REVERSE) {
        print_reverse(str);
    }
    if (action == PRINT_UPPER) {
        print_upper(str);
    }
    if (action == PRINT_42) {
        print_42(str);
    }
}