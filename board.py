import random

class Board():
	board = [[] for i in range(0,30)]
	cur_left=0
	cur_right=89
	main_board = [[] for i in range(0,30)]
	enemy= []
	for i in range(0,30):
		if i>25:
			wall=":"
		else:
			wall=" "
		for j in range(0,500):
			main_board[i].append(wall)
	for i in range(0,30):
		for j in range(0,90):
			board[i].append(main_board[i][j+cur_left])
	def cloud_make(self,x,y):
		for i in range(0,10):
			self.main_board[x][y+i]=self.main_board[x][y-i]="_"
		for i in range(0,2):
			self.main_board[x-i][y-10-i]="("
			self.main_board[x-i][y+10+i]=")"
		for i in range(0,2):
			self.main_board[x-2-i][y-12+i]="("
			self.main_board[x-2-i][y+12-i]=")"
		for i in range(0,6):
			self.main_board[x-4][y-10+i]=self.main_board[x-4][y+10-i]="_"
		for i in range(0,2):
			self.main_board[x-4-i][y-5-i]="("
			self.main_board[x-4-i][y+5+i]=")"
		for i in range(0,2):
			self.main_board[x-6-i][y-5+i]="("
			self.main_board[x-6-i][y+5-i]=")"
		for i in range(0,4):
			self.main_board[x-7][y+i]=self.main_board[x-7][y-i]="+"
		if self.cur_left<=y-10 and self.cur_right>=y+10:
			for i in range(0,10):
				self.board[x][y+i]=self.board[x][y-i]="_"
			for i in range(0,2):
				self.board[x-i][y-10-i]="("
				self.board[x-i][y+10+i]=")"
			for i in range(0,2):
				self.board[x-2-i][y-12+i]="("
				self.board[x-2-i][y+12-i]=")"
			for i in range(0,6):
				self.board[x-4][y-10+i]=self.board[x-4][y+10-i]="_"
			for i in range(0,2):
				self.board[x-4-i][y-5-i]="("
				self.board[x-4-i][y+5+i]=")"
			for i in range(0,2):
				self.board[x-6-i][y-5+i]="("
				self.board[x-6-i][y+5-i]=")"
			for i in range(0,4):
				self.board[x-7][y+i]=self.board[x-7][y-i]="+"

	def pit_make(self,x):
		for j in range(26,30):	
			for i in range(0,5):
				if j!=26:
					self.main_board[j][x-i]=self.main_board[j][x+i]=" "
				else:
					self.main_board[j][x-i]=self.main_board[j][x+i]="'"
		if self.cur_left<=x-2 and self.cur_right>=x+2:
			for j in range(26,30):	
				for i in range(0,5):
					if j!=26:
						self.board[j][x-i]=self.board[j][x+i]=" "
					else:
						self.board[j][x-i]=self.board[j][x+i]="'"
	def pillar_make(self,x):
		for j in range(22,26):
			for i in range(0,3):
				self.main_board[j][x-i]=self.main_board[j][x+i]=":"
		if self.cur_left<=x-2 and self.cur_right>=x+2:
			for j in range(22,26):
				for i in range(0,3):
					self.board[j][x-i]=self.board[j][x+i]=":"
	
	def remove_brick(self,x,y):
		self.board[x][y]=self.board[x][y+1]=" "
		self.board[x-1][y]=self.board[x-1][y+1]=" "
		self.main_board[x][y+self.cur_left]=self.main_board[x][y+1+self.cur_left]=" "
		self.main_board[x-1][y+self.cur_left]=self.main_board[x-1][y+1+self.cur_left]=" "

	def coin_make(self,x,y):
		self.main_board[x][y+self.cur_left]="C"
		if self.cur_left<=y and self.cur_right>=y:
			self.board[x][y]="C"

	def remove_coin(self,x,y):
		self.board[x][y]=" "
		self.main_board[x][y+self.cur_left]=" "

	def left(self):
		return self.cur_left
	
	def right(self):
		return self.cur_right
	
	def powerup(self,x,y):
		self.main_board[x][y+self.cur_left]="J"
		if self.cur_left<=y and self.cur_right>=y:	
			self.board[x][y]="J"

	def mountain_make(self,x,y):
		for i in range(0,10):
			if i!=0:
				self.main_board[x+i][y-i]="/"
				self.main_board[x+i][y+i]="\\"
			else:	
				self.main_board[x+i][y-i]="^"
		if self.cur_left<=y-10 and self.cur_right>=y+10:
			for i in range(0,10):
				if i!=0:
					self.board[x+i][y-i]="/"
					self.board[x+i][y+i]="\\"
				else:
					self.board[x+i][y-i]="^"
	def print_board(self):
		temp = ['' for i in range(0,30)]
		for j in range(0,30):
			for i in range(0,90):
				temp[j]+=self.board[j][i]
		for i in range(0,30):
			print(temp[i])
	def fix(self,xh,yl,h,l):
		temp = ['' for i in range(0,30)]
		self.cur_right+=1
		self.cur_left+=1
		for i in range(0,30):
			for j in range(0,90):
				if j==h and i==xh or j==h+1 and i==xh:
					temp[i]+="H"
				elif j==l and i==yl or j==l+1 and i==yl:
					temp[i]+="L"
				else:
					temp[i]+=self.main_board[i][self.cur_left+j]	
		for i in range(0,30):
			for j in range(0,90):
				self.board[i][j]=temp[i][j]
		for i in range(0,30):
			print(temp[i])