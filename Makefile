##
## EPITECH PROJECT, 2021
## CPPool_Epitech_Tech2
## File description:
## Makefile
##

all:
		make -C Day01/
		make -C Day02/

clean:
		make clean -C Day01/
		make clean -C Day02/

fclean:
		make fclean -C Day01/
		make fclean -C Day02/

re:		fclean	all

.PHONY:		all clean fclean re