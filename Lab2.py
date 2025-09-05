# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    #variables
    h_0 = float(input("Enter inital height in meters : "))
    t = int(input("Enter time in seconds : "))
    g = 9.8
    def h(t):
      return h_0-0.5*g*t**2
    print("Height of the ball at time",t,"seconds =",h(t),"meters")

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    pass  # Replace with your code
