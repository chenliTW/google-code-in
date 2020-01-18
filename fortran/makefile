CC=gfortran
CFLAGS=-llapack -lblas

main:
	$(CC) gci_saxpy.f90 -o gci_saxpy.o $(CFLAGS)
	$(CC) gci_ddot.f90 -o gci_ddot.o $(CFLAGS)
	$(CC) gci_dgemv.f90 -o gci_dgemv.o $(CFLAGS)
	$(CC) gci_dgemm.f90 -o gci_dgemm.o $(CFLAGS)

.PHONY: clean
clean:
	-rm *.o
