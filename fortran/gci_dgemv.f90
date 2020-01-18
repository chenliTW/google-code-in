        PROGRAM GCI_DGEMV
        
        character*1 TRANS

        integer::M,N,LDA,INCX,INCY

        DOUBLE PRECISION::ALPHA,BETA

        DOUBLE PRECISION, DIMENSION(4, 3)::A
        DOUBLE PRECISION, DIMENSION(2)::X
        DOUBLE PRECISION, DIMENSION(3)::Y

        TRANS = 't'

        M = 2
        N = 3
        
        LDA = 4

        ALPHA = 2
        BETA = 3

        INCX = 1
        INCY = 1

        A = reshape((/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 /), shape(A))
        X = reshape((/ 1, 2 /), shape(X))
        Y = reshape((/ 1, 2, 3 /), shape(Y))

        call dgemv(TRANS,M,N,ALPHA,A,LDA,X,INCX,BETA,Y,INCY) 	

        write(*,*) Y

        stop
        end