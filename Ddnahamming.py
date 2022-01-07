"""
Define a function hammingdistance that takes 2 DNA string inputs.

-First the function should check if both strings are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-Next, if the strings are of different lengths, the function should also return "error".

-If they are both valid DNA strands and the same length, the function calculates how many of the corresponding nucleotides in each string do not match (known as the Hamming Distance)

For example, hammingdistance("TTAC", "TGAA") should return 2.
"""
from Antcheck import isDNA

def hammingdistance(dna1, dna2):
  if isDNA(dna1) == False or isDNA(dna2) == False:
    return "error"
  if len(dna1) != len(dna2):
    return "error"
  counter = 0
  for nucleo1 in dna1:
    index = dna1.index(nucleo1)
    nucleo2 = dna2[index]
    if nucleo1 == nucleo2:
      counter += 1 
  return counter 