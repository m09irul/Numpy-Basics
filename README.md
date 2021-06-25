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
