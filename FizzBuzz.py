#create loop
for x in range(1,101):
  #compare if divisible by 3&5
  if x % 3 == 0 and x % 5 ==0:
    print("FizzBuzz")
    continue
  #compare if divisible by 3
  elif x % 3 == 0:
    print("Fizz")
    continue
  #compare if divisible by 5
  elif x % 5 == 0:
    print("Buzz")
    continue
  #prints all numbers not divisible
  else:
    print(x)
