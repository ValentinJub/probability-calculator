import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs) -> None:
    self.contents = self.unpack(kwargs)
  
  def unpack(self, c) -> None:
    return [k for k, v in c.items() for i in range(v)]

  def repack(self, l):
    self.contents = l[:]


  def draw(self, n) -> list:
    if n >= len(self.contents): 
      return self.contents
    result = []
    listToReduce = self.contents
    for i in range(n):
      x = random.randint(0, len(listToReduce) - 1)
      i = listToReduce[x]
      result.append(i)
      listToReduce.remove(i)
    return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  hit = 0
  loop = num_experiments
  originalContent = hat.contents[:]
  while loop:
    fail =  False
    counts = dict()
    r = hat.draw(num_balls_drawn)
    for ball in r:
      counts[ball] = counts.get(ball, 0) + 1
    try:
      for color, number in expected_balls.items():
        if counts[color] >= number:
          fail = False 
        else:
          fail = True
          break
    except:
      fail = True
    loop -= 1
    if not fail: hit += 1
    hat.repack(originalContent)
  prob = hit / num_experiments
  return prob
