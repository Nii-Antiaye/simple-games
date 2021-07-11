import secrets
import colorama
from colorama import Fore,Back,Style
from time import sleep

try:
	colorama.init(autoreset=True)

	print(f"{Fore.BLACK}{Back.WHITE}You are playing rock, papar, scissors ")


	option=["rock", "paper", "scissors"]
	player_score=0
	cpu_score=0

	playon=True
	gameto=int(input(f"[+]How many game (game to ?) ?: "))


	while playon:
		
		while gameto>0:
			print(f"{Fore.BLUE}\n[1] Rock ")
			print(f"{Fore.BLUE}[2] Paper ")
			print(f"{Fore.BLUE}[3] Scissor \n")
			play=int(input(f"Your choice (enter number):"))

			cpu_player = secrets.choice(option)

			while play<0 or play>3:
				print(f"{Fore.RED}There is an error, the range is 1 to 3")
				print(f"{Fore.BLUE}\n[1] Rock ")
				print(f"{Fore.BLUE}[2] Paper ")
				print(f"{Fore.BLUE}[3] Scissor \n")
				play=int(input(f"Your choice (enter number):"))


			if play==1:
				if cpu_player==option[0]:
					print(f"{Fore.GREEN}{option[play-1]} and {cpu_player} are the same")
				elif cpu_player==option[1]:
					print(f"{Fore.GREEN}{cpu_player} beats {option[play-1]}, cpu wins")
					cpu_score+=1
					gameto-=1
				else:
					print(f"{Fore.GREEN}{option[play-1]} beats {cpu_player}, you win")
					player_score+=1
					gameto-=1
			elif play==2:
				if cpu_player==option[0]:
					print(f"{Fore.GREEN}{option[play-1]} beats {cpu_player}, you win")
					player_score+=1
					gameto-=1
				elif cpu_player==option[1]:
					print(f"{Fore.GREEN}{option[play-1]} and {cpu_player} are the same")
				else:
					print(f"{Fore.GREEN}{cpu_player} beats {option[play-1]}, cpu win")
					cpu_score+=1
					gameto-=1
			elif play==3:
				if cpu_player==option[0]:
					print(f"{Fore.GREEN}{cpu_player} beats {option[play-1]}, cpu win")
					cpu_score+=1
					gameto-=1
				elif cpu_player==option[1]:
					print(f"{Fore.GREEN}{option[play-1]} beats {cpu_player}, you win")
					player_score+=1
					gameto-=1
				else:
					print(f"{Fore.GREEN}{option[play-1]} and {cpu_player} are the same")	


		print(f"{Fore.CYAN}{Style.BRIGHT}Play:{player_score}  CPU:{cpu_score}")
		
		
		tempStorage = input("Would you like to play another game? (Y/N)")

		if tempStorage=="Y" or tempStorage=="Yes" or tempStorage=="yes" or tempStorage=="y":
			gameto=int(input(f"[+]How many game (game to ?) ?: "))
			player_score=0
			cpu_score=0
		else:
			print(f"{Fore.BLACK}{Back.GREEN}{Style.BRIGHT}Bye")
			playon=False
except KeyboardInterrupt:
	pass
except Exception as error:
	print(f"{Fore.RED}{error}")


