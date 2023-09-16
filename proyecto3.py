import random
palabras=("manzana","pera","piña","mango","membrillo","banana")
palabra_secreta=random.choice(palabras)
posibilidades=len(palabra_secreta)+2
suposiciones=["_"]*len(palabra_secreta)
fallos=0

def dibujar_ahorcado(fallos):
    ahorcado = [
        """
         ---------  
            |     |
                  |
                  |
                  |
                  |
        """,
        """ 
         ---------
            |     |
            o     |
                  |
                  |
                  |
        """,
        """ 
         ---------
            |     |
            o     |
            |     |
                  |
                  |
        """,
        """  
         ---------
            |     |
            o     |
            |\    |
                  |
                  |
        """,
        """ 
         ---------
            |     |
            o     |
           /|\    |
                  |
                  |
        """,
        """  
         ---------
            |     |
            o     |
           /|\    |
                  |
                  |
        """,
        """  
         ---------
            |     |
            o     |
           /|\    |
             \    |
                  |
        """,
        """  
         ---------
            |     |
            o     |
           /|\    |
           / \    |
                  |
        """,
        """  
         ---------
            |     |
            o     |
           /|\    |
           / \    |
          /   \   |
        """
    ]
    
    return ahorcado[fallos]



    
while fallos<8:
    suposición=input("Ingrese una letra: ")
   
    if len(suposición)!=1:
            print("Por favor ingrese una sola letra")
    else:
        if suposición in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i]==suposición:
                    suposiciones[i]=palabra_secreta[i]
            print("".join(suposiciones))
            if "".join(suposiciones)==palabra_secreta:
                  print("Genial.Adivinaste la palabra")
                  break
        else:
            print("Incorrecto")
                    
            fallos+=1
            print(dibujar_ahorcado(fallos))
    if fallos==8:
            print("Ahorcado.")
            break
            
    
   




            

    
