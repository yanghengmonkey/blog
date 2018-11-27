INCLUDE_PATH = -I/usr/include/python3.6
LIB_PATH = -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu
LIBS := -lpython3.6
SRC = main.cpp
OBJECT = main
all:
	g++ -o ${OBJECT} ${SRC} ${INCLUDE_PATH} ${LIB_PATH} ${LIBS}
clean:
	rm ${OBJECT}
