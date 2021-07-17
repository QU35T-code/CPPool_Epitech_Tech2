/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** func_ptr
*/

#ifndef FUNC_PTR_H_
#define FUNC_PTR_H_

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

typedef enum action_e
{
    PRINT_NORMAL,
    PRINT_REVERSE,
    PRINT_UPPER,
    PRINT_42
}   action_t;

void do_action(action_t action, const char *str);
void print_normal(const char *str);
void print_reverse(const char *str);
void print_upper(const char *str);
void print_42(const char *str);
void do_action(action_t action, const char *str);

#endif /* !FUNC_PTR_H_ */