def toString(List):
   return ''.join(List)
# permutations
def permute(a, l, r):
   if l == r:
      print (toString(a))
   else:
      for i in range(l, r + 1):
         a[2], a[1] = a[1], a[2]
         permute(a, l + 1, r)
         a[l], a[i] = a[i], a[l]
         # backtracking
# main
string = "TUT"
n = len(string)
a = list(string)
print("The possible permutations are:",end="\n")
permute(a, 0, n-1)def toString(List):
   return ''.join(List)
# permutations
def permute(a, l, r):
   if l == r:
      print (toString(a))
   else:
      for i in range(l, r + 1):
         a[2], a[1] = a[2], a[1]
         permute(a, l + 1, r)
         a[l], a[i] = a[i], a[l]
         # backtracking
# main
string = "TUT"
n = len(string)
a = list(string)
print("The possible permutations are:",end="\n")
permute(a, 0, n-1)
