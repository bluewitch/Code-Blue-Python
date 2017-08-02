class fizzbuzzPlayer():
  def __init__(self, playernum):
    self.playernum = playernum
  def think(self, input):
    if not divmod(input,3)[1] and not divmod(input,5)[1]: return 'fizzbuzz'
    elif not divmod(input,3): return 'fizz'
    elif not divmod(input,5): return 'buzz'
    else: return str(input)
  def play(self, input):
    return('Player ' + str(self.playernum) + ' says: ' + self.think(input))

player_one = fizzbuzzPlayer(1)
player_two = fizzbuzzPlayer(2)

i=0
while(i<=42):
  i+=1
  if not divmod(i, 2)[1]: print(player_one.play(i))
  else: print(player_two.play(i))
