from diagCreator import *
import argparse
import sys
import os
from multiprocessing import Pool
import time

def draw(arg):

   particles = arg["fields"]
   out = arg["out"]

   fd = fullDiagram()
   fd.set(particles) 
   fd.plot(name=out)

   return    


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Command line parser to plot feynman diagrams from SMEFTsim models')
   parser.add_argument('-m',  '--model',   dest='model',     help='The SMEFTsim relative/absolute path to the  UFO folder you want to use', required = True)
   parser.add_argument('-o',  '--output',   dest='output',     help='The output folder where you want to save plots', required = True)
   parser.add_argument('-op',  '--operators',   dest='operators',     help='The operators you want to plot', required = True, nargs='+', default = [])
   parser.add_argument('-np',  '--nproc',   dest='nproc',     help='Number of process for multiprocessing', required = False, default = 1, type=int)
   args = parser.parse_args()
   
   t1_start = time.time() 
   # create output dir
   if not os.path.isdir(args.output):
      os.makedirs(args.output)
   
   # append ufo model path so we can import couplings and particles
   sys.path.append(args.model)
   import couplings as C
   import vertices as V

   
   # loading all vertices in a readable way
   vertices_dict = {}
   for vertex in V.all_vertices:
   
      # this will be appended to all the coefficients 
      # fields = [i.name for i in vertex.particles]
      
      for _, coupling in vertex.couplings.items():
         if coupling.name not in vertices_dict.keys():
            vertices_dict[coupling.name] = []
         
         # vertices_dict[coupling.name].append(fields)
         vertices_dict[coupling.name].append(vertex.particles)

   ops = {}

   for op in args.operators:
      # store the list of couplings for each op
      ops[op] = []
      op_order = "NP" + op
      for obj in C.all_couplings:
         if op_order in obj.order.keys(): ops[op].append(obj.name)

   
   # build list for multithreading 
   mt_args = []
   
   # cycle on the ops
   for op in ops.keys():
      # cycle on the list of couplings
      for coupling in ops[op]:
         # cycle on the vertices where this thing contribute
         for particles in vertices_dict[coupling]:
            mt_args.append({
               "fields": particles, 
               "out": args.output + "/" + op + "_" + coupling + "_" + "_".join(j.name for j in particles) + ".png" 
            })

    
   pool = Pool(processes=args.nproc)
   pool.map(draw, mt_args)

   t1_stop = time.time()
   print("Elapsed time: ",t1_stop-t1_start)  
