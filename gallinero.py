alimento_disponible = 80000
agua_disponible = 100000
abono_disponible = 0
huevos_generados = 0
huevos_de_codornis_generados = 0
huevos_de_gallina_generados = 0
huevos_de_pato_generados= 0
huevos_de_ganso_generados = 0

class ave_de_corral:
    def __init__(self, edad, estado):
        self.edad = edad
        self.estado = estado

    def comer(self):
        global alimento_disponible 
        alimento_disponible -= 100  # Por ejemplo, que coma 100 unidades
        

    def beber(self):
        global agua_disponible
        agua_disponible -= 100
        

    def producir_abono(self):
        global abono_disponible
        abono_disponible += 120

class ave_ponedora(ave_de_corral):

    def poner_huevos(self):
       global huevos_generados
       huevos_generados += 1 

class codornis(ave_ponedora):
    def poner_huevos(self):
        global huevos_de_codornis_generados 
        huevos_de_codornis_generados += 1

class gallina(ave_ponedora):
    def poner_huevos(self):
        global huevos_de_gallina_generados 
        huevos_de_gallina_generados += 0.7

class pata(ave_ponedora):
    def poner_huevos(self):
        global huevos_de_pato_generados
        huevos_de_pato_generados += 0.5

class gansa(ave_ponedora):
    def poner_huevos(self):
        global huevos_de_ganso_generados
        huevos_de_ganso_generados += 0.09
    
gallinas = []
codornises = []
gansas = []
patas = []

def manejar_aves(tipo_de_ave, cantidad):

    aves = []

    for _ in range (cantidad):
         ave = tipo_de_ave(edad= 1, estado= "sana")
         aves.append(ave)

    return aves 

gallinas = manejar_aves(gallina,100 )
codornices = manejar_aves(codornis, 100 )
patas = manejar_aves(pata, 4)
gansas = manejar_aves(gansa, 2)

for dia in range(1,11):
    print(f"\ndia {dia}")

    for ave in gallinas + codornices + patas + gansas:
        ave.comer()
        ave.beber()
        ave.poner_huevos()


    print(f"quedan {alimento_disponible} gramso de alimento \nquedan {agua_disponible} litros de agua ")
    print(f"las gansas han puesto: {huevos_de_ganso_generados} huevos \nlas gallina han puesto: {huevos_de_gallina_generados} huevos \nlas patas han puesto: {huevos_de_pato_generados} huevos \nlas codornises han puesto: {huevos_de_codornis_generados} huevos")

    

        
    




   
        
        
