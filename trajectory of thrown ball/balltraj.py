import matplotlib.pyplot as plt

def ball_trajectory(x):
    # galileo's equation used to model a hypothetical ball's trajectory
    # acceleration, speed, and distance sans wind resistance and y starts at 0
    # horizontal position at time t
    # v2 is starting speed of ball on y axis
    # a represents downward acceleration due to gravity, or -9.81, where 
    # ax^2 represents a free fall acceleration of 9.81 meters per second squared
    # y = (v2/v1)x + (ax^2)/(2*v1^2)
    location = (10 * x) - (5* x**2)  
    return location

# "Gravity's Rainbow" - Thomas Pynchon
xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]
plt.plot(xs, ys)
plt.title('The Trajectory of a Thrown Ball')
plt.xlabel('Horizontal Position of Ball')
plt.ylabel('Vertical Position of Ball')
plt.axhline(y = 0)
plt.show()

