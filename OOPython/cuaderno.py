import datetime

# guarde el proximo id
ultimoId = -1

class Nota:
    ''' representa una nota en el cuaderno. Se implementa un algoritmo 
        de busqueda y almacena etiqueta para cada nota  '''

    def __init__(self, memo, etiqueta=''):
        ''' inicializa la note con un memo y etiqueta opcionales
        separadas por espacios. Automaticamente crea un id unico para la nota '''


        self.memo = memo
        self.etiqueta = etiqueta
        self.fechaDeCreado = datetime.date.today()
        global ultimoId
        ultimoId += 1
        self.id = ultimoId

    def casa(self, filtro):
        ''' Determina si la nota casa con el filtro.
        Retorna True si casa, Falso si no casa
        La busqueda es sensible a las mayusculas o minusculas '''
        return filtro in self.memo or filtro in self.etiqueta 


class Cuaderno:
    ''' Representa una colleccion de notas con etiqueta que
    se pueden modificar '''

    def __init__(self):
        ''' inicialice el cuaderno con una lista vacia '''
        self.notas = []
        return

    def notaNueva(self, memo, etiqueta=''):
        ''' crea una nueva nota y la agrega a la lista '''
        self.notas.append(Nota(memo, etiqueta)) # composition
        return

    def modifiqueMemo(self, notaId, memo):
        ''' Encuentre la nota por el id y cambie el memo '''
        for nota in self.notas :
             if nota.id == notaId:
                 nota.memo = memo
                 break
        return

#   def modifiqueEtiqueta( self, notaId, etiqueta):
#       ''' encuentre la nota con el id y cambien la etiqueta '''
#       for nota in self.notas:
#           if nota.id == notaId:
#               nota.etiqueta == etiqueta
#               break
#
#        return
#

    def modifiqueEtiqueta( self, notaId, etiqueta):
        self.encuentreNota(notaId).etiqueta = etiqueta
        return

    def busque(self, filtro):
        ''' encuentre las notas que casan con el filtro '''
        return [nota for nota in self.notas if nota.casa(filtro)]

    def encuentreNota(self, id):
        ''' encuentre nota basado en la identificaion id '''
        for nota in self.notas:
            if nota.id == id:
                return nota

        print("no se encontro la nota %d" %(id))
        return None

    def imprimaNotas(self):
        for nota in self.notas:
            print(vars(nota))









