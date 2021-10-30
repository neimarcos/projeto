# Import PuLP modeler functions
from pulp import *
import matplotlib.pyplot as plt
import networkx as nx


# Creates a list of all the supply nodes
Routes = ["A", "B", "C","D", "E","F"]

# Creates a dictionary for the number of units of supply for each supply node
supply = {"A": 2,
          "B": 3,
          "C": 4,
          "D": 2,
          "E": 3,
          "F": 4,}

# Creates a list of all demand nodes
Probes = ["AB", "AF", "BC", "BF", "CD", "CE","CF","DE","EF"]

# Creates a dictionary for the number of units of demand for each demand node
demand = {"AB": 1,
          "AF": 1,
          "BC": 1,
          "BF": 1,
          "CD": 1,
          "CE": 1,
          "CF": 1,
          "DE": 1,
          "EF": 1,}



# Creates a list of costs of each  path
custo_sonda = [   #Probes
         #"AB", "AF", "BC", "BF", "CD", "CE","CF","DE","EF"
         [2,2,0,0,0,0,0,0,0],#A   routes
         [3,0,3,3,0,0,0,0,0],#B
         [0,0,4,0,4,4,4,0,0],#C
         [0,0,0,0,2,0,0,2,0],#D
         [0,0,0,0,0,3,0,3,3],#E
         [0,4,0,4,0,0,4,0,4],#F
         ]

# Capacidade de processamento disponivel 
#       A  B   C   D   E   F  
CPU = [45,70, 46, 67, 20, 20 ],#A   routes
Carga_Maxima=60

#  path
Links = [   #Links ativo
         #"AB", "AF", "BC", "BF", "CD", "CE","CF","DE","EF"
         [1,1,0,0,0,0,0,0,0],#A   routes
         [1,0,1,1,0,0,0,0,0],#B
         [0,0,1,0,1,1,1,0,0],#C
         [0,0,0,0,1,0,0,1,0],#D
         [0,0,0,0,0,1,0,1,1],#E
         [0,1,0,1,0,0,1,0,1],#F
         ]

# Desvendando a matemática com Python #5
def CargaCPU(Sondas, CargaCPU):
    C = []
    #verificar se A e B tem a mesma
    nLinhasSondas = len(Sondas)
    nColSondas, nCargaCPU = len(Sondas[0]), len(CargaCPU[0])
    linha = [0]*nCargaCPU
    C.append(linha)
    for i in range(nLinhasSondas):
      somacustosoma=0;
      for j in range(nColSondas):
        somacustosoma +=  Sondas[i][j]
      C[0][i] = somacustosoma + CargaCPU[0][i]
    return C

# The cost data is made into a dictionary
costs = makeDict([Routes,Probes],custo_sonda,0)
#print (costs)
# Creates the 'prob' variable to contain the problem data
prob = LpProblem("Probes Placement Problem",LpMinimize)


# Creates a list of tuples containing all the possible probes 
#possible_probes = [(w,b) for w in Routes for b in Probes]
#print (possible_probes)
possible_probes = []
possible_probes = [('A','AB'),('A','AF'),('B','AB'),('B','BC'),('B','BF'),('C','BC'),('C','CD'),('C','CE'),('F','EF'),('C','CF'),('D','CD'),('D','DE'),('E','CE'),('E','DE'),('E','EF'),('F','AF'),('F','BF'),('F','CF')]


#print (possible_probes)

#print (possible_probes)
# A dictionary called 'Vars' is created to contain the referenced variables(the routes)
vars = LpVariable.dicts("Route",(Routes,Probes),0,None,LpInteger)

# The objective function is added to 'prob' first
#tmp1 = lpSum([vars[w][b]*costs[w][b] for (w,b) in possible_probes])
#tmp2 = lpSum([vars[w][b]*costs[w][b] for (w,b) in possible_probes])
prob +=  lpSum([vars[w][b]*costs[w][b] for (w,b) in possible_probes]), "Sum_of_Measurement_Costs"


#Restrição de sondas por roteador <= número de links
for w in Routes:
    Probes_in_Route = []
    somasondas=0
    for j in range(9):
      if (Links[Routes.index(w)][j] > 0): 
        Probes_in_Route.append(Probes[j])
    prob += lpSum([vars[w][b] for b in Probes_in_Route])<=supply[w], "Sum_of_Probes_out_of_route_%s"%w

# Restrição de sondas por link = 1
for b in Probes:
    Probes_in_Route = []
    for j in range(6):
      if (Links[j][Probes.index(b)] > 0): 
        Probes_in_Route.append(Routes[j])
    prob += lpSum([vars[w][b] for w in Probes_in_Route])==demand[b], "Sum_of_Products_into_Link%s"%b


#Carga_CPU_Com_medicao=CargaCPU(custo_sonda,CPU)
#Restrição de sondas por roteador <= número de links
for w in Routes:
    Probes_in_Route = []
    somasondas=0
    for j in range(9):
      if (Links[Routes.index(w)][j] > 0): 
        somasondas+=Links[Routes.index(w)][j] * custo_sonda[Routes.index(w)][j]
    prob += somasondas <= Carga_Maxima, "Sum_of_Carga_out_of_route_%s"%w

print(prob)
# The problem data is written to an .lp file
prob.writeLP("ProbesPlacement.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    #if v.varValue > 0:
      print(v.name, "=", v.varValue)

# The optimised objective function value is printed to the screen    
print("Total Cost = ", value(prob.objective))


