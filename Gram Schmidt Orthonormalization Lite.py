#Challenge 3 part 1 - Gram-Schmidt Orthonormalization

import math

def square(number):
   return float(number * number)
      
def normalize(vector):
   n = 0
   squares = []
   normal_elements = []
   while n < len(vector):
      squares.insert(n, square(vector[n]))
      n = n + 1
   sum = float(math.sqrt(squares[0] + squares[1] + squares[2]))
   i = 0
   while i < len(vector):
      normal_elements.insert(i, float(vector[i] / sum))
      i = i + 1
   return normal_elements

vector_1 = [float(input("Enter entry 1 of vector 1: ")), float(input("Enter entry 2 of vector 1: ")), float(input("Enter entry 3 of vector 1: "))]
vector_2 = [float(input("Enter entry 2 of vector 2: ")), float(input("Enter entry 2 of vector 2: ")), float(input("Enter entry 3 of vector 2: "))]
vector_3 = [float(input("Enter entry 1 of vector 3: ")), float(input("Enter entry 2 of vector 3: ")), float(input("Enter entry 3 of vector 3: "))]

vectors = [vector_1, vector_2, vector_3]

def dot_product(v1, v2):
   a = 0
   multiplication = []
   while a < len(v1):
      multiplication.insert(a, v1[a] * v2[a])
      a = a + 1
   sum = float(multiplication[0] + multiplication[1] + multiplication[2])
   return sum
   
def proj(v1, v2):
   LHS = dot_product(v2, v1) / dot_product(v1, v1)
   a = 0
   projected = []
   while a < len(v1):
      projected.insert(a, LHS * v1[a])
      a = a + 1
   return projected

proj(vector_1, vector_2)

def subtract(v1, v2):
   subtracted = []
   a = 0
   while a < len(v1):
      subtracted.insert(a, v1[a] - v2[a])
      a = a + 1
   return subtracted

w1 = vector_1
u1 = normalize(w1)

w2 = subtract(vector_2, proj(w1, vector_2))
u2 = normalize(w2)

w3 = subtract(subtract(vector_3, proj(w1, vector_3)), proj(w2, vector_3))
u3 = normalize(w3)

print(u1)
print(u2)
print(u3)