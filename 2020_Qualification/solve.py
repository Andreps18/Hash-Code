
class livraria():
    def __init__(self, nBooks, signup, ship, books, id):
        self.id = id
        self.signup = signup
        self.ship = ship
        self.books = books
        self.nBooks = nBooks 
    def printLibrary(self):
        print("id:", self.id, "nBooks:", self.nBooks, "signup:", self.signup, "ship:", 
            self.ship, "books:")
        for book in self.books:
            book.printBook()

class Book():
    def __init__(self, number, score):
        self.number = number
        self.score = score
    def printBook(self):
        print(self.number, self.score)

def compareBookScores(book):
    return book.score

def compareLibraries(library):
    return library.signup

content = open("a_example.txt", "r")

books, nLibraries, days_for_scanning = map(int, content.readline().split() )

#print(books, nLibraries, days_for_scanning)

scores = content.readline().split() #Line 2

for i in range(len(scores)):
    scores[i] = int(scores[i])

print("Book scores:", scores)

libraries = []

for i in range(nLibraries): #criar n livrarias
    libraries.append( livraria( 0, 0 , 0 , [], 0) )
    
    #identificar a livraria
    libraries[i].id = i

    libraries[i].nBooks = int( content.read(1) )
    content.read(1)

    libraries[i].signup = int( content.read(1) )
    content.read(1)
    
    libraries[i].ship = int( content.read(1) )
    content.read(1)
    
    #libraries[i].books = content.readline().split()
    #libraries[i].books.sort()
    
    temp = content.readline().split()
    for nmr_book in temp:
        libraries[i].books.append( Book( int(nmr_book), scores[ int(nmr_book) ] ) )
    
    #ordenar de acordo com a pontuacao, livro com mais pontos esta no fim
    libraries[i].books.sort(key = compareBookScores)
    
    ''' 
    temp_dict = {}
    for j in range(len(libraries[i].books)):
        temp_dict[scores[j]] = libraries[i].books[j]
    del temp_dict(6)
    libraries[i].books = temp_dict
    print("correspondent book:", libraries[i].books[max(libraries[i].books)], "max points:", max(libraries[i].books))
    '''

libraries.sort(key = compareLibraries)

for lib in libraries:
    lib.printLibrary()

content.close()