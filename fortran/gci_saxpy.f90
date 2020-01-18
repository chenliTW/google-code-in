        PROGRAM GCI_SAXPY
        
        integer::N,INCX,INCY
        real::SA
        real, DIMENSION(9)::SX,SY
        
        N = 9
        
        SA = 2

        SX = reshape((/ 1, 4, 9, 16, 25, 36, 49, 64, 81 /), shape(SX))
        SY = reshape((/ 1, 1, 2, 3, 5, 8, 13, 21, 33 /), shape(SY))
        
        INCX = 1
        INCY = 1

        call saxpy(N,SA,SX,INCX,SY,INCY)

        write(*,*) SY

        stop
        end