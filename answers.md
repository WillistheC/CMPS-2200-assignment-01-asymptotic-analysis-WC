# CMPS 2200 Assignment 01
## Answers

**Name:** Will Cunningham

Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**
  - 1a (2 pts): Yes, the limit of T over O is a constant
  
  - 1b (2 pts): No, the limit computes to $2^{2^n - n}$, which is $2^\infty = \infty$
 
  - 1c (2 pts): No, ignoring constants, L'Hopital's gives $\frac{n^{.1}}{n^{-1}\mathrm{log}n}$ which goes to $\infty$ 

  - 1d (2 pts): Yes, because the limit computes to $\infty$ 

  - 1e (2 pts): No, ignoring constants, L'Hopital's gives $\frac{n^{-.5}}{n^{-1}\mathrm{log}^{2}n} = \frac{n^{-.5}}{n^{-1}\mathrm{log}n} = n^{.5}$ which goes to $\infty$

  - 1f (2 pts): Yes, because the limit computes to $\infty$ 

  - 1g (2 pts):

2. **SPARC to Python**

  - 2b (3 pts): This function gives the nth term of the Fibonacci Sequence

3. **Parallelism and recursion**

  - 3b (4 pts): Each element is processed once, so $W(n) = Θ(n)$; Each iteration is dependent, so $S(n) = Θ(n)$

  - 3d (4 pts): Recursive calls are made on $2$ lists of size $\frac{n}{2}$, so $W(n) = 2W(\frac{n}{2}) = Θ(n)$

  - 3e (5 pts):
