class metodos:
    """Comentartios de clase
        aqui se crearon metodos para practicar 
        la documentacion de metodos y clases"""
        
    
    def suma(numa, numb):
        
        """ Esta función realiza la suma de 
            do números cualera, ya sean
            enteros o reales"""
        
        #aqui aplicamos lo de las pruebas
    
        """
        Sumará dos números
        >>> suma(5,5)
        10
        """   
        
        return numa+numb
         

    print(suma(20, 3.4))

    #aqui imprimimos la documentacion del método

    print(suma.__doc__)

#usando help
help(metodos.suma)

help(metodos)