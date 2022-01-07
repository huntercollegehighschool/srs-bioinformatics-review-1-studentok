"""
Define a function reversecomplement that takes a DNA string as an input. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA string, the function finds the reverse complement of that string. The reverse complement is found by first reversing the string, then taking the complement of each nucleotide. A and T are complements of each other, and C and G are complements of each other.

For example,
reversecomplement("AAGCT") should return "AGCTT".
"""
from Antcheck import isDNA

def reversecomplement(dna):
  if isDNA(dna) == False:
    return "error"
  dna_list = list(dna)
  dna_list.reverse()
  complement = []
  for nucleo in dna_list:
    if nucleo == "A":
      complement.append("T")
    elif nucleo == "G":
      complement.append("C") 
    elif nucleo == "C":
      complement.append("G")
    else:
      complement.append("A")
  return complement 
