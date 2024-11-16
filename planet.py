class planet():
    mass: float
    position: tuple[float, float]
    color: tuple[int,int,int]
    radius: int
    velocity: tuple[float, float]

    def __init__(self,mass: float,position: tuple[float, float],color = (100,200,50),radius = 50,velocity = (0,0)):
        self.mass = mass
        self.position = position
        self.color = color
        self.radius = radius
        self.velocity = velocity

    def move(self, fps = 60):
        self.position = (self.position[0] + self.velocity[0]/fps,self.position[1] + self.velocity[1]/fps) 
        
def update_velocities(planets: list[planet],G:float):
    for attracted in planets:
        for attractor in planets:
            if attracted == attractor:
                pass
            else:
                update_velocity(attracted,attractor,G)
    
def update_velocity(attracted: planet, attractor: planet, G: float):
    force_modulus = (G * attracted.mass*attractor.mass)/((calculate_distance(attracted,attractor)) **(2))
    unit_vector = calculate_unit_vector(attracted,attractor)
    force = (force_modulus*unit_vector[0], force_modulus*unit_vector[1])
    attracted.velocity = (attracted.velocity[0] + force[0]/(attracted.mass*60), attracted.velocity[1] + force[1]/(attracted.mass*60))
    #print("unit vector =", unit_vector)

def calculate_distance(P1: planet,P2:planet)-> float:
    side1 = P1.position[0] - P2.position[0]
    side2 = P1.position[1] - P2.position[1]
    return ((side1)**(2)+(side2)**(2))**(1/2)

def calculate_unit_vector(attracted: planet,attractor:planet)-> tuple[float, float]:
    x_component = attractor.position[0] - attracted.position[0]
    y_component = attractor.position[1] - attracted.position[1]
    r = calculate_distance(attracted,attractor)
    return x_component/r,y_component/r