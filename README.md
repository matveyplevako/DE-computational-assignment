# DE Computational Practicum
### Matvey Plevako BS18-02
#### Solurce code [GitHub](https://github.com/matveyplevako/DE-computational-assignment).

The initial conditions: ![equation](https://latex.codecogs.com/svg.latex?y%27%20%3D%20%5Cfrac%7By%5E2%20-%20y%7D%7Bx%7D), ![equation](https://latex.codecogs.com/svg.latex?y%281%29%20%3D%20%5Cfrac%7B1%7D%7B2%7D),  ![equation](https://latex.codecogs.com/svg.latex?x%20%5Cin%20%281%2C%209%29).

**Condition for x**: ![equation](https://latex.codecogs.com/svg.latex?x%20%5Cneq%200)

## Exact Solution

Rewrite the initial equation in the form of first-order nonlinear ordinary differential equation

![equation](https://latex.codecogs.com/svg.latex?y%27%20&plus;%20%5Cfrac%7B1%7D%7Bx%7D%20y%20%3D%20%5Cfrac%7B1%7D%7Bx%7D%20y%5E2)

Using substitution ![equation](https://latex.codecogs.com/svg.latex?z%20%3D%20%5Cfrac%7B1%7D%7By%7D)

![equation](https://latex.codecogs.com/svg.latex?y%20%3D%20%5Cfrac%7B1%7D%7Bz%7D%20%5Chspace%7B2em%7D%20y%27%20%3D%20-%5Cfrac%7Bz%27%7D%7Bz%5E2%7D)

![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7Bz%27%7D%7Bz%5E2%7D%20&plus;%20%5Cfrac%7B1%7D%7Bxz%7D%20%3D%20%5Cfrac%7B1%7D%7Bxz%5E2%7D)

Multiplying this by ![equation](https://latex.codecogs.com/svg.latex?z%5E2) yields

![equation](https://latex.codecogs.com/svg.latex?-z%27%20&plus;%20%5Cfrac%7B1%7D%7Bx%7Dz%20%3D%20%5Cfrac%7B1%7D%7Bx%7D)

Complementary equation:
![equation](https://latex.codecogs.com/svg.latex?-z%27%20&plus;%20%5Cfrac%7B1%7D%7Bx%7Dz%20%3D%200)

![equation](https://latex.codecogs.com/svg.latex?%5Cint%5Cfrac%7Bdz%7D%7Bz%7D%20%3D%20%5Cint%20%5Cfrac%7Bdx%7D%7Bx%7D)

![equation](https://latex.codecogs.com/svg.latex?z%20%3D%20x%20%5Ccdot%20C)

![equation](https://latex.codecogs.com/svg.latex?-C%20-x%20%5Ccdot%20C%27%20&plus;%20C%20%3D%20%5Cfrac%7B1%7D%7Bx%7D)

![equation](https://latex.codecogs.com/svg.latex?C%27%20%3D%20-%5Cfrac%7B1%7D%7Bx%5E2%7D)

![equation](https://latex.codecogs.com/svg.latex?C%20%3D%20%5Cfrac%7B1%7D%7Bx%7D%20&plus;%20C_1)

![equation](https://latex.codecogs.com/svg.latex?z%20%3D%20x%28%5Cfrac%7B1%7D%7Bx%7D%20&plus;%20C_1%29%20%5CRightarrow%20z%20%3D%201%20&plus;%20x%20%5Ccdot%20C_1)

**Exact solution** 
![equation](https://latex.codecogs.com/svg.latex?y%20%3D%20%5Cfrac%7B1%7D%7B1%20&plus;%20x%20%5Ccdot%20C%7D)

Initial value problem:
![equation](https://latex.codecogs.com/svg.latex?%5Cfrac%7B1%7D%7B2%7D%20%3D%20%5Cfrac%7B1%7D%7B1%20&plus;%20C%7D%20%5CRightarrow%20C%20%3D%201)

**Solution for the initial value problem**
![equation](https://latex.codecogs.com/svg.latex?y%20%3D%20%5Cfrac%7B1%7D%7B1%20&plus;%20x%7D)




## Software Apllication

The **main window** \
It uses layout `mainwindow.ui` that was created in PyQt Designer application
![main](https://drive.google.com/uc?authuser=0&id=1dU07Px_Y30NgNtmmCkY0h1wCvJem6GWh&export=download)

We can zoom in to get closer look at any point  \
For example, lets look at the point **(4, 0.2)**
![point](https://drive.google.com/uc?authuser=0&id=1I-grPuLMimcMPkDogZZfafgo2Y3EaSUY&export=download)

As we can see, **runge_kutt** and **exact** are very close to each other \
We can also notice that local error of **runge_kutt** is near zero

The **UML diagram**
![uml](https://drive.google.com/uc?authuser=0&id=1jkWDIiqHUwx9Pxar88H9WO87tcalr5a8&export=download)

The most important function is `plot_new`. It is used for plotting all of solutions and error graphs.

```python
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
```

Abstract form of solution function

```python
@staticmethod
def improved_euler_method(values):
    """
    :param func:    y' = f(x, y)
    :param values:  Values class
    :return:        2 lists: x and y coordinates
    """
    x0 = values.x0
    y0 = values.y0
    X = values.X
    n = values.n
    func = values.equation

    h = (X - x0) / (n - 1)

    x = numpy.linspace(x0, X, n, endpoint=True)
    y = numpy.zeros(n)
    y[0] = y0
    for i in range(n - 1):
        k1i = ...
        k2i = ...
        ...
        y[i + 1] = ...

    return x, y
```

## Local error analysis
The more slopes we consider to approximate point the lower error we get.
The lowest error:
1. Runge-Kutt
2. Improved Euler Method
3. Euler Method 


## Global error analysis
For ![equation](https://latex.codecogs.com/svg.latex?N%20%5Cin%20%5B2%2C%205%5D) errors decrease approximately quadratically
For ![equation](https://latex.codecogs.com/svg.latex?N%20%3E%205) changes in errors are less noticeable




