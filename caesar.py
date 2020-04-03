from stuff import clear, dialogue, num_input
from string import ascii_lowercase
clear()

def caesar(text, shift, encrypt, alpha):
	cipher = alpha[shift:] + alpha[:shift]
	key = {alpha[i]: cipher[i] for i in range(len(alpha))} if encrypt else {cipher[i]: alpha[i] for i in range(len(alpha))}
	return ''.join(l if l.lower() not in alpha else (key[l.lower()].upper() if l.upper() == l else key[l]) for l in text)
	
while True:
	encrypt = False if 'd' in input('Decrypt or Encrypt: ').lower() else True
	print('Encrypt' if encrypt else 'Decrypt')
	shift = num_input('Shift (leave blank for all shifts): ')
	print('All shifts' if shift == 0 else shift)
	text = input('Text: ')
	alpha = ascii_lowercase
	if shift > 0:
		dialogue(caesar(text, shift, encrypt, alpha))
	else:
		for s in range(1, 26):
			print(f'{s}) {caesar(text, s, encrypt, alpha)}')
		dialogue()
