import os

def menu():
   
    os.system('clear')

    actividad = 0
    clima = 0
    personas = 0
    
    print ("      ----------------------------------------------")
    print ("      ----------------------------------------------")
    print ("            RECOMENDACION DE LUGARES TURÍSTICOS  \n")
    
    print (" -- ACTIVIDADES: \n")
    print ("   1. Actividades con aventuras ")
    print ("   2. Actividades que incluyan deportes extremos ")
    print ("   3. Actividades recreativas \n")
    actividad = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto: ")
    if actividad == "1":
        actividad = 1
        print ("   Gracias! \n")
    if actividad == "2":
        actividad = 2
        print ("   Gracias! \n")
    if actividad == "3":
        actividad = 3
        print ("   Gracias! \n")

    print (" -- CLIMAS: \n")
    print ("   1. Clima frío")
    print ("   2. Clima cálido ")
    print ("   3. Clima Templado \n")
    clima = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto: ")
    if clima == "1":
        clima = 1
        print ("   Gracias! \n")
    if clima == "2":
        clima = 2
        print ("   Gracias! \n")
    if clima == "3":
        clima = 3
        print ("   Gracias! \n")

    print (" -- NÚMERO DE PERSONAS: \n")
    print ("   1. Viaja con un grupo de 4, 5 o 6 personas")
    print ("   2. Viaja solo ")
    print ("   3. Viaja con su familia")
    print ("   4. Viaja con su pareja  \n")
    personas = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto:  ")
    if personas == "1":
        personas = 1
        print ("   Gracias! \n")
    if personas == "2":
        personas = 2
        print ("   Gracias! \n")
    if personas == "3":
        personas = 3
        print ("   Gracias! \n")
    if personas == "4":
        personas = 4
        print ("   Gracias! \n")
    

    
menu()
        
        
        
