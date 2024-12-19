import time
import random
import fin
import ver_preguntas
import preguntas
import Inicio

Inicio.bienvenida()
aciertos = 0
comodin_usado = False

for i in preguntas.obtener_pregunta():
    pregunta = i['question']
    correcta = i['correct_answer']
    respuestas = i['incorrect_answers']

    #Asignamos todas las respuestas en una lista
    todas = respuestas
    todas.append(correcta)
    random.shuffle(todas)

    #Llamamos a la funcion
    ver_preguntas.ver(pregunta,todas)

    comodin = input("\n¿Quieres usar un comodín? ")
    if comodin_usado:
        print("Ya no tienes comodines tienes que responder")
    elif comodin == "si":
         print("¡Comodín usado!\n")
         comodin_usado = True
         continue


    user = input("\nIntroduce la respuesta correcta: ")
    if user == correcta:
        print("Respuesta correcta\n")
        aciertos +=1

    else:
        print("Respuesta incorrecta")
        break

    time.sleep(2)

fin.final(aciertos)



