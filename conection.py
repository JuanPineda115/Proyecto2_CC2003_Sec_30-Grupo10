from py2neo import Graph, NodeMatcher

grafo = Graph("bolt://localhost:7687", auth=("neo4j","1234"))
matcher = NodeMatcher(grafo)


def menu():
    
    print ("      ----------------------------------------------")
    print ("      ----------------------------------------------")
    print ("            RECOMENDACION DE LUGARES TURÍSTICOS  \n")
    
    print (" -- ACTIVIDADES: \n")
    print ("   - Aventuras ")
    print ("   - Deportes Extremos ")
    print ("   - Recreacion \n")
    actividad = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto (escriba la opcion tal y como aparece, sin '-'): ")


    print (" -- CLIMAS: \n")
    print ("   - Frio")
    print ("   - Calido ")
    print ("   - Templado \n")
    clima = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto (escriba la opcion tal y como aparece, sin '-'): ")


    print (" -- NÚMERO DE PERSONAS: \n")
    print ("   - Grupos")
    print ("   - Parejas ")
    print ("   - Solo ")
    print ("   - Familia \n")
    personas = input (" - De las opciones anteriores, escoja la que más se adecue a su gusto (escriba la opcion tal y como aparece, sin '-'): ")


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
    matcher.match("lugar", Personas="Solo").first()
    
    print(actividad)
    print(clima)
    print(personas)

    
menu()
