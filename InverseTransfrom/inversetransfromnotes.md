# Notes:


## Wikipedia:
Method takes random samples _u_ between 0 and 1, interpreted as probability, and returns the largest value _x_ from the domain of the function _P(X)_ such that the probability of drawing _X_ less than or equal to _x_ is equal to _u_.

You randomly choose a portion of area occuring under the curve and then finding the _x_ where this area occurs behind. 

Computing the CDF analytically is really hard for continuous functions (like the normal distribution). For discrete function, you simply sum the probability for every value of x.
