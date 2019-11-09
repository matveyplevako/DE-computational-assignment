import numpy as np
import copy


class Solutions:

    @staticmethod
    def euler_method(values):
        """
        :param func: y' = f(x, y)
        :param values:   Values class
        :return:     2 lists: x and y coordinates
        """
        x0 = values.x0
        y0 = values.y0
        X = values.X
        n = values.n
        func = values.equation

        h = (X - x0) / (n - 1)

        x = np.linspace(x0, X, n, endpoint=True)
        y = np.zeros(n)
        y[0] = y0
        for i in range(n - 1):
            y[i + 1] = y[i] + h * func(x[i], y[i])
        return x, y

    @staticmethod
    def exact_solution(values):
        """
        :param func: y' = f(x, y)
        :param values:   Values class
        :return:     2 lists: x and y coordinates
        """
        x0 = values.x0
        X = values.X
        n = values.n

        x = np.linspace(x0, X, n, endpoint=True)
        y = np.zeros(n)
        for ind, xi in enumerate(x):
            y[ind] = 1 / (xi + 1)

        return x, y

    @staticmethod
    def improved_euler_method(values):
        """
        :param func: y' = f(x, y)
        :param values:   Values class
        :return:     2 lists: x and y coordinates
        """
        x0 = values.x0
        y0 = values.y0
        X = values.X
        n = values.n
        func = values.equation

        h = (X - x0) / (n - 1)

        x = np.linspace(x0, X, n, endpoint=True)
        y = np.zeros(n)
        y[0] = y0
        for i in range(n - 1):
            k1i = func(x[i], y[i])
            k2i = func(x[i] + h, y[i] + h * k1i)
            y[i + 1] = y[i] + h / 2 * (k1i + k2i)

        return x, y

    @staticmethod
    def runge_kutt_method(values):
        """
        :param func: y' = f(x, y)
        :param values:   Values class
        :return:     2 lists: x and y coordinates
        """
        x0 = values.x0
        y0 = values.y0
        X = values.X
        n = values.n
        func = values.equation

        h = (X - x0) / (n - 1)

        x = np.linspace(x0, X, n, endpoint=True)
        y = np.zeros(n)
        y[0] = y0
        for i in range(n - 1):
            k1i = func(x[i], y[i])
            k2i = func(x[i] + h / 2, y[i] + h / 2 * k1i)
            k3i = func(x[i] + h / 2, y[i] + h / 2 * k2i)
            k4i = func(x[i] + h, y[i] + h * k3i)
            y[i + 1] = y[i] + h / 6 * (k1i + 2 * k2i + 2 * k3i + k4i)

        return x, y

    @staticmethod
    def global_error(values1):
        values = copy.copy(values1)
        n_start = values.n_start
        n_finish = values.n_finish

        x = []
        y = []

        for n in range(n_start, n_finish + 1):
            values.n = n
            x.append(n)

            exact = Solutions.exact_solution(values)[1]
            y.append([
                np.sum(np.abs(Solutions.euler_method(values)[1] - exact)),
                np.sum(np.abs(Solutions.improved_euler_method(values)[1] - exact)),
                np.sum(np.abs(Solutions.runge_kutt_method(values)[1] - exact)),
            ])

        return x, np.array(y)
