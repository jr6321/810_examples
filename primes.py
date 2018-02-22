""" Calculate prime numbers using a generator """

import unittest
import time

def next_prime():
    """ generate prime numbers but store the primes you've generated so far and compare
        new potential primes only against the list of generated primes.
    """
    primes = [2]

    yield 2  # 2 is the first prime number by definition

    cur = 3  # cur is the next number to be checked

    while True:   # potentially generate an infinite number of primes
        for p in primes:
            print('checking {} % {}'.format(cur, p))
            if cur % p == 0:
                break
        else:
            # exhausted all of the primes and found another prime number
            primes.append(cur)
            yield cur
            
        cur += 1


def next_prime_naive():
    """ generate prime numbers by dividing by 2 up to the number """
    cur = 2
    while True:   # potentially generate an infinite number of primes
        for i in range(2, cur):
            print('checking {} % {}'.format(cur, i))
            if cur % i == 0:
                break  # cur is divisible by i so look at next value of cur
        else:
            # didn't divide evenly by any number so found another prime number
            yield cur

        cur += 1

def nprimes_naive(n):
    """ return a list with the first n prime numbers """
    gen = next_prime_naive()
    return [next(gen) for i in range(n)]

def prime_naive_comparisons(n):
    """ generate prime numbers by comparing up to cur // 2 + 1 """
    comparisons = 0
    cur = 2
    for m in range(n):
        for i in range(2, cur):
            #print("{}: comparing {} and {}".format(comparisons, cur, i))
            comparisons += 1
            if cur % i == 0:
                break  # cur is divisible by i so look at next value of cur
    
        # didn't divide evenly by any number so found another prime number
        cur += 1

    return comparisons

def prime_comparisons(n):
    """ generate prime numbers by comparing up to cur // 2 + 1 """
    comparisons = 0
    primes = [2]
    cur = 3  # cur is the next number to be checked

    for i in range(n):
        for p in primes:
            comparisons += 1
            if cur % p == 0:
                break
        else:
            # exhausted all of the primes and found another prime number
            primes.append(cur)
            
        cur += 1

    return comparisons

def is_prime(n):
    for p in next_prime():
        if p == n:
            return True
        elif p > n:
            return False


def nth_prime(n):
    """ return the nth prime number """
    for i, p in enumerate(next_prime()):
        if i + 1 >= n:
            return p

def nth_prime2(n):
    """ return the nth prime number using next_prime2(), not next_prime() """
    for i, p in enumerate(next_prime_naive()):
        if i + 1 >= n:
            return p
 
class PrimeTest(unittest.TestCase):
    def test(self):
        self.assertEqual(nprimes_naive(5), [2, 3, 5, 7, 11])
        self.assertEqual(nth_prime(1), 2)
        self.assertEqual(nth_prime(2), 3)
        self.assertEqual(nth_prime(5), 11)

        self.assertEqual(nth_prime2(1), 2)
        self.assertEqual(nth_prime2(2), 3)
        self.assertEqual(nth_prime2(5), 11)


def time_nprimes_naive(n):
    gen = next_prime_naive()
    start = time.time()
    for i in range(n):
        next(gen)
    end = time.time()
    print("{}: {:.5f}".format(n, end - start))


def time_nprimes(n):
    comparisons = prime_comparisons(n)
    gen = next_prime()
    start = time.time()
    for i in range(n):
        next(gen)
    end = time.time()
    print("better: {}: {} comparisons {:.5f} seconds".format(n, comparisons, end - start))

def timeit(func, *args, **kwargs):
    print("start timing", args, kwargs)
    start = time.time()
    func(args, kwargs)
    end = time.time()
    return end - start


def compare_times(n):
    start1 = time.time()
    nth_prime(n)
    end1 = time.time()

    start2 = time.time()
    nth_prime2(n)
    end2 = time.time()

    diff1 = end1 - start1
    diff2 = end2 - start2

    if diff1 < diff2:
        print("nth_prime({0}) beat nth_prime2({0}) by {1:.5} seconds".format(n, diff1))
    else:
        print("nth_prime2({0}) beat nth_prime({0}) by {1:.5} seconds".format(n, diff2))



if __name__ == "__main__":
    #unittest.main()
    print("finding 10 primes requires {} comparisons".format(prime_naive_comparisons(11)))
    #print("finding 100 primes requires {} comparisons".format(prime_naive_comparisons(100)))
    time_nprimes_naive(100)
    print("finding 200 primes requires {} comparisons".format(prime_naive_comparisons(200)))
    time_nprimes_naive(200)
    print("finding 400 primes requires {} comparisons".format(prime_naive_comparisons(400)))
    time_nprimes_naive(400)
    print("finding 800 primes requires {} comparisons".format(prime_naive_comparisons(800)))
    #time_nprimes_naive(800)
    time_nprimes(100)
    time_nprimes(200)
    time_nprimes(400)
    time_nprimes(800)
    #print(nth_prime(1000))
    #print(nth_prime(1500))
    #print(nprimes(1000))
    """
    compare_times(10)
    compare_times(1000)
    compare_times(2500)
    """