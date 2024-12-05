import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=15,
    )
    ax.set_aspect("equal")

    ax.plot(rw.x_values, rw.y_values, linewidth=1, c="gray")

    # Emphasize the first and last points.
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)
    ax.annotate("Start", (0, 0), weight="bold", fontsize=12)
    ax.annotate("End", (rw.x_values[-1], rw.y_values[-1]), weight="bold", fontsize=12)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
