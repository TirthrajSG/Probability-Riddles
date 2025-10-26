# Quant Interview Question: Twelve Coins

## Jane Street

### Problem Statement:

#### Consider a collection of 12 independent coins. The coins are divided into four groups according to their respective probabilities of landing heads:
- 3 coins each have $P(Head)=\frac{1}{2}$,
- 3 coins each have $P(Head)=\frac{1}{3}$,
- 3 coins each have $P(Head)=\frac{1}{5}$,
- 3 coins each have $P(Head)=\frac{1}{9}$.
#### What is the probability that number of heads is odd?

### Method 1: Intuitive
Assume all coins except 1 coin with P(Head) = $\frac{1}{2}$ are tossed.

$\text{P(Number of heads in 12 tosses is odd)} = \frac{1}{2}\times\text{P(Number of heads in 11 tosses is odd)} + \frac{1}{2}\times\text{P(Number of heads in 11 tosses is even)} = \frac{1}{2}\times 1 = \frac{1}{2}$

### Method 2: Brute-Force
For total number of heads to be odd, four groups of coins must have number of heads odd or even according to following table

|P(Head)=1/2 | P(Head)=1/3 | P(Head)=1/5 | P(Head)=1/9 |
|-----------|--------------|-------------|--------------|
|Odd|Even|Odd|Odd|
|Odd|Odd|Even|Odd|
|Odd|Odd|Odd|Even|
|Odd|Even|Even|Even|
|Even|Odd|Odd|Odd|
|Even|Even|Even|Odd|
|Even|Even|Odd|Even|
|Even|Odd|Even|Even|

for 3 coins where $P(Head) = p$, P(no. of heads is odd) = $p^3 + 3p(1-p)^2$ and P(no. of heads is even) = $p^3 + 3p^2(1-p)$

For first group, 
- P(No. of heads is odd) = $\frac{1}{2}$
- P(No. of heads is Even) = $\frac{1}{2}$

For second group, 
- P(No. of heads is odd) = $\frac{13}{27}$
- P(No. of heads is Even) = $\frac{1}{2}$