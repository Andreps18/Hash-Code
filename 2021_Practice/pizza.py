class Pizza:
    def __init__(self, id_nmr, ingredients, n_ingredients, used, differentElements):
        self.id_nmr = id_nmr
        self.ingredients = ingredients
        self.n_ingredients = n_ingredients
        self.used = used
        self.differentElements = differentElements
    
    def printPizzas(self):
        print(self.id_nmr, self.ingredients, self.n_ingredients)

content = open("c_many_ingredients.in", "r") #Opening the file

nPizzas, teams2, teams3, teams4 = map(int, content.readline().split() ) #Getting and assigning the number of pizzas and teams

Pizzas = [] #Getting all the possible pizzas and putting it in a list


for i in range(nPizzas):
    line = content.readline()
    line = line.split()
    Pizzas.append( Pizza(i, [x for x in line], int(line[0]), False, 0 ) )
    Pizzas[i].ingredients.pop(0)
    #n_ingredients = 
'''
print(nPizzas, teams2, teams3, teams4)
for item in Pizzas:
    item.printPizzas()
'''
def comparePizza(Pizza):
    return Pizza.n_ingredients

def scorePizza(Pizza):
    return Pizza.differentElements

Pizzas.sort(key = comparePizza, reverse=True) #Sort the pizzas by the number of ingredients, complex pizzas coming first

#print(nPizzas, teams2, teams3, teams4)
#for item in Pizzas:
#    item.printPizzas()

list_submissions = []
counter = 0
list_counter = -1

#pizzzas > pessoas      distribuir
#pizas < pessoas        resto é 3
100     24*4= 96  sobra4
3   1
pizzas-(4*teams4)>0


while counter < min(nPizzas, 2*teams2 + 3*teams3 + 4*teams4): #Stopping submissions if we run out of pizzas or teams    
    try:  
        for i in range(teams4): #Submissions must follow this scheme: team pizza_1 pizza_2
            #Sort the pizzas-
            # 
            # 
            #  by the number of ingredients, complex pizzas coming first
            Pizzas.sort(key = comparePizza, reverse=True) 
            
            list_submissions.append([4])
            list_counter += 1
            #print(list_counter)
            #for i in range(len(Pizzas)):
            for pizza in Pizzas:
                if len(list_submissions[list_counter])-1 >= list_submissions[list_counter][0]:
                    break

                if pizza.used == False:
                    list_submissions[list_counter].append(pizza)
                    counter += 1
                    pizza.used = True
                    
                    for pizza1 in Pizzas:
                        if pizza1.used  == False:
                            #comparar com pizza e alterar different elements
                            for ingredient1 in pizza1.ingredients:
                                if ingredient1 not in pizza.ingredients:
                                    pizza1.differentElements +=1
                            
                    #sort das pizzas por different elements decrescente
                    Pizzas.sort(key = scorePizza, reverse=True)   
                    
                    for pizza1 in Pizzas:
                        if pizza1.used  == False: 
                            list_submissions[list_counter].append(pizza1)  
                            pizza1.used = True
                            counter += 1
                            if len(list_submissions[list_counter])-1  >= list_submissions[list_counter][0]:
                                break

        for i in range(teams3): #Submissions must follow this scheme: team pizza_1 pizza_2
            #Sort the pizzas by the number of ingredients, complex pizzas coming first
            Pizzas.sort(key = comparePizza, reverse=True) 
            
            list_submissions.append([3])
            list_counter += 1
            #print(list_counter)
            #for i in range(len(Pizzas)):
            for pizza in Pizzas:
                if len(list_submissions[list_counter])-1 >= list_submissions[list_counter][0]:
                    break

                if pizza.used == False:
                    list_submissions[list_counter].append(pizza)
                    counter += 1
                    pizza.used = True
                    
                    for pizza1 in Pizzas:
                        if pizza1.used  == False:
                            #comparar com pizza e alterar different elements
                            for ingredient1 in pizza1.ingredients:
                                if ingredient1 not in pizza.ingredients:
                                    pizza1.differentElements +=1
                            
                    #sort das pizzas por different elements decrescente
                    Pizzas.sort(key = scorePizza, reverse=True)   
                    
                    for pizza1 in Pizzas:
                        if pizza1.used  == False: 
                            list_submissions[list_counter].append(pizza1)  
                            pizza1.used = True
                            counter += 1
                            if len(list_submissions[list_counter])-1  >= list_submissions[list_counter][0]:
                                break
           
        
        #2 PERSON TEAM
        for i in range(teams2): #Submissions must follow this scheme: team pizza_1 pizza_2
            #Sort the pizzas by the number of ingredients, complex pizzas coming first
            Pizzas.sort(key = comparePizza, reverse=True) 
            
            list_submissions.append([2])
            list_counter += 1
            #print(list_counter)
            #for i in range(len(Pizzas)):
            for pizza in Pizzas:
                if len(list_submissions[list_counter])-1 >= list_submissions[list_counter][0]:
                    break

                if pizza.used == False:
                    list_submissions[list_counter].append(pizza)
                    counter += 1
                    pizza.used = True
                    
                    for pizza1 in Pizzas:
                        if pizza1.used  == False:
                            #comparar com pizza e alterar different elements
                            for ingredient1 in pizza1.ingredients:
                                if ingredient1 not in pizza.ingredients:
                                    pizza1.differentElements +=1
                            
                    #sort das pizzas por different elements decrescente
                    Pizzas.sort(key = scorePizza, reverse=True)   
                    
                    for pizza1 in Pizzas:
                        if pizza1.used  == False: 
                            list_submissions[list_counter].append(pizza1)  
                            pizza1.used = True
                            counter += 1
                            if len(list_submissions[list_counter])-1  >= list_submissions[list_counter][0]:
                                break
                            
         
        
        """
        #4 PERSON TEAM
        for i in range(teams4): #Submissions must follow this scheme: team pizza_1 pizza_2 pizza_3 pizza_4

            list_submissions.append([4])
            list_counter += 1

            for ii in range(4):

                list_submissions[list_counter].append(Pizzas[counter])
                counter += 1

        #3 PERSON TEAM
        for i in range(teams3): #Submissions must follow this scheme: team pizza_1 pizza_2 pizza_3
            list_submissions.append([3])
            list_counter += 1

            for ii in range(3):

                list_submissions[list_counter].append(Pizzas[counter])
                counter += 1
        
        #2 PERSON TEAM
        for i in range(teams2):

            list_submissions.append([2])
            list_counter += 1

            for ii in range(2):

                list_submissions[list_counter].append(Pizzas[counter])
                counter += 1
        """
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