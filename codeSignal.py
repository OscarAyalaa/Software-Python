# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:40:49 2022

@author: HP
"""

""" Dada una matriz de enteros, encuentra el par de elementos adyacentes que tiene el producto más grande y devuelve ese producto.           """
from itertools import permutations 
from itertools import groupby
import re


lista = [3, 6, -2, -5, 7, 3]

def solutionMult(inputArray): 
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

#print(solutionMult(lista))

""" Dado un año, devuelva el siglo en el que se encuentra. El primer siglo abarca desde el año 1 hasta el año 100 inclusive, el segundo, desde el año 101 hasta el año 200 inclusive, etc.  """

def solutionYear(year):
    if year <= 0:
        return 0
    
    elif year <= 100:
        return 1
    
    elif year % 100 == 0:
        return int(year/100)
    
    else:
        return int((year/100)+1)


#print(solutionYear(1001)) 


"""  comprobar un palindromo  """


def solutionPalindromo(palindromo):
    fin = len(palindromo)-1
    inicio = 0
    
    while inicio < fin:
        if palindromo[inicio] != palindromo[fin]:
            return False
        inicio = inicio + 1
        fin = fin-1
        
    return True
    
#print(solutionPalindromo("oso"))


"""  calcular el número mínimo de estatuas adicionales necesarias, cada estatua debe ser mas grande que la anterior por 1   """

arrayStatues = [6, 2, 3, 8]

def solutionStatues(statues):
    #return max(statues) - min(statues) - len(statues) + 1  "mejor respuesta"
    r = 0
    statues.sort()
    
    for num in range(len(statues)-1):
        c = statues[num]
        if statues[num] < statues[num + 1]:
            while c + 1 < statues[num +1]:
                r = r + 1
                c = c + 1
    return r

#print(solutionStatues(arrayStatues))


""" Dada una secuencia de enteros como un arreglo, determine si es posible obtener una secuencia estrictamente creciente eliminando no más de un elemento del arreglo. """

sequence = [1, 3, 2, 1]

def solutionSequence(sequence):
    fails1 = 0
    fails2 = 0
    
    for i in range(len(sequence)-1):
            if sequence[i] >= sequence[i+1]:
                fails1 = fails1 + 1
                
    for i in range(len(sequence)-2):
            if sequence[i] >= sequence[i+2]:
                fails2 = fails2 + 1
                
    if (fails1 < 2) and (fails2 < 2):
                
        return True
    else:
        return False 
    

#print(solutionSequence(sequence))



""" Dada una matriz, contar los numeros diferentes de cero, con la condicion de que encima de los numeros no haya ningun cero  """

matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

#print(len(matrix))
#print(len(matrix[0]))
#

def cuartosF(matrix):
    coast  = 0
    
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j]!=0:
                coast+=matrix[i][j]
            else:
                break
            
    return  coast

        
#print("mi maldita prueba: "+str(cuartosF(matrix)))

""" dado un arreglo de strings, regresa otro arreglo de strings que contenga los strings mas largos """

inputArray = ["aba", "aa", "ad", "vcd", "aba"]


def stringLargo(inputArray):
    
    outputArray = []
    tem = 0
    
    for i in range(len(inputArray)):
        
        if len(inputArray[i]) > tem:
            tem = len(inputArray[i])
    
    for i in range(len(inputArray)):
        if  len(inputArray[i]) == tem:
            outputArray.append(inputArray[i])
    
    return outputArray

#print(stringLargo(inputArray))
    

""" dado dos strings, encontrar el número de caracteres comunes entre ellos  """

s1 = "aabcc"
s2 = "adcaa"

def caraComu(s1, s2):
    
    com = [min(s1.count(i),s2.count(i)) for i in set(s1)]
    return sum(com)


#print(caraComu(s1, s2))

"""
print(min(s1.count("a"), s2.count("a")))

for i in set(s1):
    print(i)  """
    

# desglose de la operacion del metodo caraComu    
def caraComu2(s1, s2):
    com = 0
    
    for i in set(s1):
        com = [min(s1.count(i), s2.count(i))]
    
    return sum(com)

#print(caraComu(s1, s2))



""" encontrar si el ticket es de la suerte o no, la suma de primera mitad de los digitos tiene que ser igual a la suma de la segunda mitad de los digitos"""

ticket = 1230

def isLucky(ticket):
    op1 = 0
    op2 = 0
    
    numT = len(str(ticket))
    numT = int(numT/2)
    ticketS = str(ticket)
    
    mit1 = ticketS[0:numT]
    mit2 = ticketS[numT:numT+numT]
    
    for i in range(len(mit1)):
        op1 = op1 + int(mit1[i])
        
    for i in range(len(mit2)):
        op2 = op2 + int(mit2[i])
        
    if op1 == op2:
        return True
    
    else:
        return False

#print(isLucky(ticket))



""" ordenar los valores de menor a mayor sin mover la posicion de -1"""


rowPark = [-1, 150, 190, 170, -1, -1, 160, 180] 


def Height(rowPark):
    orden = []
    
    for i in rowPark:
        if i > 0:
            orden.append(i)
    
    orden.sort()
    
    for n,i in enumerate(rowPark):
        if i == -1:
            orden.insert(n, i)
    
    return orden



def HeightSolucionEficiente(a):

    l = sorted([i for i in a if i > 0])
    for n,i in enumerate(a):
        if i == -1:
            l.insert(n,i)
    return l


#print(Height(rowPark))


""" crear una función que invierta los caracteres entre paréntesis """

palabra = "(bar)"
palabra2 = "foo(bar(baz))blim"


def invertCHaracter(palabra):
    quitar = "()"
    res = ""
    
    for x in range(len(quitar)):
        palabra = palabra.replace(quitar[x], "")
    
    for i in reversed(palabra):
        res = res + i 
       
    return res



def invertCHaracter2(palabra2):
    for i in range(len(palabra2)):
        if palabra2[i] == "(":
            start = i
        if palabra2[i] == ")":
            end = i
            return invertCHaracter2(palabra2[:start] + palabra2[start+1:end][::-1] + palabra2[end+1:]) 
        
    return palabra2
    
    
#print(invertCHaracter(palabra))
#print(invertCHaracter2(palabra2))

""" se manda un arreglo donde se tiene que dividir de dos listas los elementos en posision impar en el team 1 y pares en team 2, como rsultado se tiene que dar una lista done de la suma de los elementos de los dos team"""


roWeights = [50, 60, 60, 45, 70]


def Weights(roWeights):
    
    team1 = []
    team2 = []
    res = []
    
    for i in range(len(roWeights)):
        
        if i % 2 == 0 :
            team1.append(roWeights[i])
        else:
            team2.append(roWeights[i])
            
    res.append(sum(team1))
    res.append(sum(team2))
    
    return res


#print(Weights(roWeights))



""" se obtiene una matriz rectangular, añadir un borde e asteriscos """

picture = ["abc", "ded"]



def matrizRectangular(picture):
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]


def matrizRectangular2(picture):
    l=len(picture[0])+2
    res = ["*"*l]
    
    for x in picture:
        r = x.center(l,"*")
        res.append(r)
        
    res.append("*"*l)
    return res

#print(matrizRectangular(picture))
#print()
#print(matrizRectangular2(picture))



"""  verificar si son similares las dos listas """

a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279] 


def AreSimilar(a, b):
    
    a.sort()
    b.sort()
    
    if len(a) == len(b):   
        for i in range(len(a)):
            if a[i] != b[i] :
                return False
    else:
        return False
        
    return True


def AreSimilarOptimizada(A, B):
    return sorted(A)==sorted(B) and sum([a!=b for a,b in zip(A,B)])<=2



#print(AreSimilar(a, b))


"CodeSignal ArrayChange"

chA = [-1000, 0, -2, 0]

def solution(inputArray):
    a = 0
    for i in range(1, len(inputArray)):
        if inputArray[i] <= inputArray[i - 1]:
            f = (inputArray[i - 1] - inputArray[i]) + 1
            inputArray[i] = inputArray[i - 1] + 1
            a += f
    return a


#print(solution(chA))


"palindromeRearranging: se nos da un string, revisar si reorganizando los caracteres podemos formar un palindromo"


sPalindromo = "aabb"


def palindromeRearranging(sPalindromo):
    
    letras = set(sPalindromo)
    nPalindromo = []
    op = 0
    
    for x in letras:
        l = 0
        for i in range(len(sPalindromo)):
             if x == sPalindromo[i]:
                 l = l + 1
        nPalindromo.append(l)    
    
    for j in range(len(nPalindromo)):
        
        if nPalindromo[j] % 2 != 0:
            op = op + 1     
    
    if op > 1:
        return False
        
    return True


#print(palindromeRearranging(sPalindromo))

""" Descubrir si tienen la misma fuerza  """

yourLeft = 15
yourRight = 10

friendsLeft = 15
friendsRight = 9


def brazoFuerza(yourLeft, yourRight, friendsLeft, friendsRight):
    
    if (yourLeft == friendsLeft and yourRight == friendsRight):
        
        return True
    
    elif (yourLeft == friendsRight and yourRight == friendsLeft):
        
        return True
    
    else:
        
        return False


def brazoFuerzaOptimo(yourLeft, yourRight, friendsLeft, friendsRight):
    return {yourLeft, yourRight} == {friendsLeft, friendsRight}



#print(brazoFuerza(yourLeft, yourRight, friendsLeft, friendsRight))



"""  diferencia maxima absoluta entre dos de sus elementos abyacentes  """


diferenciaM = [2, 4, 1, 0]


def DiferenciaMaxima(diferenciaM):
    
    dif = 0
    
    for i in range(len(diferenciaM)-1):
        
        
        if i > 0:
            
            d = abs(diferenciaM[i] - diferenciaM[i - 1])
            
            if d > dif:
                
                dif = d
            
            d = abs(diferenciaM[i] - diferenciaM[i + 1])
            
            if d > dif:
                
                dif = d
                 
    return dif


#print(DiferenciaMaxima(diferenciaM))


""" Dada una cadena, averigüe si cumple con las reglas de nomenclatura de direcciones IPv4. """


ip = "172.16.254.00"


def DireccionIPv4(ip):
    IPv4 = ip.split('.')
    
    print(IPv4[1][0])
    
    
    for i in range(len(IPv4)):
        for j in range(99):
            if (IPv4[i] == "0"+str(j)):
                return False
        
        if len(IPv4) != 4:
        
            return False
        
        if IPv4[i] == "":
            
            return False     
        
        try:
            if int(IPv4[0]) < 0 or int(IPv4[0]) > 223:
            
             return False
        
            if int(IPv4[i]) < 0 or int(IPv4[i]) > 255:
            
             return False
        
        except Exception:
            
            return False
        

    return True


def DireccionIPv4Optim(inputString):
    l = inputString.split('.')
    if len(l) != 4:
        return False
    for i in range(len(l)):
        if not l[i].isnumeric():
            return False
        elif (len(l[i]) > 1) and (l[i][0] == '0'):
            return False
        elif int(l[i]) not in range(256):
            return False
    return True


#print(DireccionIPv4(ip))
#print(DireccionIPv4Optim(ip))



"el minimo tamaño de salto para evitar los obstaculos"

obstaculos = [5, 3, 6, 7, 9]


def avoidObstacles(obs):
    
    # sort the list in ascending order
    obs = sorted(obs)
     
    # set jump distance to 1
    jump_dist = 1
     
    # flag to check if current jump distance
    # hits an obstacle
    obstacle_hit = True
    while(obstacle_hit):
         
 
        obstacle_hit = False
        jump_dist += 1
         
        # checking if jumping with current length
        # hits an obstacle
        for i in range(len(obs)):
            if obs[i] % jump_dist == 0:
                 
                # if obstacle is hit repeat process
                # after increasing jump distance
                obstacle_hit = True
                break
 
    return jump_dist


#print(avoidObstacles(obstaculos))


"Aplicar el algoritmo boxBlur"


image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]

def square_matrix(square):
	""" This function will calculate the value x
	(i.e. blurred pixel value) for each 3 * 3 blur image.
	"""
	tot_sum = 0
	
	# Calculate sum of all the pixels in 3 * 3 matrix
	for i in range(3):
		for j in range(3):
			tot_sum += square[i][j]
			
	return tot_sum // 9	 # return the average of the sum of pixels

def boxBlur(image):
	"""
	This function will calculate the blurred
	image for given n * n image.
	"""
	square = []	 # This will store the 3 * 3 matrix
				# which will be used to find its blurred pixel
				
	square_row = [] # This will store one row of a 3 * 3 matrix and
					# will be appended in square
					
	blur_row = [] # Here we will store the resulting blurred
					# pixels possible in one row
					# and will append this in the blur_img
	
	blur_img = [] # This is the resulting blurred image
	
	# number of rows in the given image
	n_rows = len(image)
	
	# number of columns in the given image
	n_col = len(image[0])
	
	# rp is row pointer and cp is column pointer
	rp, cp = 0, 0
	
  
	# This while loop will be used to
	# calculate all the blurred pixel in the first row{}
	while rp <= n_rows - 3:
		while cp <= n_col-3:
            
			
			for i in range(rp, rp + 3):
				
				for j in range(cp, cp + 3):
					
					# append all the pixels in a row of 3 * 3 matrix
					square_row.append(image[i][j])
				# append the row in the square i.e. 3 * 3 matrix
				square.append(square_row)
				square_row = []
			
			# calculate the blurred pixel for given 3 * 3 matrix
			# i.e. square and append it in blur_row
			blur_row.append(square_matrix(square))
			square = []
			
			# increase the column pointer
			cp = cp + 1
		
		# append the blur_row in blur_image
		blur_img.append(blur_row)
		blur_row = []
		rp = rp + 1 # increase row pointer
		cp = 0 # start column pointer from 0 again
	
	# Return the resulting pixel matrix
	return blur_img



def boxBlurOptimo(m):
    r = len(m)
    c = len(m[0])
    ans = []
    for i in range(1,r-1):
        row=[]
        for j in range(1,c-1):
            row.append(sum([m[i+k][j+l] for k in [-1,0,1] for l in [-1,0,1]])//9)
        ans.append(row)
    return ans


#print(boxBlur(image))
#print(boxBlurOptimo(image))


"busca minas indicar el numero de minas que hay alrededor, las minas se identifican con True"

mine = [[False,False,False], 
        [False,False,False]]


def Minesweeper(matrix):
    r = []
    
    for i in range(len(matrix)):
        r.append([])
        for j in range(len(matrix[0])):
            l = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]):
                        l += matrix[i+x][j+y]

            r[i].append(l)
            
    return r
                    

def MinesweeperTry(matrix):
    minas = []
    
    for i in range(len(matrix)):
        minas.append([])
        for j in range(len(matrix[0])):
            boom = 0
            
            if i == 0:
                
                if j == 0:
                    
                    if matrix[i][j+1] == True:
                        boom += 1
                    
                    if matrix[i+1][j] == True:
                        boom += 1
                    
                    if matrix[i+1][j+1] ==  True:
                        boom += 1
                
                if j == len(matrix[0])-1:
                    
                    if matrix[i][j-1] == True:
                        boom += 1
                    
                    if matrix[i+1][j-1] == True:
                        boom += 1
                    
                    if matrix[i+1][j] == True:
                        boom += 1
                
                if 0 < j < len(matrix[0])-1:
                    
                    if matrix[i][j-1] == True:
                        boom += 1
                        
                    if matrix[i][j+1] == True:
                        boom += 1
                    
                    if matrix[i+1][j-1] == True:
                        boom += 1
                    
                    if matrix[i+1][j+1] == True:
                        boom += 1
                        
                    if matrix[i+1][j] == True:
                        boom += 1
           
            
            if i == len(matrix)-1:
                
                if j == 0:
                    
                    if matrix[i][j+1] == True:
                        boom += 1
                    
                    if matrix[i-1][j] == True:
                        boom += 1
                    
                    if matrix[i-1][j+1] == True:
                        boom += 1
                        
                if j == len(matrix[0])-1:
                    
                    if matrix[i][j-1] == True:
                        boom += 1
                        
                    if matrix[i-1][j-1] == True:
                        boom += 1
                        
                    if matrix[i-1][j] == True:
                        boom += 1
                        
                if 0 < j < len(matrix[0])-1:
                    
                    if matrix[i][j-1] == True:
                        boom += 1
                        
                    if matrix[i][j+1] == True:
                        boom += 1
                    
                    if matrix[i-1][j-1] == True:
                        boom += 1
                        
                    if matrix[i-1][j+1] == True:
                        boom += 1
                    
                    if matrix[i-1][j] == True:
                        boom += 1
                    
            if 0 < i < len(matrix)-1:
                
                if j == 0:
                    
                    if matrix[i][j+1] == True:
                        boom += 1
                    
                    if matrix[i-1][j] == True:
                        boom += 1
                    
                    if matrix[i-1][j+1] == True:
                        boom += 1
                        
                    if matrix[i+1][j+1] == True:
                        boom += 1
                        
                    if matrix[i+1][j] == True:
                        boom +=1
                    
                if j == len(matrix[0])-1:
                    
                    if matrix[i][j-1] == True:
                        boom += 1
                        
                    if matrix[i-1][j-1] == True:
                        boom += 1
                        
                    if matrix[i-1][j] == True:
                        boom += 1
                        
                    if matrix[i+1][j-1] == True:
                        boom += 1
                        
                    if matrix[i+1][j] == True:
                        boom += 1
                        
                        
                if 0 < j < len(matrix[0])-1:
                    
                    if matrix[i][j-1] == True:
                        boom += 1
                        
                    if matrix[i][j+1] == True:
                        boom += 1
                    
                    if matrix[i-1][j-1] == True:
                        boom += 1
                        
                    if matrix[i-1][j+1] == True:
                        boom += 1
                    
                    if matrix[i-1][j] == True:
                        boom += 1
                        
                    if matrix[i+1][j-1] == True:
                        boom += 1
                        
                    if matrix[i+1][j+1] == True:
                        boom += 1
                        
                    if matrix[i+1][j] == True:
                        boom += 1
                    
                    
            minas[i].append(boom)
            
    return minas

#print(Minesweeper(mine))
#print(MinesweeperTry(mine))


""" remplazar los elementos del arreglo indicados por los sustitutos """

entrada = [1, 2, 1]
remplazar = 1
sustitucion = 3



def ArrayReplace(inputArray, elemToReplace, substitutionElem):
    
    resp = []
    
    for i in range(len(inputArray)):
        
        if inputArray[i] == elemToReplace:
            
            resp.append(substitutionElem)
            
        else:
            
            resp.append(inputArray[i])
    
    return resp


#print(ArrayReplace(entrada, remplazar, sustitucion))


"Comprobar si son pares"

n = 248622


def Pares(n):
    
    n = str(n)
    
    for i in range(len(n)):
        
         if int(n[i]) % 2 != 0:
             
             return False
        
    return True

#print(Pares(n))



"comprobar si el nombre de la variable es correcto, solo puede ener letras, digitos y giones bajos, pero no puede iniciar con un numero"

name = "aaa"

"Valores ASCII, letras M:65-90, m97-122, num:48-57"



def variableName(name):
    
    for i in range(len(name)):
        
        if name[0].isdigit() == True:
            
            return False
        
        if name[i] == " ":
            
            return False
        
        if (48 > ord(name[i])  or ord(name[i]) > 57 and 65 > ord(name[i])  or ord(name[i]) > 90 and ord(name[i]) != 95 and 97 > ord(name[i])  or ord(name[i]) > 122):
            
            return False

    return True


def variableNameOptim(name):
    
    return name.isidentifier()


#print(variableName(name))
#print(variableNameOptim(name))



"remplazar las letras ddel string con su siguiente letra deacuerdo al abecedario ejem: a --> b, c --> d"


abcABC = "crazy"

def alphabeticShift(abcABC):
    res = ""
    
    for i in range(len(abcABC)):
        
        if ord(abcABC[i]) == 90:
            
            res = res + res.join(chr(65))
            
        elif ord(abcABC[i]) == 122:
            
            res = res + res.join(chr(97))
            
        else:
             x = ord(abcABC[i])
        
             res = res + res.join(chr(x+1))
    
    return res

#print(alphabeticShift(abcABC))

""" Determinar si en un tablero de Ajedrez. las dos celas que se tienen son del mismo color o no"""

cell1 = "A1" 
cell2 = "H3"



def obtenerPoicion(x, y):
    
    pos = ""
    
    if x == "a":
        x = 0
    
    if x == "b":
        x = 1
    
    if x == "c":
        x = 2
    
    if x == "d":
        x = 3
        
    if x == "e":
        x = 4
    
    if x == "f":
        x = 5
    
    if x == "g":
        x = 6
    
    if x == "h":
        x = 7
    
    if y == "1":
        y = 7
    
    if y == "2":
        y = 6
    
    if y == "3":
        y = 5
    
    if y == "4":
        y = 4
        
    if y == "5":
        y = 3
    
    if y == "6":
        y = 2
    
    if y == "7":
        y = 1
    
    if y == "8":
        y = 0
    
    pos = pos.join(str(x))
    pos = pos + pos.join(str(y))
    
    return pos


def chessBoardCellColor(cell1, cell2):
    p1 = ""
    p2 = ""
    
    board = [[True, False, True, False, True, False, True, False],
             [False, True, False, True, False, True, False, True],
             [True, False, True, False, True, False, True, False],
             [False, True, False, True, False, True, False, True],
             [True, False, True, False, True, False, True, False],
             [False, True, False, True, False, True, False, True],
             [True, False, True, False, True, False, True, False],
             [False, True, False, True, False, True, False, True]]
    
    x1 = cell1[0].lower()
    y1 = cell1[1].lower()
    
    x2 = cell2[0].lower()
    y2 = cell2[1].lower()
    
    pos = obtenerPoicion(x1, y1)
    
    if board[int(pos[0])][int(pos[1])]  == True:
        
        p1 = "blanco"
        
    if board[int(pos[0])][int(pos[1])]  == False:
        
        p1 = "negro"
        
    
    pos = obtenerPoicion(x2, y2)
    
    if board[int(pos[0])][int(pos[1])]  == True:
        
        p2 = "blanco"
        
    if board[int(pos[0])][int(pos[1])]  == False:
        
        p2 = "negro"
        
        
    
    if p1 == p2:
        return True
        
    return False


#print(chessBoardCellColor(cell1, cell2))

""" Circle of Numbers """

n = 4
firstNumber = 1


def circleNumber(n, firstNumber):
    return (n / 2 + firstNumber) % n


#print(int(circleNumber(n, firstNumber)))


deposit = 100 
rate = 1
threshold = 101


""" encontrar cuantos años tardara en que el deposito supere el umbral especifico(threshold), rate es el porcectaje que aumenta el deposito por año """

def depositProfit(deposit, rate, threshold):
    year = 0
    
    while deposit < threshold:
        
         por = (deposit * rate) / 100
         
         deposit = deposit + por
         
         year += 1
    
    return year


#print(depositProfit(deposit, rate, threshold))


"""  """

Abss = [2, 3]

def absoluteValuesSumMinimization(a):
    
    resF = 0
    res = 0
    con =  0   
    
    for i in range(len(Abss)):
        aux = 0
        for x in range(len(Abss)):
            aux = aux + abs(Abss[x] - Abss[i])
            
        if i == 0:
            res = aux
        
        if aux < res:
            resF = Abss[i]
            res = aux
            
        if aux == res and con < 1:
            resF = Abss[i]
            res = aux
            con += 1
            
        
    return resF

#print(absoluteValuesSumMinimization(Abss))


"stringsRearrangement"

""" abc, abx, axx, abc  False """

""" abc, abx, axx, abx, abc     True"""

Rearrangement = ["ab", "bb", "aa"]


def comprobarRearrangement(inputArray):
    
    
    for i in range(len(inputArray)-1):
        cont = 0
        
        for x in range(len(inputArray[0])):
            
            s1 = inputArray[i]
            s2 = inputArray[i+1]
            
            if s1[x] != s2[x]:
                
                cont += 1
            
            if cont > 1:
                
                return False
                
    
    return True


def stringsRearrangement(inputArray):
    
    perm = permutations(inputArray)
    
    
    if len(inputArray) <= 2:
        
        return False
    
    
    for i in list(perm):
        
        if comprobarRearrangement(i) == True:
            
            return True
    
    
    return False



#print(stringsRearrangement(Rearrangement))


"""  """

arrayM = [2, 4, 6, 8, 10]
arrayM2 = [2, 4, 6, 8, 10]

k = 2
    
def extractEachKth(inputArray, k):
    del inputArray[k-1::k]
    return inputArray


def desgloseExtractEachKth(inputArray, k):
    res =[]
    
    for i in range(len(inputArray)):
        s = i+1
        if s % k != 0:
            res.append(inputArray[i])
        
    return res

#print(extractEachKth(arrayM, k))
#print(desgloseExtractEachKth(arrayM2, k))


""" devolver el primer digito de un string """

firstD = "var_1__Int"

def firstDigit(inputString):
    
    for i in range(len(inputString)):
        
        if inputString[i].isdigit() == True:
            
            return inputString[i]


#print(firstDigit(firstD))


""" dado un string, encontrar el numero de caracteres diferentes dentro de el """

s = "cabca"


def differentSymbolsNaive(s):
    
    caracteres = set(s)
    
    return len(caracteres)


#print(differentSymbolsNaive(s))


""" """

sumArray = [2, 3, 5, 1, 6]
nk = 4

def arrayMaxConsecutiveSum(inputArray, k):
    
    maxS = 0
    res = 0
    cont = 0
    
    
    for i in range(len(inputArray)-(k-1)):
        
        while cont < k:
            
            maxS = maxS + inputArray[i + cont]
            
            cont += 1
        
        if maxS > res:
            res = maxS
        
        maxS = 0
        cont = 0
        
    return res


#print(arrayMaxConsecutiveSum(sumArray, nk))

"""  encontrar cuantos dias son necesarios para que la planta alcance la altura deseada"""

upSpeed = 100
downSpeed = 10
desiredHeight = 910


def dia(p, upSpeed):
    
    return p + upSpeed

def noche(p, downSpeed):
    
    return p - downSpeed


def growingPlant(upSpeed, downSpeed, desiredHeight):
    
    growP = upSpeed
    Noche = 1
    Dia = 0
    cont = 1
    
    while growP < desiredHeight:
        
        if Noche == 1:
            growP = noche(growP, downSpeed)
            Noche = 0
            Dia = 0
            
        
        if Dia == 1:
            growP = dia(growP, upSpeed)
            Dia = 0
            Noche = 1
            cont += 1
        
        Dia = 1
        
        
    return cont

#print(growingPlant(upSpeed, downSpeed, desiredHeight))


"""  """

value1 = 3
weight1 = 5
value2 = 3       #3
weight2 = 8
maxW = 10


def KnapsackLight(value1, weight1, value2, weight2, maxW):
    resp = 0
    
    if value1 > value2:
        
        if weight1 <= maxW:
            
            resp = resp + value1
            maxW = maxW - weight1
            
        if weight2 <= maxW:
            
            resp = resp + value2
            maxW = maxW - weight2
    
    if value2 > value1:
        
        if weight2 <= maxW:
            
            resp = resp + value2
            maxW = maxW - weight2
        
        if weight1 <= maxW:
            
            resp = resp + value1
            maxW = maxW - weight1
    
    if value1 == value2:
        
        if weight1 <= weight2:
            
            if weight1 <= maxW:
                
                resp = resp + value1
                maxW = maxW - weight1
                
            if weight2 <= maxW:
                
                resp = resp + value2
                maxW = maxW - weight2
        
        if weight2 <= weight1:
            
            if weight2 <= maxW:
                
                resp = resp + value2
                maxW = maxW - weight2
            
            if weight1 <= maxW:
                
                resp = resp + value1
                maxW = maxW - weight1
    
    return resp


#print(KnapsackLight(value1, weight1, value2, weight2, maxW))

"""Given a string, output its longest prefix which contains only digits."""

digitLong = "12abc34"


def longestDigitsPrefix(inputString):
    
    return re.findall('^\d*',inputString)[0]


#print(longestDigitsPrefix(digitLong))


""" ssumar los digitos hasta obtener un numero de un solo digito y indicar cuantas veses se debe hacer para obtener el resultado """

nDigit = 100        
        
def sumDigit(n):
    tot = 0
    
    n = re.findall('\d', str(n))
    
    for i in n:
        tot += int(i) 

    return tot


def digitDegree(n):
    
    digitUno = n
    cont = 0
    
    if len(str(n)) == 1:
        return 0
        
    while len(str(digitUno)) >= 2:
        
        digitUno = sumDigit(digitUno)
        cont += 1
    
    return cont


#print(digitDegree(nDigit))

""" dada una posision de un alfil determinar si puede comerse al peon en un solo movimiento"""

bishop = "e7"
pawn = "a3"


def BishopandPawn(b, p):
    b=[ord(b[0]),int(b[1])]
    p=[ord(p[0]),int(p[1])]
    return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)


#print(BishopandPawn(bishop, pawn))


"""     """

stringB = "bbc"


def isBeautifulString(inputString):
    uniB = inputString.lower()
    numMax = uniB.count("a")
 
    
    for i in uniB:
        
        if ord(i) < 97 or ord(i) > 122:
            return False
    
    
    for i in range(98, 123):
        
        if numMax < uniB.count(chr(i)):
            
            return False
        
        numMax = uniB.count(chr(i))
    
    
    return True


#print(isBeautifulString(stringB))


""" substraer la parte del dominio de una direccion """

address = "\"very.unusual.@.unusual.com\"@usual.com"

def FindEmailDomain(address):
    patron = '@([A-Za-z][^ ]*)'
    res = re.findall(patron, address)
    
    return res[0]

#print(FindEmailDomain(address))


"""  """

st = "ababab"

def buildPalindrome(st):
    for i in range(0,len(st)):
        if(st[i:len(st)] == st[i:len(st)][::-1]):
            return st[0:i] + st[i:len(st)] + st[0:i][::-1]

#print(buildPalindrome(st))


"""   """

votes = [2, 3, 5, 2] 
k = 3

def ElectionsWinners(votes, k):
    win = 0
    sec = max(votes)
    
    if k == 0:
        
        if votes.count(sec) > 1:
            
            return 0
         
        if votes.count(sec) == 1:
            
            return 1
            
    
    for i in range(len(votes)):
        
        prim = votes[i] + k
        
        if prim > sec:
            
            win = win + 1
            
    return win


#print(ElectionsWinners(votes, k))

""" Ientificar si la direccion Ip es una direccion MAC-48 Address correcta """

ipE = "not a MAC-48 address"

def IsMAC48Address(ipE):
    
    ip = ipE.split("-")
    
    if len(ip) < 6 or len(ip) > 6:
        
        return False
    
    for i in range(len(ip)):
        
        if len(ip[i]) < 2 or len(ip[i]) > 2:
            
            return False
        
        for j in range(0, 2):
            
            print(ip[i][j])
            print(ord(ip[i][j]))
            
            if ord(ip[i][j]) < 48 or ord(ip[i][j]) > 57 and ord(ip[i][j]) < 65 or ord(ip[i][j]) > 70:
                
                return False
    
    return True

#print(IsMAC48Address(ipE))



""" """

line = "abbcabb"

def lineEncoding(line):
    
    s = set(line)
    res = ""
    
    for i in s:
        
        n = line.count(i)
        if n != 1:
            res = res + res.join(str(n))

        res = res + res.join(i)
        
    return res


def lineEncoding2(s):
    x = ''
    for k,g in groupby(s):
        y = len((list(g)))
        
        if y==1:
            x += k
        else:
            x += str(y) + k
    return x

#print(lineEncoding(line))
#print(lineEncoding2(line))


""" Retornar todos los movimientos posibles que puede realizar el caballo en un tablero de ajedrez desde una casilla """
"""problema chessKnigh codesignal"""
cell = "a1"

def caballoPos(c):
    x,y = ord(c[0])-96, int(c[1])
    return sum([1<=(x+i)<=8 and 1<=(y+j)<=8 for i in [-2,-1,1,2] for j in [-2,-1,1,2]])//2


def desgloseCaballoPos(c):
    
    x = ord(c[0])-96 # x a los lados
    y = int(c[1])    # y hacia arriba
    acum = 0
    print("Posicion---> x:"+str(x)+" y:"+str(y))
    
    
    for i in [-2,-1,1,2]:      # los for nos sirven para que la pieza haga todos los movimientos posibles
        for j in [-2,-1,1,2]:
            
            print("i:"+str(i)+" j:"+str(j))
            print("x+i--> "+str(x)+"+"+str(i)+"= "+str(x+i)) #mov a los lados
            print("y+j--> "+str(y)+"+"+str(j)+"= "+str(y+j)) #mov hacia arriba y abajo
            
            if 1<=(x+i)<=8 and 1<=(y+j)<=8:
                acum += 1
                print("si")
            print("------------------------------")
    
    print("numero de veces que son si: "+str(acum))  #de los resultados que salen que "si", 1 de cada 2 no es valido en el tablero de ajedrez, por eso se divide en 2
    print("movimientos validos en la posicion "+c+"("+str(x)+","+str(y)+") en el tablero: "+""+str(acum//2))
    
    return acum//2

#print(caballoPos(cell))
#print(desgloseCaballoPos(cell))

""" eliminando solo un caracter, encontrar el numero mas alto que se pueda obtener """

deltD = 152

def deleteDigit(n):
    
    n = str(n)
    resp = 0 
    
    for i in range(len(n)):
        aux = ""
        for j in range(len(n)):
            if i != j:
                aux = aux + aux.join(n[j])
            
        if int(aux) > resp:
            resp = int(aux)
            
    return resp

def deleteDigitOptimo(n):
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))

#print(deleteDigit(deltD))
#print(deleteDigitOptimo(deltD))

"""  """

text = "To be or not to be"

def longestWord(text):
    
    text = text.split(" ")
    res = ""
    aux = 0
    
    for i in range(len(text)):
        
        text[i] = text[i].strip()
        
        s = re.findall('[a-zA-Z]+', text[i])    
        
        temp = len(s[0])
    
        if temp > aux:
            
            aux = temp
            res = s[0]
    
    
    return res 
print(longestWord(text))


