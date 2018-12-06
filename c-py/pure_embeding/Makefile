INCLUDE_PATH = -I/usr/include/python3.6
LIB_PATH = -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu
LIBS := -lpython3.6
INC_REFERENCE = -I/usr/include/python3.6m -I/usr/include/python3.6m  -Wno-unused-result -Wsign-compare -g -fdebug-prefix-map=/build/python3.6-MtRqCA/python3.6-3.6.6=. -specs=/usr/share/dpkg/no-pie-compile.specs -fstack-protector -Wformat -Werror=format-security  -DNDEBUG -g -fwrapv -O3 -Wall -fPIC
LIB_REFERENCE = -L/usr/lib/python3.6/config-3.6m-x86_64-linux-gnu -L/usr/lib -lpython3.6m -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions
SRC = main.cpp
OBJECT = main
all:
	gcc -o ${OBJECT} ${SRC} ${INC_REFERENCE} ${LIB_REFERENCE} 
clean:
	rm ${OBJECT}
