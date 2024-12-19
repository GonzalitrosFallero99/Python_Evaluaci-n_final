
def ver(pregunta, lista_repuestas):

    print(f"{pregunta}\n")
    num=1
    for i in lista_repuestas:
        print(f"\t {num}) " + i)
        num+=1
