"""
Este programa lee un texto que el usuario quiera, lee las palabras y las ordena segun su rango de frecuencia en 5 rangos,
luego este le muestra al usuario el rango que quiera ver, le pide dijitar la palabra que este quiera, enseñando el significado de la palabra
si el usuario la quiere guardar el programa pregunta y crea una "ficha" donde esta la palabra y su significado, si el usuario quiere cerrar el programa
entonces cuando el programa pregunta si quiere ver otra, el usuario le digita "no" y el programa se termina
"""

"""solo un input para que el usuario ingrese el nombre del texto"""
def Texto(): 
    archivo=input("ingrese nombre del texto: " )
    return Texto2(archivo)


"""abre el texto que el usuario desee"""
def Texto2(archivo): 
    f=open(str(archivo)+".txt","r")
    archivo=f.read()
    f.close()
    return quitarsignos(archivo)

"""elimina todos los signos de puntuacion de el texto y divide el texto en palabras"""
def quitarsignos(x): 
    signos=["<",">","“","”","--","-","—",",",";",".","\n","(",")","[","]",'"',"@","#","/","!",'',":","?","¡","¿"," ","0","1","2","3","4","5","6","7","8","9"]
    c=0
    palabras=""
    while c<len(x):
        if x[c] not in signos:
            palabras=palabras+x[c]
            c=c+1
        else:
            if x[c] in signos:
                palabras=palabras+" "
                c=c+1
    return Minusculas(palabras)

"""recibe el texto sin los signos, convierte todas las mayusculas en minusculas"""
def Minusculas(palabras):
    palabras= palabras.lower()
    palabras=palabras.split()
    return contar(palabras)

"""llama a contar_aux con palabras, p, rango1, rango2, rango3, rango4 y rango5"""
def contar(palabras):
    return contar_aux(palabras,[],[],[],[],[],[])

"""toma las palabras del texto y las agrupa segun su rango de frecuencia""" 
def contar_aux(palabras,p,rango1,rango2,rango3,rango4,rango5):
    if palabras==[]:
        print("rango5=", rango5)
        print("")
        print("rango4=", rango4)
        print("")
        print("rango3=", rango3)
        print("")
        print("rango2=", rango2)
        print("")
        print("rango1=", rango1)
        print("")
        return elegiRango(rango1,rango2,rango3,rango4,rango5)
    else:
        p=palabras[0]
        palabractual=palabras.count(p)
        if palabractual<=5:
            rango1=rango1+[str(p)+" "+str(palabractual)]
            while p in palabras:
                palabras.remove(p)
            return contar_aux(palabras,p,rango1,rango2,rango3,rango4,rango5)
        elif palabractual>5 and palabractual<=10:
            rango2=rango2+[str(p)+" "+str(palabractual)]
            while p in palabras:
                palabras.remove(p)
            return contar_aux(palabras,p,rango1,rango2,rango3,rango4,rango5)

        elif palabractual>10 and palabractual<=15:
            rango3=rango3+[str(p)+" "+str(palabractual)]
            while p in palabras:
                palabras.remove(p)
            return contar_aux(palabras,p,rango1,rango2,rango3,rango4,rango5)

        elif palabractual>15 and palabractual<=20:
            rango4=rango4+[str(p)+" "+str(palabractual)]
            while p in palabras:
                palabras.remove(p)
            return contar_aux(palabras,p,rango1,rango2,rango3,rango4,rango5)

        elif palabractual>20:
            rango5=rango5+[str(p)+" "+str(palabractual)]
            while p in palabras:
                palabras.remove(p)
            return contar_aux(palabras,p,rango1,rango2,rango3,rango4,rango5)
        
"""toma el rango que el usuario eligio y le quita los numeros de frecuencia y devuelve una lista con solo las palabras"""
def Rsignos(R,r):
    if R==[]:
        return r
    else:
        if R[0][len(R[0])-2]==" ":
            r=r+[R[0][:len(R[0])-2]]
            return Rsignos(R[1:],r)
        else:
            r=r+[R[0][:len(R[0])-3]]
            return Rsignos(R[1:],r)


"""devuelve el significado de la palabra que el usuario escogio"""            
def significado(d):
    import urllib.request
    f = urllib.request.urlopen("http://www.ic-itcr.ac.cr/~ezeledon/wsdiccionario/buscar_definicion.php?word="+str(d))
    definicion= f.read()
    return(definicion.decode("utf8"))
    
"""abre la lista de las palabras ya conocidas y regresa la lista con estas"""
def Pconocidas(d):
    f=open("palabras conocidas.txt","a")
    f.write(d)
    f.close()
    return""
    
    

"""toma la lista que sale de Rsignos y pregunta sobre si se quiere el significado de alguna palabra, tambien crea una ficha para guardar la informacion de la palbra si asi se quiere"""
def Definicion(lista):
    print("")
    d=input("si desea saber el significado de alguna palabra del texto ingresela aqui: ")
    if d in lista:
        if d not in Pconocidas(d):
            print(significado(d))
            g=input("desea guardar palabra SI o NO: ")
            if g=="si" or "Si" or "SI" or "sI":
                f1=open(str(d)+".txt","w")
                f1.write(significado(d))
                f1.close()
                f2=open("palabras conocidas.txt","a")
                f2.write(str(d)+'\n')
                y=input("desea buscar otra palabra: ")
                if y=="si":
                    return Texto()
                else:
                    if y=="no":
                        return("Adios")
            else:
                if g=="no" or "No" or "NO" or "nO":
                    y=input("desea buscar otra palabra: ")
                    if y=="si":
                        return Texto()
                    else:
                        if y=="no":
                            return("Adios")
        else:
            if d in Pconocidas():
                print(significado(d))
                y=input("desea buscar otra palabra: ")
                if y=="si":
                    print (elegiRango(rango1,rango2,rango3,rango4,rango5))
                else:
                    return("Adios")
    elif d=="":
        return Definicion(lista)

    else:
        print("")
        print("la palabra no esta en el rango")
        return Definicion(lista)


"""toma los rangos y le pide al usuario que escoja el rango que desee, le entrega el rango que el usuario quiere a Rsignos"""
def elegiRango(rango1,rango2,rango3,rango4,rango5):
    x=input("eliga un rango (rango1, rango2, rango3, rango4 o rango5): ")
    if x=="rango1":
        print("")
        print("rango1: ",Rsignos(rango1,[]))
        if rango1==[]:
            print("rango vacio")
            return elegiRango(rango1,rango2,rango3,rango4,rango5)
        else:
            return Definicion(Rsignos(rango1,[]))
    elif x=="rango2":
        print("")
        print("rango2: ",Rsignos(rango2,[]))
        if rango2==[]:
            print("rango vacio")
            return elegiRango(rango1,rango2,rango3,rango4,rango5)
        else:
            return Definicion(Rsignos(rango2,[]))
    elif x=="rango3":
        print("")
        print("rango3: ",Rsignos(rango3,[]))
        if rango3==[]:
            print("rango vacio")
            return elegiRango(rango1,rango2,rango3,rango4,rango5)
        else:
            return Definicion(Rsignos(rango3,[]))
    elif x=="rango4":
        print("")
        print("rango4: ",Rsignos(rango4,[]))
        if rango4==[]:
            print("")
            print("rango vacio")
            return elegiRango(rango1,rango2,rango3,rango4,rango5)
        else:
            return Definicion(Rsignos(rango4,[]))
    elif x=="rango5":
        print("")
        print("rango5: ",Rsignos(rango5,[]))
        if rango5==[]:
            print("rango vacio")
            return elegiRango(rango1,rango2,rango3,rango4,rango5)
        else:
            return Definicion(Rsignos(rango5,[]))
    else:
        print("")
        print("rango no existe")
        print("")
        return elegiRango(rango1,rango2,rango3,rango4,rango5)

print(Texto())







