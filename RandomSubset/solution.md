# Quant Interview Question: Exact Maximum

## Asked by Citadel

### Problem Statement:

#### Let $S=\{1,2,3,…,10\}$. Two subsets $𝑋$ and $𝑌$ are chosen independently and uniformly at random from the power set of $𝑆$, i.e. each of the $2^10$ subsets of $𝑆$ is equally likely to be chosen for both $𝑋$ and $𝑌$. Determine the probability that $𝑋$ is a subset of $𝑌$ that is, find $P(X⊆Y)$.

### Method 1: Intuitive

For each element $s$ in $S$, $\text{P(}s\text{ in }X\text{ and }Y\text{)} = 1 - \text{P(}s\text{ not in } X \text{ and }Y) = 1 - \frac{1}{4} = \frac{3}{4}$

$\therefore P(X \subseteq Y) = \left(\frac{3}{4}\right)^{10} \approx 0.0563135$

### Method 2: Mathematical

Choose a subset $X$ with $|X| = n$ in $\binom{10}{n}$ ways, then number of ways to choose Y are $2^{10-n}$. This is because we have two choices for the elements not in X, to be in Y or not to be in Y.

Total Proability $P(X \subseteq Y) = \frac{\sum_{n=0}^{10} \binom{10}{n} \times 2^{10-n}}{2^{20}} = \frac{1}{2^{10}}\times \sum_{n=0}^{10}\binom{10}{n}\times \left(\frac{1}{2}\right)^{n}\times(1)^{10-n} = \frac{1}{2^{10}}\times\left(\frac{1}{2} + 1\right)^{10} = \left(\frac{3}{4}\right)^{10} \approx 0.0563135$