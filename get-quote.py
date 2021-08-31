import random
last = 13
rnd = random.randint(0, last)
def main():
<<<<<<< HEAD
  #print("Keep it logically awesome.")
=======
  print("Keep it logically awesome.")
>>>>>>> a3ab345b7c667bc50b423cbf82778db7ea493f05

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[rnd])
  
if __name__== "__main__":
    main()