##
## EPITECH PROJECT, 2021
## B-SYN-400-TLS-4-1-autoCompletion-alexis.martin
## File description:
## Makefile
##

all:
		@cp autoCompletion.py autoCompletion
		@chmod 777 autoCompletion

clean:
		@rm -f rm autoCompletion
		@rm -f ret.txt
		@rm -f errors.txt

fclean: clean
		@rm -f rm autoCompletion

run_tests: fclean all
	./tests/autoCompletion_tests

re:		fclean	all

.PHONY:		all clean fclean re