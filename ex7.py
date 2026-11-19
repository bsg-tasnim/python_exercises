#Write a program to find all prime numbers up to 20, 
# but only print every second (alternate) prime number found.

prime=[]
for i in range(2,21):
    for j in range(2, int(i*0.5)+1):
        if i%j==0:
            break
    else:
        prime.append(i)

print(prime)
print("Alternate Primes: ", prime[::2])




