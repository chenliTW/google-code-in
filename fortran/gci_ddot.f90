        PROGRAM GCI_DDOT
        
        integer::N,INCX,INCY
        DOUBLE PRECISION, DIMENSION(9)::DX,DY

        N = 9

        DX = reshape((/ 1, 4, 9, 16, 25, 36, 49, 64, 81 /), shape(DX))
        DY = reshape((/ 1, 1, 2, 3, 5, 8, 13, 21, 33 /), shape(DY))

        INCX = 1
        INCY = 1

        call ddot(N,DX,INCX,DY,INCY)

        write(*,*) dtemp

        stop
        end
        