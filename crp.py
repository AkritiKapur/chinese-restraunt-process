import matplotlib.pyplot as plt
import numpy as np

alpha = 0.5  # Concentration parameter


def assign_new_table(n):
    """
    :param n: number of customers in the restraunt
    :param K: number of occupied tables
    :return: probability customer will be assigned to a new table
    """
    if n == 0:
        return 1
    else:
        return alpha / (n - 1 + alpha)


def assign_occupied_table(n, K):
    pass


def plot_assignments(tot_cus):
    x = np.arange(tot_cus)
    x = x + 1
    y = np.zeros(len(x))

    for i in range(tot_cus):
        # Probability of new table being assigned
        p_new = assign_new_table(i+1)
        y[i] = p_new

    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    plot_assignments(500)
