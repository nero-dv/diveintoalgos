import matplotlib.pyplot as plt


def ball_trajectory(x):
    # galileo's equation used to model a hypothetical ball's trajectory
    # acceleration, speed, and distance sans wind resistance and y starts at 0
    # horizontal position at time t
    # v2 is starting speed of ball on y axis
    # a represents downward acceleration due to gravity, or -9.81, where
    # ax^2 represents a free fall acceleration of 9.81 meters per second squared
    # y = (v2/v1)x + (ax^2)/(2*v1^2)
    location = (10 * x) - (5 * x**2)
    return location


def main():
    # x is the horizontal position of the ball
    x = 0
    # y is the vertical position of the ball
    y = 0
    # x_list is a list of the horizontal position of the ball
    x_list = []
    # y_list is a list of the vertical position of the ball
    y_list = []
    # while the ball is still in the air, keep updating the position of the ball
    while y >= 0:
        x_list.append(x)
        y_list.append(y)
        x += 0.1
        y = ball_trajectory(x)
    # plot the trajectory of the ball
    plt.plot(x_list, y_list)
    plt.xlabel("Horizontal Position (meters)")
    plt.ylabel("Vertical Position (meters)")
    plt.title("Ball Trajectory")
    plt.show()


if __name__ == "__main__":
    main()
