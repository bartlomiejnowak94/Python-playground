# Python Examples

- [Python Examples](#python-examples)
  - [Continued Fraction](#continued-fraction)
  - [Two Sum](#two-sum)

## Continued Fraction

File: [continued-frac.ipynb](continued-frac.ipynb)

Simple implementation in Python. Function `cont_frac(list)` takes as argument `type: list`, eg. `[a0,a1,a2,a3]` and returns numerical value for continued fraction in the form:
$$cf = a0 + \frac{1}{a1 + \frac{1}{a2 + \frac{1}{a3}}}$$

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

## Two Sum

File: [two-sum.ipynb](two-sum.ipynb)

We have given list like `[1,3,5,6,11,23]` and sum of some two values from this list `sum = 9`. We need to find these values, like here `3,6`.