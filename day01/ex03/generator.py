
def generator(text, sep, option):
	lst = text.split(sep)
	for word in lst:
		lst.sort()
		yield (word)

if __name__ == "__main__":
	text = "Le Lorem Ipsum est simplement du faux texte."
	sep = ' '
	option = 'ordered'
	for word in generator(text, sep, option):
		print(word)