# Quant Interview Question: Find the Units Digit

## Asked by Citadel

### Problem Statement:


**Define product value of a number as follows:** 
- **Replace all 0s with 1.**
- **Product value is product of all digits.**

**Let S denote the sum of product values of integers from 0 to $10^{100}-1$, both inclusive.**
**What is units digit of S**

### Solution: 
Define $S(n) := \text{sum of product values of integers from } 0 \text{ to } 10^n-1$

$S(1) = 1 + \sum_{k=1}^{9}k = 46$

$S(n+1) = S(n) + \sum_{k=1}^{9}k\times S(n) = 46S(n)$

$\implies S(n) = 46^n$

$\text{put n=100, we get}$

$S(100) = 46^{100}$

$\text{Unit digit of }46^{100}\text{ is 6} \quad \blacksquare$