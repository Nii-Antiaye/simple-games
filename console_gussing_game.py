import random
import colorama
from colorama import Fore

colorama.init(autoreset=True)

print(f"{Fore.YELLOW}Welcome to the hangman game skeleton")

print(f"{Fore.YELLOW}A word has been selected for you so it's time to guess")

def rand():
	wordS=[("Cat","Is a lazy animal and are like females"),
			("Dog","Is a good and loyal animal like males"),
			("Bat","Come out at night and believed to be blind"),
			("Rat","Known for stealing food stuff and chewing money"),
			("lion","Known as the king of the jungle"),
			("Eagle","Known as the king of the sky and almost always seen catching a snake"),
			("Rabbit","used for the famous playboy symbol")
			]

	selected_word=wordS[random.randint(0,len(wordS)-1)]
	#print(selected_word)
	return selected_word

def guessing():
	play_on=True
	while play_on:
		selected_word=rand()
		print(f"{Fore.GREEN}[CLUE]{selected_word[1]}")
		guess_word=[i.lower() for i in selected_word[0]]
		
		number_tries=3
		while number_tries>0:
			print(f"{Fore.GREEN}Enter your guess:")
			guessed_letter=input().lower()
			if guessed_letter in guess_word:
				print(f"{Fore.GREEN}Yes,{guessed_letter} is in the word :)")
				print("")
				guess_word.remove(guessed_letter)
				number_tries=3
				if (guess_word==[]):
					print(f"{Fore.BLUE}You won")
					break
				else:
					continue
			else:
				print(f"{Fore.GREEN}Sorry, {guessed_letter} is not in the word")
				print("")
				number_tries-=1
		else:
			print(f"The word was {selected_word[0]}")
			print(f"{Fore.LIGHTGREEN_EX}Sorry, You are out of tries")



		print(f"{Fore.LIGHTGREEN_EX}Would you like to try another word?")
		play_on=input().lower()

		if play_on == "yes" or play_on == "y":
			play_on=True
		else:
			play_on=False



guessing()
