import math
# Objects

# -- `Sym`s summarize a stream of symbols.
class Sym:

  def __init__(self,c=0,s=""):
    self.n=0 # items seen
    self.at=c # column position
    self.name=s # column name
    self._has={} # kept data

  # Helpers
  # Add one thing to `col`. For Num, keep at most `nums` items. 
  def add(self, v):
    if v != "?":
      self.n = self.n + 1
      self._has[v] = 1 +  ( self._has[v]  if(v in self._has) else 0)

  def mid(self, col, most, mode):
    most = -1
    for k,v in self._has.items():
      if(v > most):
        mode, most = k, v
    return mode
  
  def div(self,e, fun):
    # helper func
    def fun(p):
      return p* math.log(p,2)
    
    e = 0
    for _,n in self._has.items():
      if( n> 0):
        e = e - fun(n/self.n)
    return e 