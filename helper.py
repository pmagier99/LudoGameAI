import matplotlib.pyplot as plt
from IPython import display

plt.ion()


def plot_stats(a, b, c, d, e, f, g, h):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()

    plt.subplot(2, 4, 1)
    plt.plot(a, color="yellow")
    plt.title('Yellow good dec')

    plt.subplot(2, 4, 2)
    plt.plot(b, color="red")
    plt.title('Red good dec')

    plt.subplot(2, 4, 3)
    plt.plot(c, color="green")
    plt.title('Green good dec')

    plt.subplot(2, 4, 4)
    plt.plot(d, color="blue")
    plt.title('Blue good dec')

    plt.subplot(2, 4, 5)
    plt.plot(e, color="yellow")
    plt.title('Yellow bad dec')

    plt.subplot(2, 4, 6)
    plt.plot(f, color="red")
    plt.title('Red bad dec')

    plt.subplot(2, 4, 7)
    plt.plot(g, color="green")
    plt.title('Green bad dec')

    plt.subplot(2, 4, 8)
    plt.plot(h, color="blue")
    plt.title('Blue bad dec')
    plt.show()
    plt.pause(.1)
    plt.savefig('plots/plot_10000games.png')
