import random

import matplotlib.pyplot as plt
import numpy as np

alpha = 0.5  # Concentration parameter
colors = ['green', 'red', 'blue', 'orange', 'pink', 'brown', 'yellow', 'cyan']


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
    :return: {Integer numpy array} Probabilties of choosing already assigned table
    """
    # this indicates that this is the first customer
    if not table_people_map:
        # probability 0 since there are no occupied tables
        return [0]

    Z = n - 1 + alpha
    k = np.array(table_people_map)
    k = k / Z
    return k.tolist()


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
    table_cus_map = []  # Indicates how many customers occupy each table
    cur_tables = 0
    samples = []  # In the form (x-cord, y-cord, color)

    for cus in range(tot_cus):
        p_new = assign_new_table(cus + 1)
        p_occ = assign_occupied_table(cus + 1, table_cus_map)
        table_p = p_occ + [p_new]
        if cus == 0:
            table_p = [p_new]

        table_chosen = np.random.multinomial(n=1, pvals=table_p, size=1)

        table_chosen = np.argmax(table_chosen[0])

        # if new table chosen
        if table_chosen == cur_tables:
            # increment current tables
            cur_tables += 1
            # One customer added to the new table
            table_cus_map.append(1)
            # Sample dish distribution to the new table from distribution G0
            x = np.random.random_sample()
            y = np.random.random_sample()

            # Add dish distribution to table
            table_params.append((x, y))
        else:
            table_cus_map[table_chosen] += 1

        # Draw sample dishes from chosen table's dish distribution
        mean = [table_params[table_chosen][0], table_params[table_chosen][1]]
        covariance = [[0.01, 0], [0, 0.01]]
        x, y = np.random.multivariate_normal(mean, covariance)
        samples.append([x, y, table_chosen])

    return samples


def format_samples(samples):
    """
        Formats sample list into matplotlib parameters
    :param samples: samples that need to be formatted
    :return: {Dict} matplotlib friendly parameters
    """
    samples = np.array(samples)
    x = samples[:, 0]
    y = samples[:, 1]
    c = samples[:, 2].tolist()
    c = [colors[int(i)] for i in c]

    return {'x': x, 'y': y, 'color': c}


def plot_crp_distribution(samples):
    """
        Plots CRP distribution as a scatter plot
    :param samples: Samples that need to be plotted
    :return: None
    """
    params = format_samples(samples)
    plt.scatter(params['x'], params['y'], c=params['color'],  marker='o')
    plt.xticks([])
    plt.yticks([])
    plt.show()

if __name__ == '__main__':
    plot_assignments(500)
    samples = generative_model(500)
    plot_crp_distribution(samples)
