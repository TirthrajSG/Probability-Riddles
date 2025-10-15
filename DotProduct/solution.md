# Quant Interview Question: Dot Product

## Asked by Citadel

### Problem Statement:

#### Let A be a 10 dimensional array of 0 and 1, for each element probability of 1 is $\frac{1}{2}$. Similarly let B be a 10 dimentional array of 0 and 1, for each element probability of 1 is $\frac{3}{4}$. Find the probability that the dot product of A and B is odd.

##### Method 1: Reccursion

We will approach this problem by recursion.

Assume we have calculated products till n<sup>th</sup> position, then the (n+1)<sup>th</sup> product will be 1 with prob $\frac{1}{2} \times \frac{3}{4} = \frac{3}{8}$.

Let probability that sum of products till n is odd is $p_n$, the recurssive relation: 

$p_{n} = \frac{3}{8} \times (1 - p_{n-1}) + \frac{5}{8} \times p_{n-1} \text{ and, } p_1 = \frac{3}{8}$

$\implies  p_n = \frac{1}{4} \times p_{n-1} + \frac{3}{8}$

$\implies p_n = \frac{1}{4^2} \times p_{n-2} + \frac{1}{4} \times \frac{3}{8} + \frac{3}{8}$

$\implies p_n = \frac{1}{4^3} \times p_{n-3} + \frac{1}{4^2} \times \frac{3}{8} + \frac{1}{4} \times \frac{3}{8} + \frac{3}{8}$

$\implies p_n = \frac{1}{4^k} \times p_{n-k} + \frac{3}{8} \sum_{i=1}^k \frac{1}{4^k}$

Put $k=n-1$

$\implies p_n = \frac{1}{4^{n-1}} \times p_{1} + \frac{3}{8} \times \frac{1(1 - \frac{1}{4^{n-1}})}{1 - \frac{1}{4}}$

$\implies p_n = \frac{1}{2^{2n-2}} \times \frac{3}{8} + \frac{3}{8} \times \frac{1 - \frac{1}{4^{n-1}}}{\frac{3}{4}}$

$\implies p_n = \frac{3}{2^{2n+1}} + \frac{1}{2} \times (1 - \frac{1}{4^{n-1}})$

$\implies p_n = \frac{1}{2} + \frac{3}{2^{2n+1}} - \frac{1}{2n-1}$

$\implies p_n = \frac{1}{2} + \frac{3}{2^{2n+1}} - \frac{4}{2n+1}$

$\implies p_n = \frac{1}{2} - \frac{1}{2n+1}$

For our question, put n = 10

$\implies p_{10} = \frac{1}{2} - \frac{1}{2^{21}} \approx 0.4999995$
