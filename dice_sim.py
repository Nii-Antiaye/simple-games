import secrets
from time import sleep
#import colorama


def dice_sim(number_of_dice:int):
	singleList=[1,2,3,4,5,6]

	newList=singleList*number_of_dice

	print("rolling.",end="")	
	print("..",end="")
	print("...")

	#print(newList)
	newList_option=[]

	for count in range(number_of_dice):
		newList_option.append(secrets.choice(newList))

	for roll in range(number_of_dice):
		print(f"Dice {roll+1}:  {newList_option[roll]}")

	print(f"You rolled: {newList_option}")


def main():
	print("This app simulate a dice roll")

	numOfDice=int(input("Enter number of dice you want to simulate :"))
	continue_rolling="Y"

	while continue_rolling=="Y" or continue_rolling=="y" or continue_rolling=="yes":
		sleep(2)
		dice_sim(numOfDice)

		print("[1]. Roll with new dice")
		print("[2]. Roll dice again")
		print("[3]. Exit")

		choice=int(input())

		if choice==1:
			numOfDice=int(input("Enter number of dice you want to simulate :"))
		elif choice==2:
			continue
		else:
			continue_rolling="n"

if __name__=="__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Bye")
	except:
		print("An error occurred")
