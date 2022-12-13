import random
A=int(input())
B=int(input())
d=random.randint(A,B)
print("randomaly picked number is %d"%(d))
if d%2==0:
    print("%d is an even number"%(d))
if d%2!=0:
    print("%d is an odd number"%(d))
if d>=0:
    print("%d is a positive number"%(d))
if d<0:
    print("%d is negative number"%(d))
if d==1:
   print("%d is neither prime NOR composite  number"%(d))
if d > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(d/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (d % i) == 0:
			print(d, "is composite number")
			break
	else:
		print(d, "is a prime number")