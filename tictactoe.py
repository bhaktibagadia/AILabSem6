def printdata(matr):
    for row in matr:
        print(" ---" * 3)
        print("|", end="")
        for cell in row:
            print(f"{cell} |", end="")
        print()
    print(" ---" * 3)


def tictactoe(matr):
  compposition=[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
  count=0

  while(1):
      printdata(matr)
      if count==8:
        print("Game Draws")
        return

      print("User Plays")
      userposition=input()
      userposition=tuple(map(int, userposition.split(',')))

      if userposition in compposition:
        matr[userposition[0]][userposition[1]]="x"
        compposition.remove(userposition)
        count+=1
        printdata(matr)

      for i in range(3):
            if all(matr[i][j]=="x" for j in range(3)) or all(matr[j][i]=="x" for j in range(3)):
                printdata(matr)
                print("User wins")
                return

            if all(matr[i][i]=="x" for i in range(3)) or all(matr[i][2 - i]=="x" for i in range(3)):
                printdata(matr)
                print("User wins")
                return

      print("Computer Plays")
      newposition=random.choice(compposition)
      if newposition in compposition:
        matr[newposition[0]][newposition[1]]="o"
        compposition.remove(newposition)
        count+=1

      for i in range(3):
            if all(matr[i][j]=="o" for j in range(3)) or all(matr[j][i]=="o" for j in range(3)):
                printdata(matr)
                print("Computer wins")
                return

            if all(matr[i][i]=="o" for i in range(3)) or all(matr[i][2 - i]=="o" for i in range(3)):
                printdata(matr)
                print("Computer wins")
                return


import random

matr = [['   |' for _ in range(3)] for _ in range(3)]
tictactoe(matr)
printdata(matr)
