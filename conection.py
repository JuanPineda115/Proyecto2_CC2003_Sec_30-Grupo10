from py2neo import Graph, NodeMatcher

grafo = Graph("bolt://localhost:7687", auth=("neo4j","1234"), encrypted=False)
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


    response = matcher.match("lugar", Actividades="Aventuras")
    matcher.match("lugar", Clima="Frio")
    matcher.match("lugar", Personas="Solo")
    
    
    print(" ")
    print(response)
    print(actividad)
    print(clima)
    print(personas)

    
menu()
