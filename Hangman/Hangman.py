import random
from assist import logo, stages, word_list

print(logo)

word = random.choice(word_list)
word_le = len(word)
print(word)
decoded = list(len(word)* '_' )

turns = 6
runnig = True
while runnig:
	if turns >= 0:
		user_input = input(' Guess a litter: ').lower()
		for pos in range(len(word)):
			litter = word[pos]
			if user_input == litter:
				decoded[pos] = user_input

		if user_input not in word:
			print(stages[turns])
			turns = turns - 1
		print(decoded)
		if '_' not in decoded:
			print('You Win')
			runnig = False
	else:
		print('Game over')
		break
