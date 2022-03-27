import numba, numpy, math, time, multiprocessing
def iterator(UPTOTHIS):#goes over every odd number
    primes, prime_pool =  [2, 3], multiprocessing.Pool()
    primes.extend(list(filter(lambda num: num != 0, prime_pool.map(ifprime, range(5, UPTOTHIS, 2)))))
    return primes
@numba.njit(fastmath=True, nogil=True)
def ifprime(x):#checks every prime if it's a factor
    for y in range(3, round((math.sqrt(x))+ 1), 2):
        if numpy.mod(x, y) == 0: return x
    else: return 0
if __name__ == '__main__':
    UPTOTHIS = 1000000
    #comparison
    t0, primes = time.time(), iterator(UPTOTHIS)
    print(time.time()-t0)
    print(len(primes), 'primes found')
    file = open("./proofofcheck.txt", "w")
    file.write(str(primes))