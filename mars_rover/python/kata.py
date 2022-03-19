direcciones = ["N", "E", "S", "W"]
current = "N"
revDir = {"N":"S", "S":"N", "E":"W", "W":"E"}

def wrap(rover):
    if rover.x > 2:
        rover.x = 0
    elif rover.x < 0:
        rover.x = 2
    elif rover.y > 2:
        rover.y = 0
    elif rover.y < 0:
        rover.y = 2


class Proxy(object):
    def __init__(self, rover, width, height):
        self.rover = rover
        self.mapWidth = width
        self.mapHeight = height
        self.obstacles = []


    def move(self, movs):
        self.rover.move(movs)

    def turn(self, d):
        if d == "l":
            self.rover.orientation = direcciones[(direcciones.index(self.rover.orientation) - 1) % 4]
        elif d == "r":
            self.rover.orientation = direcciones[(direcciones.index(self.rover.orientation) + 1) % 4]

    def wrap(self):
        if self.rover.x > self.mapWidth - 1:
            self.rover.x = 0
        elif self.rover.x < 0:
            self.rover.x = self.mapWidth - 1
        elif self.rover.y > self.mapHeight - 1:
            self.rover.y = 0
        elif self.rover.y < 0:
            self.rover.y = self.mapHeight - 1

    def addObstacle(self, x, y):
        self.obstacles.append((x, y))
    

    def checkObstacle(self, x, y):
        if x > self.mapWidth - 1:
            x = 0
        elif x < 0:
            x = self.mapWidth - 1
        elif y > self.mapHeight - 1:
            y = 0
        elif y < 0:
            y = self.mapHeight - 1

        #Uso esta versión por ser la mas común, aunque no es la más eficiente, es mas interesante el uso de diccionarios para usar su hashmap optimizado.
        #Pero en efectos de coste es igual O(1) en el mejo de los casos, O(n) en el peor de los casos.
        for o in self.obstacles:
            if x == o[0] and y == o[1]:
                return True
        return False


    def simulateMove(self, move):
        avialable = True
        obsPos = None
        if move == "f":
            if self.rover.orientation == "N":
                if self.checkObstacle(self.rover.x, self.rover.y + 1):
                    avialable = False
                    obsPos = (self.rover.x, self.rover.y + 1)
            elif self.rover.orientation == "S":
                if self.checkObstacle(self.rover.x, self.rover.y - 1):
                    avialable = False
                    obsPos = (self.rover.x, self.rover.y - 1)
            elif self.rover.orientation == "E":
                if self.checkObstacle(self.rover.x + 1, self.rover.y):
                    avialable = False
                    obsPos = (self.rover.x + 1, self.rover.y)
            elif self.rover.orientation == "W":
                if self.checkObstacle(self.rover.x - 1, self.rover.y):
                    avialable = False
                    obsPos = (self.rover.x - 1, self.rover.y)
        elif move == "b":
            if self.rover.orientation == "N":
                if self.checkObstacle(self.rover.x, self.rover.y - 1):
                    avialable = False
                    obsPos = (self.rover.x, self.rover.y - 1)
            elif self.rover.orientation == "S":
                if self.checkObstacle(self.rover.x, self.rover.y + 1):
                    avialable = False
                    obsPos = (self.rover.x, self.rover.y + 1)
            elif self.rover.orientation == "E":
                if self.checkObstacle(self.rover.x - 1, self.rover.y):
                    avialable = False
                    obsPos = (self.rover.x - 1, self.rover.y)
            elif self.rover.orientation == "W":
                if self.checkObstacle(self.rover.x + 1, self.rover.y):
                    avialable = False
                    obsPos = (self.rover.x + 1, self.rover.y)
            self.rover.move([move])
            self.wrap()
        if not avialable:
            #Reportamos el error de de encontrar un obstaculo, podría levantar una excepción, pero prefiero usar print.
            print("Error: encontrado obstaculo en (" + str(obsPos[0]) + "," + str(obsPos[1]) + "), abortando el movimiento")
            return False
        return True
                
    def move(self, movs):
        for m in movs:
            if m == "l" or m == "r":
                self.turn(m)
            else:
                if not self.simulateMove(m):
                    return False
        return True
