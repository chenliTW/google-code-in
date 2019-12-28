![](https://github.com/chenliTW/google-code-in/raw/master/time-bound-computation/result.png)

blue=numpy
orange=@numba.jit
red=hardcode

numpy.dot is faster because it use optimized compiled code, and it is way more faster than python interpreter.

@numba.jit translate code into fast machine code,but my code isn't optimized,so the speed is a little slower that numpy,but much faster than the hardcode one ;)
