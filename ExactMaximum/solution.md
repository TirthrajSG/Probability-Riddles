# Quant Interview Question: Exact Maximum

## Asked by Citadel

### Problem Statement:

#### 8 six sided fare die are rolled, find the probability that the maximum of the rolls is 5.

### Method 1: Find Cases

**Total Outcomes** = $6^8$

Calculate favourable outcomes:

**Case 1:** no. of dice with 5 on top = 1 

Number of cases = $\binom{8}{1} \times 4^7$

**Case 2:** no. of dice with 5 on top = 2 

Number of cases = $\binom{8}{2} \times 4^6$

$\vdots$

**Case 8:** no. of dice with 5 on top = 8 

Number of cases = $\binom{8}{8} \times 4^0$

$\therefore \text{Favourable outcomes} = \sum_{k=1}^{8} \binom{8}{k} \times 4^{8-k}$

By Binomial theorem, 

$(1 + 4)^8 = \sum_{k=0}^{8} \binom{8}{k} \times 1^k \times 4^{8-k} = 4^8 + \sum_{k=1}^{8} \binom{8}{k} \times 4^{8-k}$

$\therefore \text{Favourable Outcomes} = 5^8 - 4^8$

$\implies \text{P(max of 8 rolls = 5)} = \frac{5^8-4^8}{6^8} \approx 0.1935496$

### Method 2: Combinatorics

$\begin{aligned}
\text{P(max = 5)} &= \text{P(max }\le\text{ 5)} - \text{P(max }\le\text{ 4)} \\
&= \frac{5^8}{6^8} - \frac{4^8}{6^8} \\
&= \frac{5^8 - 4^8}{6^8} \\
&\approx 0.1935496
\end{aligned}$
