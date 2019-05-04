import itertools

def funct(gg):

	def all(l):
		if l.count(l[0])==len(l) and l[0]!=0:
			return True
		else:
			return False	
	for row in game:
		if all(row):
			print("Player {}".format(curr_player)+" wins horizontally",row)
			return True	
	
	for col in range(len(game)):
		check=[]
		for row in game:
			check.append(row[col])
		if all(check):
			print ("Player {}".format(curr_player)+" wins vertically",check)
			return True
	diag=[]
	for ix in range(len(game)):
		diag.append(game[ix][ix])
	if all(diag):
		print("Player {}".format(curr_player)+" wins diagonally \\",diag)
		return True 
	diags=[]
	row=list(reversed(range(len(game))))
	col=range(len(game))
	for i,j in zip(row,col):
		diags.append(game[i][j])	
	if all(diags):
		print("Player {}".format(curr_player)+" wins diagonally /",diags)
		return True
	return False	

def function(w,x=0,y=0,z=0,just_display=False):
	try:	
		if w[y][z]!=0:
			print("Position Occupied ! Choose another")
			return w,False
		print("   "+"  ".join(str[i]) for i in range(len(w)))
		if not just_display:
			w[y][z]=x
		for count,y in enumerate(w):
			print(count,y)
		return w, True

	except IndexError as e:
		print("Wrong Index Value, Error:",e)
		return w,False

play=True		
while play:
	game_size=int(input("What game size do you wanna play?: "))
	game=[[0 for i in range(game_size)] for i in range(game_size)]
	game_won=False
	game, _ =function(game,just_display=True)
	player_choice=itertools.cycle([1,2])
	while not game_won:
		curr_player=next(player_choice)
		print("Current Player: {}".format(curr_player))
		played=False
		while not played:
			col_choice=int(input("enter a column choice:  "))
			row_choice=int(input("enter a row choice:  "))
			game,played=function(game,curr_player,row_choice,col_choice)		
		if funct(game):
			game_won=True
			again=input("The game is over , do you want to play again (Y/N) ")
			if again.lower()=='y':
				print("Restarting..")
			elif again.lower()=='n':
				print("Bye")
				play=False
			else:
				print("Not a valid answer ")
				play=False			