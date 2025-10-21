# Quant Interview Question: Exact Maximum

## Asked by Citadel

### Problem Statement:

#### Five points are chosen independently and uniformly at random on the circumference of a unit circle. What is the probability that the center of the circle lies inside the convex pentagon formed by joining these five points in order around the circle?

### Method 1: Intuitive

$\text{P(Center lies inside) = 1 - P(Center lies outside)}$

Center lies outside $\implies$ All 5 points lie on one hemisphere.

Choose a point from 5 points with $\binom{5}{1}$ ways.

Put that point on the circle with probability 1.

Put other 4 points on same hemisphere with probability $(\frac{1}{2})^4$

$\text{P(Center lies outtside)} = \binom{5}{1} \times \frac{1}{2^4} = \frac{5}{16}$

$\text{P(Center lies inside)} = 1 - \text{P(Center lies outside)}$

$\text{P(Center lies inside)} = 1 - \frac{5}{16} = \frac{11}{16}$


### Method 1: Mathematical

$\text{Let } U_1, U_2, U_3, U_4, U_5 \text{ be angles from positive x-axis such that } U_i \sim\text{Unif(}0,2\pi\text{)}$

$\text{P(Center lies inside)} = \text{P(max(}U_i - U_j\text{) < }\pi\text{)} = \text{P(max(}U_i\text{)} - \text{min(}U_j\text{) < }\pi\text{)}$

$\text{Let max(}U_i\text{)} = Y \text{ and min(}U_i\text{)} = X$

$X = U_{(1)}$ and $Y = U_{(5)}$ where $U_{(i)}$ are order statistics

Joint Distribution of $X$ and $Y$ will be $$
