/*
** EPITECH PROJECT, 2021
** CPPool_Epitech_Tech2
** File description:
** mem_ptr
*/

#ifndef MEM_PTR_H_
#define MEM_PTR_H_

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct str_op_s
{
    const char *str1;
    const char *str2;
    char *res;
} str_op_t;

void add_str(const char *str1, const char *str2, char **res);
void add_str_struct(str_op_t *str_op);

#endif /* !MEM_PTR_H_ */