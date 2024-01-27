
# In Python, a variable or other reference has no intrinsic type.##

# Garbage Collector
''' 
    Significa que removera de la memoria el objeto
    Reclama espacio en memoria
'''

# Counter Reference
''' 
    Si un objeto es referenciado el contador va incrementando
    Si es liberado el contador va decrementando
    todos los objetos nacen con un contador
'''


# Strong Reference
''' 
    Un Objeto puede tener mas de una referencia del tipo Strong
    Si se declara como Strong Reference, este evita que sea removido de la memoria
'''



# Weak Reference
''' 
    Significa que que removera de la memoria el objeto
    Si se declara como Weak Reference, este puede ser removido de la memoria
    Weak reference no protege al objeto

     * weak dictionaries
     * Caches

     weakref, es un modulo externo si lo deseas manejar por tu cuenta.
     Crea objetos del tipo weak reference.
     import weakref

     WeakKeyDictionary
     WeakValueDictionary

'''


