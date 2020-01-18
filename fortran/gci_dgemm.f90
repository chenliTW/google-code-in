        PROGRAM GCI_DGEMM
        
        character*1 TRANSA,TRANSB

        integer::M,N,K,LDA,LDB,LDC

        DOUBLE PRECISION::ALPHA,BETA

        DOUBLE PRECISION, DIMENSION(4, 2)::A
        DOUBLE PRECISION, DIMENSION(3, 4)::B
        DOUBLE PRECISION, DIMENSION(2, 3)::C

        TRANSA = 't'
        TRANSB = 't'

        M = 2
        N = 3
        K = 4
        
        LDA = 4
        LDB = 3
        LDC = 2

        ALPHA = 2
        BETA = 3

        A = reshape((/ 1, 2, 3, 4, 5, 6, 7, 8 /), shape(A))
        B = reshape((/ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12/), shape(B))
        C = reshape((/ 1, 2, 3, 4, 5, 6 /), shape(C))

        call dgemm(TRANSA,TRANSB,M,N,K,ALPHA,A,LDA,B,LDB,BETA,C,LDC)

        write(*,*) C
        
        stop
        end