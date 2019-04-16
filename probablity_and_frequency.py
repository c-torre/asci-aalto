import numpy as np


def main():

    p = 0.60

    t_max = 10 ** 6

    results = np.zeros(t_max)

    for t in range(t_max):

        results[t] = int(p > np.random.random())
        # Do the same as:
        # r = np.random.random()
        # if p > r:
        #     results[t] = 1
        # else:
        #     results[t] = 0

        # results[t] =

    print("Theoretical probability", p)
    print("Frequency:", np.mean(results))


if __name__ == '__main__':

    main()
