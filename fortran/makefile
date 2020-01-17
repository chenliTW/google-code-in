CC=gfortran
CFLAGS=-llapack -lblas

main:
	$(CC) saxpy.f90 -o saxpy.o $(CFLAGS)
	$(CC) ddot.f90 -o ddot.o $(CFLAGS)
	$(CC) dgemv.f90 -o dgemv.o $(CFLAGS)
	$(CC) dgemm.f90 -o dgemm.o $(CFLAGS)

.PHONY: clean
clean:
	-rm *.o
