class Exo:
    def puissance(self, x, n):
        # Si n= 0, retourner 1 car tout nombre élevé à la puissance 0 est 1.
        if n == 0:
            return 1
        
        # n est négatif, utiliser la propriété x^(-n) = 1 / x^n.
        elif n < 0:
            return 1 / self.puissance(x, -n)
        
        else:
            return x * self.puissance(x, n - 1)


exo = Exo()
print(exo.puissance(2, 3))  
print(exo.puissance(2, 1))  
print(exo.puissance(2, 0))  
print(exo.puissance(2, -3)) 
print(exo.puissance(-10,7))