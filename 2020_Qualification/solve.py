content = open("a_example.txt", "r")

books = content.read(1) #Line 1
content.read(1)
nLibraries = int(content.read(1))
content.read(1)
days_for_scanning = int(content.read(1))
content.read(2)
scores = content.readline().split() #Line 2

class livraria():
    def __init__(self, nBooks, signup, ship, books):
        self.signup = signup
        self.ship = ship
        self.books = books
        self.nBooks = nBooks 
    def printLibrary(self):
        print("nBooks:", self.nBooks, "signup:", self.signup, "ship:", self.ship, "books:", self.books)

#content.read(1)   

libraries = []

for i in range(nLibraries): #criar n livrarias
    libraries.append( livraria( 0, 0 , 0 , 0) )
    
    libraries[i].nBooks = int( content.read(1) )
    content.read(1)

    libraries[i].signup = int( content.read(1) )
    content.read(1)
    
    libraries[i].ship = int( content.read(1) )
    content.read(1)
    
    libraries[i].books = content.readline().split()
    
for lib in libraries:
    lib.printLibrary()