##
## EPITECH PROJECT, 2021
## CPPool_Epitech_Tech2
## File description:
## Makefile
##

all:
		make -C Day01/

clean:
		make clean -C Day01/


fclean:
		make fclean -C Day01/

re:		fclean	all

.PHONY:		all clean fclean re