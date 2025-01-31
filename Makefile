SRC = $(wildcard PrivCheck/*.c)
OBJS = $(patsubst PrivCheck/%.c, %.o, $(SRC))
CC_x64 := x86_64-w64-mingw32-gcc
STRIP_x64 := x86_64-w64-mingw32-strip
CFLAGS := -masm=intel

all: $(OBJS)

%.o: PrivCheck/%.c
	$(CC_x64) $(CFLAGS) -o ./output/$*.x64.o -c $<
	$(STRIP_x64) --strip-unneeded ./output/$*.x64.o

vulnerabledrivers.o: PrivCheck/vulnerabledrivers.c
    # Download the latest vulnerable driver list and output the parsed list into the "includes" folder
	python3 includes/download_vulnerable_driver_list.py includes
	$(CC_x64) $(CFLAGS) -o ./output/vulnerabledrivers.x64.o -c PrivCheck/vulnerabledrivers.c
	$(STRIP_x64) --strip-unneeded ./output/vulnerabledrivers.x64.o

clean:
	rm ./output/*.o
