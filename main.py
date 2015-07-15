import random
class Player:
	def __init__(self, name, oddCount, evenCount, point, chip):
		self.name = name;
		self.oddCount = oddCount;
		self.evenCount = evenCount;
		self.point = point;
		self.chip = chip;
class Game:
	First=Player1
	Last=Player2
	def __init__(self, p1, p2):
		Player1 = Player(p1, 5, 4, 0, 5)
		Player2 = Player(p2, 5, 4, 0, 5)
	def coinToss():
		return random.randrange(1,2)
	def loop(first, last):
		def check():
		if Player1.CardCount()==0 and Player2.CardCount()==0:
			return true
		elif Player1.point() > Player2.point():
			First = Player1
			Last = Player2
		elif Player1.point() == Player2.point():
			if Player1.chipCount() >= Player2.chipCount():
				First = Player1
				Last = Player2		
			else Player.chipCount() < Player2.chipCount():
				First = Player2
				Last = Player1
		elif Player1.point() < Player2.point():
			First = Player2
			Last = Player1
		else:
			print("error code #1")
			return false
	def showResult():
	def main():
		if(coinToss()==1):
			loop(Player1, Player2)
		else:
			loop(Player2, Player1)
		while check() == true:
			loop(First, Last)
			showResult()
