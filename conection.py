from py2neo import Graph, NodeMatcher

grafo = Graph("bolt://localhost:7473", auth=("neo4j","1234"))
matcher = NodeMatcher(grafo)
#7474
#7473

def menu():
    
    print ("      ----------------------------------------------")
    print ("      ----------------------------------------------")
    print ("            RECOMENDACION DE LUGARES TURÍSTICOS  \n")
    
    print (" -- ACTIVIDADES: \n")
    print ("   1. Aventuras ")
    print ("   2. Deportes Extremos ")
    print ("   3. Recreacion \n")
    actividad = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto (escriba la opcion tal y como aparece): ")


    print (" -- CLIMAS: \n")
    print ("   1. Frio")
    print ("   2. Calido ")
    print ("   3. Templado \n")
    clima = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto (escriba la opcion tal y como aparece): ")


    print (" -- NÚMERO DE PERSONAS: \n")
    personas = input (" - Ingrese el numero de personas que lo acompañarian (incluyendo a ud):  ")


#    statement1 = "MATCH(I:Lugar) <-[:pertenece]-(s:Actividades{Actividades: '" +actividad+ "'}) return l"
#    response1 = grafo.run(statement1).to_table()
#    print(response1)
#    
#    statement2 = "MATCH(I:Lugar) <-[:pertenece]-(s:Clima{Clima: '" +clima+ "'}) return l"
#    response2 = grafo.run(statement2).to_table()
#    print(response2)
#    
#    statement3 = "MATCH(I:Lugar) <-[:pertenece]-(s:Personas{Personas: '" +personas+ "'}) return l"
#    response3 = grafo.run(statement3).to_table()
#    print(response3)

    matcher.match("lugar", Actividades="Aventuras").first()
    matcher.match("lugar", Clima="Frio").first()
    matcher.match("lugar", Personas="1").first()
    
    print(actividad)
    print(clima)
    print(personas)

    
menu()
