import math
import re
class Projects():
    def __init__(self):
        
        pass 
    def sumMultiples(self,nums,limit):  #PROBLEM 1
        x=[]
        for i in range(limit):
            for j in nums:
                if i%j==0:
                    x.append(i)
                    break
        return sum(x)
    

    def is_prime(self,n):
        #Base conditions
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False

        # since all primes > 3 are of the form 6n ± 1
        # start with f=5 (which is prime)
        # and test f, f+2 for being prime
        # then loop by 6
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0: return False
            if n % (f+2) == 0: return False
            f += 6
        return True


    def getPrimesTill(self,n, returnHighest=False):
        primes = []
        for i in range(n+1):
            if self.is_prime(i):
                primes.append(i)
        if returnHighest:
            return primes[-1]
        return primes
    

    def getHighestPrimeFactor(self,n): #PROBLEM 3
        highest_prime = 1
        for i in self.getPrimesTill(n):
            if n%i == 0:
                highest_prime = i
    
        return highest_prime
    

    def evenFibNumbers(self, limit): #PROBLEM 2
        a=0
        b=2
        sum=a+b
        if limit<2:
            return 0
        while b<=limit:
            c=(4*a)+b
            if c>limit:
                break
            a=b
            b=c
            sum+=c
        return sum
    
    def sumSquareDif(self,n):
        sumOfSquares=(n*(n+1)*(2*n+1))//6
        squareOfSums=((n*(n+1))//2)**2
        return (abs(squareOfSums-sumOfSquares))
    
    def getnthPrime(self, n):
        x=0
        prime=0
        while True:
            if self.is_prime(prime):
                x+=1
            if n==x:
                break
            prime+=1
        return prime        
    
    def prodLargestNumberIn(self, sring, size):
        Max=int(size*"9")
        Min=int(size*"1")
        for i in range(Max,Min,-1):
            if str(i) in sring:
                return self.prodOfDigits(str(i))
    
    def prodOfDigits(self,n):
        x=1
        for i in n:
            x=x*int(i)

        return x
    def isPerfectSquare(self,n):
        return (math.sqrt(n)+0.5)**2==n
    def isPythagoreanTriple(self,n):
       
        if n[0]**2 + n[1]**2 == n[2]**2:
            return n
        else:
            return [0,0,0]
    def getPythagoreanTriple(self,n):
        m=math.sqrt(n+1)
        a=n
        b=int(2*m) 
        c=int((m**2)+1)
        return self.isPythagoreanTriple([a,b,c])
    
    def abc(self,limit):
        l=[]
        for i in range(limit):
            l= self.getPythagoreanTriple(i)
            if l[0]+l[1]+l[2] == limit:
                return l
            
            #if self.isPythagoreanTriple(trps):
                #return trps[0]*trps[1]*trps[2] 
'''
import projectEuler as pe
import var
sol=pe.Projects()
sol.abc(11)
'''