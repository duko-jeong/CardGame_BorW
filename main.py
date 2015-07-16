import random
class Player:
	def __init__(self, name, oddCount, evenCount, point, chip):
		self.name = name
		self.oddCount = oddCount
		self.evenCount = evenCount
		self.point = point
		self.chip = chip
	def name():
		return name
	def CardCount():
		return oddCount+evenCount
	def point():
		return point
	def chipCount():
		return chip
	def getPoint(score):
		point+=score
	def getChip(count):
		chip+=count
	def loseChip(count):
		chip-=count
	def loseOdd():
		oddCount-=1
	def loseEven():
		evenCount-=1
class Game:
	def __init__(self, p1, p2):
		self.Player1 = Player(p1, 5, 4, 0, 5)
		self.Player2 = Player(p2, 5, 4, 0, 5)
		self.First=self.Player1
		self.Last=self.Player2
	def coinToss(self):
		return random.randrange(1,2)
	def loop(self, first, last):
		print('Dear {p1}, submit your card\n'.format(p1=first.name()))
		card_p1=input(" number : ")
		if card_p1%2==0:
			first.loseEven()
			print('{p1} : #'.format(p1=first.name()))
		else:
			first.loseOdd()
			print('{p1} : @'.format(p1=first.name()))
		print('Dear {p2}, submit your card\n'.format(p2=last.name()))
		card_p2=input(" number : ")
		if card_p2%2==0:
			last.lostEven()
			print('{p2} : #'.format(p2=last.name()))
		else:
			last.lostOdd()
			print('{p2} : @'.format(p2=last.name()))
		print("Finished Submit\n")
		print("Start Betting\n")
		print('Dear {p1}, Will you join this betting?\n'.format(p1=first.name()))
		print("input yes or no\n")
		p1_decision=input(" : ")
		if p1_decision=='yes' or p1_decision=='Yes':
			print('betting this match using chips\n')
			print("which is your prediction. win or lose\n")
			p1_prediction=input(" input win or lose : ")
			print("How much chips do you bet?\n")
			p1_bet=input(" number : ")
			first.loseChip(p1_bet)
			print("Finished your turn, Thank you, Wait result\n")
			
			print('Dear {p2}, Will you join this betting?\n'.format(p2=last.name()))
			print("input yes or no\n")
			p2_decision=input(" : ")
			if p2_decision=='yes' or p2_decision=='Yes':
				print('betting this match using chips\n')
				print("which is your prediction. win or lose\n")
				p2_prediction=input(" input win or lose : ")
				print("How much chips do you bet?\n")
				p2_bet=input(" number : ")
				last.loseChip(p2_bet)
				print("Finished your turn, Thank you, Wait result\n")
			elif p2_decision=='no' or p2_decision=='No':
				print('{p2} gave up this betting\n'.format(p2=last.name()))
				print("Wait result\n")
			else:
				print("error code #2\n")
		elif p1_decision=='no' or p1_decision=='No':
			print('{p1} gave up this betting\n'.format(p1=first.name()))
			print("Wait result\n")
		else:
			print("error code #3\n")
			
	def check(self):
		if Player1.CardCount()==0 and Player2.CardCount()==0:
			if Player1.chipCount()+Player1.point() > Player2.chipCount()+Player2.point():
				FinalWinner=first.name()
				FinalLoser=last.name()
				isFinalDraw=false
			elif Player1.chipCount()+Player1.point() == Player2.chipCount()+Player2.point():
				isFinalDraw=true
			if Player1.chipCount()+Player1.point() < Player2.chipCount()+Player2.point():
				FinalWinner=last.name()
				FinalLoser=first.name()
				isFinalDraw=false
			return true
		elif Player1.point() > Player2.point():
			First = Player1
			Last = Player2
		elif Player1.point() == Player2.point():
			if Player1.chipCount() >= Player2.chipCount():
				First = Player1
				Last = Player2		
			elif Player1.chipCount() < Player2.chipCount():
				First = Player2
				Last = Player1
			else:
				print("error code #4\n")
		elif Player1.point() < Player2.point():
			First = Player2
			Last = Player1
		else:
			print("error code #1\n")
			return false
	def process(self):
		if card_p1>card_p2:
			first.getPoint(3)
			winner=first.name()
			loser=last.name()
			isDraw=false
			if p1_decision == 'yes' and p1_bet > 0:
				first.getChip(p1_bet*2)
		elif card_p1==card_p2:	
			isDraw=true
		elif card_p2>card_p1:
			last.getPoint(3)
			winner=last.name()
			loser=first.name()
			isDraw=false
			if p2_decision == 'yes' and p2_bet > 0:
				first.getChip(p2_bet*2)
	def showResult(self):
		print("Result\n")
		if isDraw!=true:
			print('Win -> {Winner}, Lose -> {Loser}\n'.format(Winner=winner, Loser=loser))
		else:
			print(" Draw \n")
		print("Status\n")
		print('{p1} | oddCard : {odd}, evenCard : {even}, Chips : {chip}, Point : {point}\n'.format(p1=Player1.name(),odd=Player1.oddCount(),even=Player1.evenCount(),chip=Player1.chipCount(), point=Player1.point()))
		print('{p2} | oddCard : {odd}, evenCard : {even}, Chips : {chip}, Point : {point}\n'.format(p2=Player2.name(),odd=Player2.oddCount(),even=Player2.evenCount(),chip=Player2.chipCount(), point=Player2.point()))
	def main(self):
		if(self.coinToss()==1):
			self.loop(self.Player1, self.Player2)
		else:
			self.loop(self.Player2, self.Player1)
		while check() == true:
			self.loop(First, Last)
			showResult()
		print("Final result\n")
		if isFinalDraw!=true:
			print('Win -> {Winner}, Lose -> {Loser}\n'.format(Winner=FinalWinner, Loser=FinalLoser))
		else:
			print(" Draw \n")
		print("Final Status\n")
		print('{p1} |  Chips : {chip}, Point : {point}\n'.format(p1=Player1.name(),chip=Player1.chipCount(), point=Player1.point()))
		print('{p2} |  Chips : {chip}, Point : {point}\n'.format(p2=Player2.name(),chip=Player2.chipCount(), point=Player2.point()))	
player1=input(" p1_nickName : ")
print(type(player1))
player2=input(" p2_nickName : ")
new=Game(player1, player2)
new.main()
