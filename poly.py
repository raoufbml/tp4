class Polynome:
    def __init__(self, coefficients):
        """
        Initialise un polynôme avec un tableau de coefficients.
        Les coefficients sont ordonnés par puissance croissante de x.
        Exemple : pour P(x) = 2 + 3x + x^3, coefficients = [2, 3, 0, 1].
        """
        self.coefficients = coefficients  # Les coefficients du polynôme, accessibles publiquement

    def afficher(self):
        """Renvoie le polynôme sous forme de chaîne lisible."""
        chaine = ""
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:
                if i == len(self.coefficients) - 1:
                    chaine += f"{self.coefficients[i]}*X^{i}"
                elif i == 0:
                    chaine += f"{self.coefficients[i]} + "
                else:
                    chaine += f"{self.coefficients[i]}*X^{i} + "
        return chaine

    def get_valeur(self, x):
        """Calcule la valeur du polynôme pour une valeur donnée de x."""
        val = 0
        for i in range(len(self.coefficients)):
            val += self.coefficients[i] * (x ** i)
        return val

    def deriver(self):
        """Calcule et renvoie le polynôme dérivé sous forme d'une nouvelle instance de Polynome."""
        D = [i * self.coefficients[i] for i in range(1, len(self.coefficients))]
        return Polynome(D)

# Exemple d'utilisation de la classe Polynome
p = Polynome([2, 3, 0, 1])  # Représente le polynôme P(x) = 2 + 3*X^1 + 0*X^2 + 1*X^3

# Affichage du polynôme
print("P(x) =", p.afficher())

# Calcul de la valeur du polynôme pour x = 5
valeur_x_5 = p.get_valeur(5)
print(f"P(5) = {valeur_x_5}")

# Dérivation du polynôme et affichage du polynôme dérivé
p_prime = p.deriver()
print("P'(x) =", p_prime.afficher())



