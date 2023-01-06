# Continued Fraction

Simple implementation in Python. Function `cont_frac(list)` takes as argument `type: list`, eg. `[a0,a1,a2,a3]` and returns numerical value for continued fraction in the form:
$$cf = a0 + \frac{1}{a1 + \frac{1}{a2 + \frac{1}{a3}}}$$

## Solving problem
Continued fraction defined as
$$cf = a0 + \frac{1}{a1 + \frac{1}{a2 + \frac{1}{a3 + \dots}}}$$
can be solved backwards. Take last value from list, reverse it and add it to next value `a2`
```
cf = a3
cf = 1/cf + a2
```
Do this as long as you have values in your list
```
cf = 1/cf + a1
cf = 1/cf + a0
```
