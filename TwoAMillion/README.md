# TwoAMillion

This is a prime number finder that I wrote in Python for the purposes of practicing multithreading optimization and for testing out NUMBA's JIT compiler. It's named TwoAMillion
since it took two seconds to generate the first primes within 1 to 1 millon.

## Speed of TwoAMillion on my AMD Ryzen 5 3500U
From 2 -> Million: Takes 2 seconds
From 2 -> 10 Million: Takes 4 seconds
## Speed of TwoAMillion On my INTEL i3 8350K
From 2 -> Trillion: Takes 700 seconds

The JIT and multiprocessing does take away from it's initial speed as that has to be compiled but I think I did pretty good overall!
