#https://stackoverflow.com/questions/36263254/how-to-generate-prime-palindromes-in-python-3
#Palindrome test
def palindrome(num):
    return str(num) == str(num)[::-1]

#Prime Test
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

#Get user input
N = 1
M = 20000000

data=[93766,9916239]

for x in range(N, M):

    #Check for palindrome and prime number
    if palindrome(x) and is_prime(x):
        k = 0
        while k < len(data):
            if (x ^ data[k]) < 256:
                print(str(k)  + ': ' + str(data[k]) + " ^ " + str(x) + " > " + str(x ^ data[k]) + " > " + chr((x ^ data[k])))
            k +=1
