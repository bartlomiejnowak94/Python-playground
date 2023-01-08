# Python Examples

- [Python Examples](#python-examples)
  - [Continued Fraction](#continued-fraction)
  - [Two Sum](#two-sum)
  - [Roman to Int](#roman-to-int)

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

Problem taken from [leetcode](leetcode.com)

File: [two-sum.ipynb](two-sum.ipynb)

We have given list like `[1,3,5,6,11,23]` and sum of some two values from this list `sum = 9`. We need to find these values, like here `3,6`.

## Roman to Int

Problem taken from [leetcode](leetcode.com)

File: [romanToInt.ipynb](romanToInt.ipynb)

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.