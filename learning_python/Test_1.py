import random
secret = random.randint(1,10)
guess = 0
tries = 0
while guess != secret and tries < 6:
    #guess = int(input("猜数字！"))
    guess = 5
    if guess < secret:
        print ("数字太小!")
    elif guess > secret:
      print ("数字太大!")
    tries = tries + 1
if guess == secret:
    print ("OK!")
else:
    print (secret)