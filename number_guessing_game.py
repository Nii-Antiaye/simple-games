import secrets
import colorama
from colorama import Fore, Back

# :sad but relieved face:
# :pile of poo:
# :worried face:
# :frowning face:
# :star-struck:
# :grinning face:

colorama.init(autoreset=True)

try:
	print(f"\n\t{Fore.BLACK}{Back.WHITE}This is a guessing game ")

	state="yes"

	while state=="yes" or state=="y" or state=="YES" or state=="Yes":
		numOfTries=3
		print(f"{Fore.LIGHTWHITE_EX}A number is being selected for you")

		toGuess=secrets.randbelow(100)

		print(toGuess)
		print(f"{Fore.LIGHTWHITE_EX}The number selected is between {toGuess-secrets.randbelow(10)} and {toGuess+secrets.randbelow(10)}")

		while numOfTries>0:
			print("")
			userGuess=int(input("Guess the number :"))
			print("")

			if toGuess==userGuess:
				print(f"{Fore.LIGHTGREEN_EX}Your guess is Right!!")
				print(f"{Fore.LIGHTGREEN_EX}You win")
				break
			else:
				if toGuess>userGuess:
					print(f"{Fore.LIGHTYELLOW_EX}Your guess is less than the number !!")
					numOfTries-=1
					print(f"{Fore.LIGHTYELLOW_EX}You have {numOfTries} of tries left")
				elif toGuess<userGuess:
					print(f"{Fore.LIGHTYELLOW_EX}Your guess is more than the number !!")
					numOfTries-=1
					print(f"{Fore.LIGHTYELLOW_EX}You have {numOfTries} of tries left")
		else:
			print(f"{Fore.LIGHTRED_EX}Sorry you lost, you had {numOfTries} number of tries left")
			print(f"{Fore.LIGHTRED_EX}The number was {toGuess}")

		print("")
		state=input("Do you want to play again ? ")
		print("")
except KeyboardInterrupt:
	print(f"Thanks Bye")
except Exception as e:
	print(f"An error occurred: {e}")