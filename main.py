print("Welcome to the Decision Game")
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
  print("You are old enough!")
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Let's play!")

    left_or_right = input("First choice... Left or Right? ").lower()
    if left_or_right == "left":
      ans = input("You follow the path and reach a lake. Do you swim across or walk around (swim/walk)? ")

      if ans == "walk":
        print("It took you 3 hours to reach the other side of the lake but you made it.")
      elif ans == "swim":
        print("You managed to get across but a snake bit you and you lost 5 health.")
        health -= 5

      ans = input("You look around. There's a house one direction and a mountain corridor the other. Where do you want to go (house/mountain)? ")
      if ans == "house":
        print("You meet the old lady who lives there and she welcomes you inside. However, she has an agressive dog who runs out and attacks you. You lose 5 health.")
        health -= 5

        if health <= 0:
          print("You now have 0 health and you lose the game.")
        else:
          print("The old lady helps you get in contact with people who can get you home. You win!")
      else:
        print("You were stuck in the mountain corridor for days and froze to death.")
      

    else:
      print("You fell in a bottomless pit and died.")


  else:
    print("Bye!")
else:
  print("You are not old enough to play...")