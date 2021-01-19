class Pizza:
    def __init__(self, id_nmr, ingredients, n_ingredients):
        self.id_nmr = id_nmr
        self.ingredients = ingredients
        self.n_ingredients = n_ingredients
    
    def printPizzas(self):
        print(self.id_nmr, self.ingredients, self.n_ingredients)

content = open("e_many_teams.in", "r")

nPizzas, teams2, teams3, teams4 = map(int, content.readline().split() )

Pizzas = []

for i in range(nPizzas):
    line = content.readline()
    line = line.split()
    Pizzas.append( Pizza(i, [x for x in line], int(line[0])) )
    Pizzas[i].ingredients.pop(0)
    #n_ingredients = 
'''
print(nPizzas, teams2, teams3, teams4)
for item in Pizzas:
    item.printPizzas()
'''
def comparePizza(Pizza):
    return Pizza.n_ingredients

Pizzas.sort(key = comparePizza, reverse=True)

#print(nPizzas, teams2, teams3, teams4)
#for item in Pizzas:
#    item.printPizzas()

list_submissions = []
counter = 0
list_counter = -1

while counter < len(Pizzas):
    try:
        #2 PERSON TEAM
        for i in range(teams2):

            list_submissions.append([2])
            list_counter += 1

            for ii in range(2):

                list_submissions[list_counter].append(Pizzas[counter])
                counter += 1

        #3 PERSON TEAM
        for i in range(teams3):
            list_submissions.append([3])
            list_counter += 1

            for ii in range(3):

                list_submissions[list_counter].append(Pizzas[counter])
                counter += 1

        #4 PERSON TEAM
        for i in range(teams4):

            list_submissions.append([4])
            list_counter += 1

            for ii in range(4):

                list_submissions[list_counter].append(Pizzas[counter])
                counter += 1
    except:
        continue
######################################################8===========D


if list_submissions[-1][0] != len(list_submissions[-1]) - 1:
    list_submissions.pop()


output = open("output", "w")
output.write(str(len(list_submissions)) + "\n")
for item in list_submissions:
#    if item[0] != len(item) - 1:
#        break
    for subitem in item:
        try:
            output.write(str(subitem.id_nmr) + " ")
        except:
            output.write(str(subitem) + " ")
    output.write("\n")

content.close()
output.close()