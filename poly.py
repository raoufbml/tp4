def afficher(p) :
    chaine = ""
    for i in range(len(p)) :
      if p[i] != 0 :
        if i == (len(p)-1) :
          chaine += f"{p[i]}*X^{i}"
        elif i==0 :
          chaine += f"{p[i]} + "
        else :
          chaine += f"{p[i]}*X^{i} + "

    return f"{chaine}"

def get_valeur(p,x) :
  val = 0
  for i in range(len(p)) :
    val = val + p[i]*(x**i)

  return print(f"P({x}) = {val}")

def deriver(p) :
  D=[]
  for i in range (1,len(p)):
    D.append(i*p[i])
  return print(f"P'(x) = {afficher(D)}")

x=[2,3,0,1]

print(f"P(x) = {afficher(x)}")

get_valeur(x,5)

deriver(x)