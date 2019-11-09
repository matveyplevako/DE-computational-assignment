# DE Computational Practicum
### Matvey Plevako BS18-02
#### Solurce code [GitHub](https://github.com/matveyplevako/DE-computational-assignment).

The initial conditions: $y' = \frac{y^2 - y}{x}$,  $y(1) = \frac{1}{2}$,  $x \in (1, 9)$.

**Condition for x**: $x \neq 0$

## Exact Solution

Rewrite the initial equation in the form of first-order nonlinear ordinary differential equation

<img src="https://latex.codecogs.com/svg.latex?y' + \frac{1}{x} y = \frac{1}{x} y^2" />

\
Using substitution <img src="https://latex.codecogs.com/svg.latex?z = \frac{1}{y}" />


<img src="https://latex.codecogs.com/svg.latex?y = \frac{1}{z} \hspace{2em} y' = -\frac{z'}{z^2}" />

\
<img src="https://latex.codecogs.com/svg.latex?\frac{z'}{z^2} + \frac{1}{xz} = \frac{1}{xz^2}" />


Multiplying this by <img src="https://latex.codecogs.com/svg.latex?z^2" /> yields


<img src="https://latex.codecogs.com/svg.latex?-z' + \frac{1}{x}z = \frac{1}{x}" />

\
Complementary equation:

<img src="https://latex.codecogs.com/svg.latex?-z' + \frac{1}{x}z = 0" />

\
<img src="https://latex.codecogs.com/svg.latex?\int\frac{dz}{z} = \int \frac{dx}{x}" />

\
<img src="https://latex.codecogs.com/svg.latex?z = x \cdot C" />

\
<img src="https://latex.codecogs.com/svg.latex?-C -x \cdot C' + C = \frac{1}{x}" />

\
<img src="https://latex.codecogs.com/svg.latex?C' = -\frac{1}{x^2}" />


\
<img src="https://latex.codecogs.com/svg.latex?C = \frac{1}{x} + C_1" />

\
<img src="https://latex.codecogs.com/svg.latex?z = x(\frac{1}{x} + C_1)  \Rightarrow z = 1 + x \cdot C_1" />

\
**Exact solution**
<img src="https://latex.codecogs.com/svg.latex?y = \frac{1}{1 + x \cdot C}" /> 


\
Initial value problem:
<img src="https://latex.codecogs.com/svg.latex?\frac{1}{2} = \frac{1}{1 + C} \Rightarrow C = 1" /> 

\
**Solution for the initial value problem**
<img src="https://latex.codecogs.com/svg.latex?y = \frac{1}{1 + x}" /> 




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
For <img src="https://latex.codecogs.com/svg.latex?N \in [2, 5]" /> errors decrease approximately quadratically
For <img src="https://latex.codecogs.com/svg.latex?N > 5" /> changes in errors are less noticeable


