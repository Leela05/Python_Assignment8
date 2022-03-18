# Write a Python class to implement pow(x, n)

class Sample:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x, -n)
        val = self.pow(x, n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(Sample().pow(2, 4));
print(Sample().pow(4, 5));
print(Sample().pow(5, 0));
