from PyQt5 import QtWidgets, uic
import pyqtgraph as pg
import sys
from solutions import Solutions
import numpy as np

app = QtWidgets.QApplication(sys.argv)


class Values:

    def __init__(self, window):
        self.equation = lambda x, y: (y ** 2 - y) / x
        self.x0 = int(window.x0.value())
        self.y0 = window.y0.value()
        self.X = int(window.X.value())
        self.n = int(window.GridSize.value())
        self.n_start = int(window.NStart.value())
        self.n_finish = int(window.NFinish.value())

    def get_plot_points(self, method):
        method_solution = method(self)
        exact = Solutions.exact_solution(self)
        method_error = exact[0], np.abs(method_solution[1] - exact[1])
        return method_solution, method_error


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('mainwindow.ui', self)

        self.update.clicked.connect(self.plot_new_graphs)

        self.ExactSolutions.setTitle("Solutions", color='000', size='25pt')
        self.ExactSolutions.setLabel('left', 'y', color='000', **{'font-size': '25pt'})
        self.ExactSolutions.setLabel('bottom', 'x', color='000', **{'font-size': '25pt'})

        self.Errors.setTitle("Local Errors", color='000', size='25pt')
        self.Errors.setLabel('left', 'Local Error', color='000', **{'font-size': '25pt'})
        self.Errors.setLabel('bottom', 'x', color='000', **{'font-size': '25pt'})

        self.GlobalErrors.setTitle("Global Errors", color='000', size='25pt')
        self.GlobalErrors.setLabel('left', 'Global Error', color='000', **{'font-size': '25pt'})
        self.GlobalErrors.setLabel('bottom', 'N', color='000', **{'font-size': '25pt'})

        self.plot_new_graphs()

    def plot(self, graph, hour=None, temperature=None, color=None, name=None):
        # if initial values were not specified  set them empty
        if hour is None or temperature is None:
            hour, temperature, color = [], [], (255, 0, 0)

        graph.setBackground('w')
        graph.showGrid(x=True, y=True)

        pen = pg.mkPen(color=color, width=5)
        graph.plot(hour, temperature, pen=pen, name=name)

    def plot_new_graphs(self):
        values = Values(self)
        self.clear_graphs()

        self.ExactSolutions.addLegend()
        self.Errors.addLegend()
        self.GlobalErrors.addLegend()

        self.ExactSolutions.enableAutoRange()
        self.Errors.enableAutoRange()
        self.GlobalErrors.enableAutoRange()

        # Global Error
        x, y = Solutions.global_error(values)
        self.plot(self.GlobalErrors, x, y[:, 0], color=(255, 0, 0), name="euler method")
        self.plot(self.GlobalErrors, x, y[:, 1], color=(255, 165, 0), name="improved euler method")
        self.plot(self.GlobalErrors, x, y[:, 2], color=(0, 0, 255), name="runge kutt")

        # Exact
        exact_solution = Solutions.exact_solution(values)
        self.plot(self.ExactSolutions, *exact_solution, color=(255, 0, 165), name="exact")

        # Euler
        euler_method_solution, euler_method_error = values.get_plot_points(Solutions.euler_method)
        self.plot(self.ExactSolutions, *euler_method_solution, color=(255, 0, 0), name="euler method")
        self.plot(self.Errors, *euler_method_error, color=(255, 0, 0), name="euler method error")

        # Improved Euler
        improved_euler_method_solution, improved_euler_method_error = values.get_plot_points(
            Solutions.improved_euler_method)
        self.plot(self.ExactSolutions, *improved_euler_method_solution, color=(255, 165, 0),
                  name="improved euler method")
        self.plot(self.Errors, *improved_euler_method_error, color=(255, 165, 0), name="improved euler method error")

        # Runge-Kutt
        runge_kutt_method_solution, runge_kutt_method_error = values.get_plot_points(Solutions.runge_kutt_method)
        self.plot(self.ExactSolutions, *runge_kutt_method_solution, color=(0, 0, 255), name="runge kutt")
        self.plot(self.Errors, *runge_kutt_method_error, color=(0, 0, 255), name="runge kutt error")

    def clear_graphs(self):
        # remove previous plot

        graphs = [self.ExactSolutions, self.Errors, self.GlobalErrors]
        for graph in graphs:
            legend = graph.plotItem.legend
            if legend is not None:
                legend.scene().removeItem(legend)

        for graph in graphs:
            graph.clear()
        app.processEvents()


def main():
    main = MainWindow()
    main.show()
    app.processEvents()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
