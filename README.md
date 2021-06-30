# Numpy-Exercices

1. Import the numpy package under the name np (★☆☆)
2. Print the numpy version and the configuration (★☆☆)
3. Create a null vector of size 10 (★☆☆)
4. How to find the memory size of any array (★☆☆)
5. How to get the documentation of the numpy add function from the command line? (★☆☆)
6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
7. Create a vector with values ranging from 10 to 49 (★☆☆)
8. Reverse a vector (first element becomes last) (★☆☆)
9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
11. Create a 3x3 identity matrix (★☆☆)
12. Create a 3x3x3 array with random values (★☆☆)
13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
14. Create a random vector of size 30 and find the mean value (★☆☆)
15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
16. How to add a border (filled with 0's) around an existing array? (★☆☆)
17. What is the result of the following expression? (★☆☆)<br>

0 * np.nan<br>
np.nan == np.nan<br>
np.inf > np.nan<br>
np.nan - np.nan<br>
np.nan in set([np.nan])<br>
0.3 == 3 * 0.1<br>

18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element? (★☆☆)
21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
22. Normalize a 5x5 random matrix (★☆☆)
23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
26. What is the output of the following script? (★☆☆) <br><br>

print(sum(range(5),-1))<br>
from numpy import *<br>
print(sum(range(5),-1))<br>

27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)<br>

Z**Z<br>
2 << Z >> 2<br>
Z <- Z<br>
1j*Z<br>
Z/1/1<br>
Z<Z>Z<br>
  
28. What are the result of the following expressions? (★☆☆)<br>

np.array(0) / np.array(0)<br>
np.array(0) // np.array(0)<br>
np.array([np.nan]).astype(int).astype(float)<br>

29. How to round away from zero a float array ? (★☆☆)
30. How to find common values between two arrays? (★☆☆)
31. How to ignore all numpy warnings (not recommended)? (★☆☆)
32. Is the following expressions true? (★☆☆)<br>

np.sqrt(-1) == np.emath.sqrt(-1)<br>

33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
34. How to get all the dates corresponding to the month of July 2016? (★★☆)
35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
36. Extract the integer part of a random array of positive numbers using 4 different methods (★★☆)
37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆)
38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)
39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
40. Create a random vector of size 10 and sort it (★★☆)
41. How to sum a small array faster than np.sum? (★★☆)
42. Consider two random array A and B, check if they are equal (★★☆)
43. Make an array immutable (read-only) (★★☆)
44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
46. Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)
47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj)) (★★☆)
48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)
49. How to print all the values of an array? (★★☆)
50. How to find the closest value (to a given scalar) in a vector? (★★☆)
51. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆)
52. Consider a random vector with shape (100,2) representing coordinates, find point by point distances (★★☆)
53. How to convert a float (32 bits) array into an integer (32 bits) in place?
54. How to read the following file? (★★☆)
  
1, 2, 3, 4, 5<br>
6,  ,  , 7, 8<br>
 ,  , 9,10,11<br>
  
55. What is the equivalent of enumerate for numpy arrays? (★★☆)
56. Generate a generic 2D Gaussian-like array (★★☆)
57. How to randomly place p elements in a 2D array? (★★☆)
58. Subtract the mean of each row of a matrix (★★☆)
59. How to sort an array by the nth column? (★★☆)
60. How to tell if a given 2D array has null columns? (★★☆)
61. Find the nearest value from a given value in an array (★★☆)
62. Considering two arrays with shape (1,3) and (3,1), how to compute their sum using an iterator? (★★☆)
63. Create an array class that has a name attribute (★★☆)
64. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? (★★★)
65. How to accumulate elements of a vector (X) to an array (F) based on an index list (I)? (★★★)
66. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique colors (★★☆)
67. Considering a four dimensions array, how to get sum over the last two axis at once? (★★★)
68. Considering a one-dimensional vector D, how to compute means of subsets of D using a vector S of same size describing subset indices? (★★★)
69. How to get the diagonal of a dot product? (★★★)
70. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3 consecutive zeros interleaved between each value? (★★★)
71. Consider an array of dimension (5,5,3), how to mulitply it by an array with dimensions (5,5)? (★★★)
72. How to swap two rows of an array? (★★★)
73. Consider a set of 10 triplets describing 10 triangles (with shared vertices), find the set of unique line segments composing all the triangles (★★★)
74. Given a sorted array C that corresponds to a bincount, how to produce an array A such that np.bincount(A) == C? (★★★)
75. How to compute averages using a sliding window over an array? (★★★)
76. Consider a one-dimensional array Z, build a two-dimensional array whose first row is (Z[0],Z[1],Z[2]) and each subsequent row is shifted by 1 (last row should be (Z[-3],Z[-2],Z[-1]) (★★★)
