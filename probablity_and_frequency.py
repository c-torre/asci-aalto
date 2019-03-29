import numpy as np


def main():

    p = 0.60

    t_max = 10 ** 6

    results = np.zeros(t_max)

    for t in range(t_max):

        r = np.random.random()

        if p > r:
            results[t] = 1
        else:
            results[t] = 0

    print(np.mean(results))


if __name__ == '__main__':

    main()
