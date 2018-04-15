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


def assign_occupied_table(n, table_people_map):
    """
    :param n: number of customers in the restraunt
    :param table_people_map: people at each table.
    :return: Probabilties of choosing already assigned table
    """
    # this indicates that this is the first customer
    if not table_people_map:
        # probability 0 since there are no occupied tables
        return 0

    Z  = n - 1 + alpha
    k = np.array(table_people_map)
    k = k / Z
    return k


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


def generative_model(tot_cus):
    table_params = []  # Param for table 1 would be at index 0, 2 at index 1 and so on.
    table_cus_map = [] # Indicates how many customers occupy each table

    for cus in range(tot_cus):
        pass


if __name__ == '__main__':
    plot_assignments(500)
