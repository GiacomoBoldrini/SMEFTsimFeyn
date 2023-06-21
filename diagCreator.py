import sys
sys.path.append("feynman/")
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from feynman import Diagram

class converter():
   

   convertion = {
  
      "a": {"style": "wiggly"},
      "Z": {"style": "wiggly"},
      "W+": {"style": "wiggly"},
      "W-": {"style": "wiggly"},
      "g": {"style":"linear loopy", "xamp":.025, "yamp":.035, "nloops":7},
      "Z1": {"style": "wiggly"},
      "W1+": {"style": "wiggly"},
      "W1-": {"style": "wiggly"},
      "ve": {"arrow":False},
      "ve~": {"arrow":False},
      "vm": {"arrow":False},
      "vm~": {"arrow":False},
      "vt": {"arrow":False},
      "vt~":{"arrow":False},
      "e-": {"arrow":False},
      "e+": {"arrow":False},
      "mu-": {"arrow":False},
      "mu+": {"arrow":False},
      "ta-": {"arrow":False},
      "ta+": {"arrow":False},
      "u": {"arrow":False},
      "u~": {"arrow":False},
      "d": {"arrow":False},
      "d~": {"arrow":False},
      "c": {"arrow":False},
      "c~": {"arrow":False},
      "s": {"arrow":False},
      "s~": {"arrow":False},
      "b": {"arrow":False},
      "b~": {"arrow":False},
      "t": {"arrow":False},
      "t~": {"arrow":False},
      "t1": {"arrow":False},
      "t1~": {"arrow":False},
      "H": {"arrow":False, "style":"dashed"},
      "H1": {"arrow":False, "style":"dashed"},

   }

   def __init__(self):
      pass

   def get(self, field_name):
      if field_name not in self.convertion:
         raise ValueError("Value {} is not a known field".format(field_name)) 

      return self.convertion[field_name]


class baseDiagrams():

   fields = []
   
   center = [0.5, 0.5]
 
   # [(x,y), ...]
   extremes_6fields = [(0.2, 0.9), (0.8, 0.9), (0.9, 0.5), (0.8, 0.1), (0.2, 0.1), (0.1, 0.5)]
   extremes_5fields = [(0.5, 0.9), (0.1, 0.5), (0.9, 0.5), (0.2, 0.1), (0.8, 0.1)]
   extremes_4fields = [(0.9, 0.9), (0.1, 0.1), (0.9, 0.1), (0.1, 0.9)]
   extremes_3fields = [(0.1, 0.1), (0.9, 0.1), (0.5, 0.9)]

   ex = {
        6: extremes_6fields,
	5: extremes_5fields,
        4: extremes_4fields,
        3: extremes_3fields,
   }
 
   def __init__(self):
      pass

   def get(self):
      if len(self.fields) == 0: 
         raise ValueError("You first need to setup the fields by calling the set function")

      return self.center, self.ex[len(self.fields)]
      # if len(self.fields)==3: return self.center, self.extremes_3fields
      # elif len(self.fields)==4: return self.center, self.extremes_4fields

   def set(self, fields):
      print(fields)
      if not isinstance(fields, list): raise ValueError("first argument should be a list with the vertices")
      if len(fields) not in [3,4,5,6]: raise ValueError("This program only works with 3 or 4 vertices")

      self.fields = fields


class fullDiagram(baseDiagrams):

   conv_ = converter()

   
   def plot(self, name="plot.png"):

      fig = plt.figure(figsize=(10.,10.))
      ax = fig.add_axes([0,0,1,1], frameon=False)

      diagram = Diagram(ax)

      center_, extremes = self.get()
      center_vertex = diagram.vertex(xy=center_)

      vertices = []
      for ex_ in extremes:
         vertices.append( diagram.vertex(xy=ex_, marker='')  )
   
      lines = []
      for idx, field in enumerate(self.fields):
         lines.append(diagram.line(vertices[idx], center_vertex, **self.conv_.get(field.name)))
         lines[-1].text(field.name, size=30)


      diagram.plot()
      fig.savefig(name)
