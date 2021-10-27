from typing import Annotated
from automata.fa.dfa import DFA

#Iniciar DFA-Método de árbol

#Creación de clase DFA
dfa = DFA(

    #Establacer estados del autómata
    #Establecer caracteres del lenguaje
    #Ingresar transiciones 
    states={'1','2','3','4','5','6'},
    input_symbols={'C','c','V','v','x'},
    transitions= {
        '1':{'C':'4','V':'5','x':'6'},
        '2':{'C':'4','c':'4'},
        '3':{'V':'5','v':'5'},
        '4':{'V':'2','v':'2'},
        '5':{'C':'3','c':'3'},
        '6':{'x':'6'}             
    },
    
    #Configurar estado inicial
    #Configurar estados finales
    #Permitir matriz no cuadrada
    initial_state= '1',
    final_states={'2','3','6'},
    allow_partial=True
)

#Convertir cadena en variables reconocibles Ej: CaSa-CvCv
aux2=0
def vowel_or_consonant(c):
    if not c.isalpha():
        aux2=1
    if c.isnumeric():
        return 'x'
    vowels = 'aeiou'
    if c.lower() in vowels:
        if c.isupper():
            return 'V'
        else:
            return 'v'
    else:
        if c.isupper():
            return 'C'
        else:
            return 'c'

#Conversión de texto ingresado en formato de lista a una cadena de texto aceptada por DFA
def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele  
    return str1   
#Recibir entrada de texto de GUI
anterior=3
def arranca(valor):
    aux = []
    contador=0
    switch=0
    error=None
    global anterior
    for c in valor:
        #Envío a conversión a cadenas reconocidas por DFA
        aux.append(vowel_or_consonant(c))
        #Verificador de caracter por caracter
        contador=contador+1
        if(contador % 2) == 0 and switch == 0:
            if(dfa.accepts_input(aux)):
                anterior=1
            else:  
                if anterior == 0 and switch == 0:
                    error=contador-1
                    switch=1
                else:            
                    error=contador
                    switch=1
        else:
            aux2=0
        anterior=0
    if contador == 1:
        switch=2
        error=1
    if (contador % 2) == 1:
        switch=3
#Definir aceptación o rechazo según el resultado de DFA
    if(dfa.accepts_input(listToString(aux))):        
        return "Cadena aceptada"
    elif switch==1 or switch==2:
        return "Cadena NO aceptada.  "+"Error en el caracter "+str(error)
    elif contador==1:
        return "Cadena NO aceptada.  "+"Unicamente se ingreso un caracter"
    elif switch==3:
        return "Cadena NO aceptada.  "+"La cadena no es par"
    else:
        return "Cadena NO aceptada"


#((x)|(x)+)|((Cv|CV)|(Vc|VC))|((Cv|CV)(cv|Cv|cV|CV)+)|((Vc|VC)(vc|Vc|vC|VC)+)