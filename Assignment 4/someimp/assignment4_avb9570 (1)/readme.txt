Assignment 4
Name		:	Aditya Bharaswadkar
UTA		:	1001529570
Language	:	Python
Code Structure	:	file1:maxconnect4.py
			import statements
			initialize board from file
			utilityfn()-compares values with utility table
			checkmove()-checks if move is valid
			playturn()-plays move and sets next player turn
			minimax()-minmax algorithm with alpha-beta pruning
			read arguments and initialize game state
			set game move and select first player
			print score
			file2:MaxConnect4Game.py
			draw table function and write to files
			calculate score functions
			check if player move is valid and return invalid if column full
Executing Program:	
			onemove-mode:
			python maxconnect4.py one-move [input_file.txt] [output_file.txt] [depth]
			example:
			python maxconnect4.py one-move input1.txt green_next.txt 5

			interactive-mode:
			python maxconnect4.py interactive [input_file.txt] [human-next/computer-next] [depth]
			example:
			python maxconnect4.py interactive input1.txt human-next 5

Participate in tournament: No.
