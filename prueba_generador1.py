def multiplos_de(n): 
    index = 1 
    while True: 
        yield index*n 
        index = index + 1 

if __name__ == '__main__': 
    # En este caso genera mltiplos de 7 
    for i in multiplos_de(7): 
        print i 
    # Bastara usar multiplos_de(5) para mltiplos de 5 
    # O multiplos_de(10) para generar mltiplos de 10 - See more at: http://www.alvarohurtado.es/generadores-en-python/#sthash.WdLgSIag.dpuf