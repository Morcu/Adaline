import csv, operator, random

def main():
  
  vectorPesos = []
  vectorEntrada = []
  vectorValidacion = []
  vectorTest = []
  vectorErrores = []
  numeroCiclo = 0
  umbral = random.random()
  tasaEntrenamiento = 0.01
  salidaEsperada = 0
  salidaObtenida = 0
  numeroPatrones = 0
  numeroPatronesValidacion = 0
  numeroPatronesTest = 0
  
  fileErrores = open ("errores.csv","w")
  fileErrores.write ("Ciclo;ErrorEntrenamiento;ErrorValidacion" + '\n')
  
  with open('Entrenamiento.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
		numeroPatrones = numeroPatrones + 1
		intermedio = []
		for dato in reg:
		   intermedio.append(float(dato))
		vectorEntrada.append(intermedio)
  for iterador in range(0, len(vectorEntrada[0])-1):
    vectorPesos.append(random.random())      
  

  with open('Validacion.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
	numeroPatronesValidacion = numeroPatronesValidacion + 1
	intermedio = []
	for dato in reg:
	   intermedio.append(float(dato))
    	vectorValidacion.append(intermedio)
    	
    	
  with open('Test.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    for reg in entrada:
        numeroPatronesTest = numeroPatronesTest + 1
	intermedio = []
	for dato in reg:
	   intermedio.append(float(dato))
    	vectorTest.append(intermedio)


  while (numeroCiclo < 500):


	  #Un ciclo del adaline.
	  for patron in vectorEntrada:
		salidaEsperada = patron[len(vectorEntrada[0])-1]
		for entradaPeso in range (0,len(patron)-1):
		  salidaObtenida = salidaObtenida + patron[entradaPeso] * vectorPesos[entradaPeso]
		salidaObtenida = (salidaObtenida + umbral) 
		delta = (salidaEsperada - salidaObtenida) * tasaEntrenamiento

		for peso in range (0,len(vectorPesos)):
		  vectorPesos[peso] = vectorPesos[peso] + delta * patron[peso]      

		umbral = umbral + delta
		
		salidaObtenida = 0
		
	  
	    


	  #--------------------------------------------------------------------------
	  
	  
	  
	  errorEntrenamiento = 0
	  for patron in vectorEntrada:
		salidaEsperada = patron[len(vectorEntrada[0])-1]
		for entradaPeso in range (0,len(patron)-1):
		  salidaObtenida = salidaObtenida + patron[entradaPeso] * vectorPesos[entradaPeso]
		salidaObtenida = (salidaObtenida + umbral) 
		errorEntrenamiento = errorEntrenamiento + pow((salidaEsperada - salidaObtenida), 2)
		salidaObtenida = 0
		
	  errorEntrenamiento = errorEntrenamiento / numeroPatrones
	  
	  #TODO: meter errores en array y pasarlos a un fichero
	   
	  
	  
	  errorValidacion = 0
	  for patron in vectorValidacion:
		salidaEsperada = patron[len(vectorValidacion[0])-1]
		for entradaPeso in range (0,len(patron)-1):
		  salidaObtenida = salidaObtenida + patron[entradaPeso] * vectorPesos[entradaPeso]
		salidaObtenida = (salidaObtenida + umbral) 
		
		errorValidacion = errorValidacion + pow((salidaEsperada - salidaObtenida), 2)
		salidaObtenida = 0
		
	  errorValidacion = errorValidacion / numeroPatronesValidacion
          fileErrores.write (str(numeroCiclo) + ";" + str(errorEntrenamiento) + ";" + str(errorValidacion) + '\n')
	  vectorErrores.append([numeroCiclo, errorEntrenamiento, errorValidacion])
	  numeroCiclo = numeroCiclo + 1
	    
	    

  errorTest = 0
  for patron in vectorTest:
	salidaEsperada = patron[len(vectorValidacion[0])-1]
	for entradaPeso in range (0,len(patron)-1):
	  salidaObtenida = salidaObtenida + patron[entradaPeso] * vectorPesos[entradaPeso]
	salidaObtenida = (salidaObtenida + umbral) 
	
	errorTest = errorTest + pow((salidaEsperada - salidaObtenida), 2)
	salidaObtenida = 0
	
  errorTest = errorTest / numeroPatronesTest

	    
  print (vectorErrores)
  print (errorTest)
   
   
  fileErrores.write ('\n' + "--------------------------------------------------------------------------"+ '\n' + '\n')
  fileErrores.write (str(errorTest))

  #--------------------------------------------------------------------------
    





main()




