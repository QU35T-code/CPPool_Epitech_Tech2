##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Makefile
##

CCP		=	gcc

CCFLAGS	+=	-Wextra -Werror -Wall

NAME_BINARY = bitmap

INCLUDES	= -I./

SRCS	=	main.c \
			bitmap_header.c \

OBJ_SRCS	=	$(SRCS:.c=.o)

all: $(NAME_BINARY)

$(NAME_BINARY): $(OBJ_SRCS)
			$(CCP) $(OBJ_SRCS) -o $(NAME_BINARY) $(CCFLAGS) $(INCLUDES)

clean:
	@rm -f $(OBJ_SRCS)

fclean: 	clean
	@rm -f $(NAME_BINARY)
	@rm -f 32px.bmp

re: 	fclean all

.PHONY: clean fclean re