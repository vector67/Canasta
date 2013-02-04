import random as myrandom
import collections
from itertools import groupby
class jeffPlayer:
  def __init__(self):
		self.hand = Hand()
		self.hasplayedout = 0
	def addPile(self,pile):
		self.hand.addPile(pile)
	def add(self,card):
		self.hand.add(card)
	def discard(self,card):
		self.hand.discard(card)
	def wantsToPickUpPile(self,card):
		return 0
	def canPickUpPile(self,card):
		return 0
	def discard(self):
		self.hand.sort()
		doublescards = []
		lengths = {}
		#print "start while"
		print self.hand.cards
		mycards = []
		for card in self.hand.cards:
			mycards.append(card.num)
		values = [len(list(group)) for key, group in groupby(mycards)]
		key = list(set(mycards))
		counter=collections.Counter(mycards)
		print(counter)
		print(counter.values())
		# [4, 4, 2, 1, 2]
		print(counter.most_common())
		# [1, 2, 3, 4, 5]
		return self.hand.discard(self.findlowestnot(self.hand.cards,[0,1]))
	def findlowestnot(self,arr,arr2):
		for card in arr:
			if(not self.contains(arr2,card.num)):
				return card
	def contains(self,arr, value):
		for x in arr:
			if(x==value):
				return 1
		return 0
class Hand:
	def __init__(self):
		self.cards = []
	def __repr__(self):
		return self.cards.__repr__()
	def add(self,card):
		self.cards.append(card)
	def addPile(self,pile):
		self.cards = self.cards+pile.cards
		pile.empty()
		self.sort()
	def discard(self,card):
		return self.cards.remove(card)
	def discardrandom(self):
		random1 = myrandom.Random()
		random1.shuffle(self.cards)
		del self.cards[random1.randint(0,len(self.cards)-1)]
	def sort(self):
		self.cards.sort(Card.compare)
class Score:
	def __init__(self,player):
		self.player = player
		self.points = 0
	def __repr__(self):
		return self.player.__repr__()+"-"+self.points
	def addScore(self,score):
		self.points = self.points + score
		if (self.points > 5000):
			return true
		return false
	def hasWon(self):
		return self.points > 5000
	def breakingPoint(self):
		if(self.points<1500):
			return 50
		else:
			if(self.points<3000):
				return 90
			else:
				return 120
class Pile:
	def __init__(self):
		self.cards = []
		self.isempty = 0
	def __repr__(self):
		return self.cards.__repr__()
	def add(self,card):
		self.cards.append(card)
	def empty(self):
		del self.cards[:]
	def deal(self):
		if(not len(self.cards)==0):
			return self.cards.pop()
		else:
			self.isempty = 1
	def shuffle(self):
		random1 = myrandom.Random()
		random1.shuffle(self.cards)
class Card:
	def __init__(self,points,value,num):
		self.points = points
		self.value = value
		self.num = num
	def __repr__(self):
		return self.value
	def compare(a,b):
		return (a.num-b.num)

points = [50 ,20 , 5 , 5 , 5 , 5 , 5 ,10 ,10 , 10 ,10 ,10 ,10 ,20 ]
values = ["$","2","3","4","5","6","7","8","9","10","J","Q","K","A"]
cards = {}
thepile = Pile()
num=0
suit=0
gameover = 0
numdecks = 5
counter = 0
deck=1
while deck<numdecks:
	while num<=13:
		cards[num] = {}
		while suit<=3:
			thepile.add(Card(points[num],values[num],num))
			suit = suit +1
			counter=counter+1
		suit=0
		num=num+1
	num=0
	deck = deck+1
thepile.shuffle()
numplayers = 4
players = {}
counter = 0
curplayer=0
while  curplayer < numplayers:
	players[curplayer] = jeffPlayer()
	curplayer = curplayer+1
curplayer=0
while counter<11:
	while curplayer < numplayers:
		players[curplayer].add(thepile.deal())
		curplayer = curplayer+1
	curplayer=0
	counter = counter + 1
#print players[3].hand.cards
currentplayer=0
discardpile = Pile()
round = 0
while 1:
	player = players[currentplayer]
	if(player.wantsToPickUpPile(thepile.cards[len(thepile.cards)-1]) and player.canPickUpPile(thepile.cards[len(thepile.cards)-1])):
		player.add(discardpile)
	else:
		player.add(thepile.deal())
		if(thepile.isempty):
			break
		player.add(thepile.deal())
		if(thepile.isempty):
			break
	discardpile.add(player.discard())
	if (player.hasplayedout):
		break
	if (len(players)-1)==currentplayer:
		round = round + 1
		currentplayer = 0
	currentplayer = currentplayer + 1
