# with open("names.txt", 'r') as f:
#     for x in f:
#         print(x)
with open("scrabble_list.txt", 'r') as f:

    scrabble_list = []
    for x in f:
        scrabble_list.append(x)
    alphabet = [a,	b,	c,	d,	e,	f,	g,	h,	i,	j,	k,	l,	m,	n,	o,	p,	q,	r,	s,	t,	u,	v,	w,	x,	y,	z,	]
    def play():
        print("welcome to ghost!")



    def getUserLetter():
        letter = input("gimme a letter")
        if(len(letter) == 1 and letter.isalpha()):
            return letter
        else:
            return getUserLetter()
    def getValidLetters(current_word):
        







