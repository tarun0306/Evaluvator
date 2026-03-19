# Raise a Polynomial to the Power of *n*

1.  Create a method that accepts the following two parameters.

    1.  an **array of integers** that represents the coefficients of a
        polynomial and

        1.  For example, if the array is {5, 6, 7, 8, 9}, then the
            represented polynomial is
            5*x*<sup>4</sup> + 6*x*<sup>3</sup> + 7*x*<sup>2</sup> + 8*x* + 9.

    2.  an **integer** ***n*** that represents the power of n.

    3.  <u>Ensure that you’ve tested all the values in the table
        below.</u>

2.  When the value of ***n*** is **<u>negative</u>** or **<u>zero</u>**
    OR when the ***array of integers*** is null or empty, the method
    simply returns a null.

3.  The method returns an array of integers that represents the
    coefficients of the input polynomial raised to the power of *n*.

    1.  The return array should have a length of

*r**e**s**u**l**t**i**n**g* *l**e**n**g**t**h* = *n*(*l**e**n**g**t**h*−1) + 1

2.  Therefore, the first step is to first **<u>copy all the values from
    the original array</u>** to the end of the return array.

3.  For example, if the input array is {5, 6, 7, 8, 9} and *n* = 2, then
    we will need to calculate the
    (5*x*<sup>4</sup>+6*x*<sup>3</sup>+7*x*<sup>2</sup>+8*x*+9)<sup>2</sup>.
    See the next page of the actual workouts.

4.  Because the highest power is 4 × 3 = 12, the length of the return
    array is 13.

5.  As such, the return array should be initialized to  
    {0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 7, 8, 9} before performing
    multiplications.

<!-- -->

4.  This should have **O****(****n****×****l**<sup>**2**</sup>**)**
    **operations, so you are expected to write <u>three nested
    loops</u>**. You may create as many arrays as you need to. But, you
    should work out the calculations individually before you can
    understand what to write. If *n* = 2 is the only one you’ve got,
    that’s better than nothing. Optimization is not a priority.

|                 
 Input array      |       
                   **n**  |                                            
                           Return array                                |
|-----------------|-------|--------------------------------------------|
|                 
 {1, 2}           |       
                   0      |                                            
                           null                                        |
|                 
 null             |       
                   1      |                                            
                           null                                        |
|                 
 {5, 6, 7, 8, 9}  |       
                   1      |                                            
                           {5, 6, 7, 8, 9}                             |
|                 
 {5, 6, 7, 8, 9}  |       
                   2      |                                            
                           {25, 60, 106, 164, 235, 220, 190, 144, 81}  |
|                 
 {5, 6, 7, 8, 9}  |       
                   3      |                                            
                           $$\\begin{Bmatrix}                          
                           125,450,1065,2096,3606,5046, \\\\           
                           6181,6756,6474,4994,3429,1944,729 \\\\      
                           \\end{Bmatrix}$$                            |

## First, multiply each term together.

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     | 5   | 6   | 7   | 8   | 9   |
|     |     |     |     |     |     |     |     |     |     |     |     | 9   |
|     |     |     |     |     |     |     |     | 45  | 54  | 63  | 72  | 81  |

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     | 5   | 6   | 7   | 8   | 9   |
|     |     |     |     |     |     |     |     |     |     |     | 8   |     |
|     |     |     |     |     |     |     | 40  | 48  | 56  | 64  | 72  |     |

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     | 5   | 6   | 7   | 8   | 9   |
|     |     |     |     |     |     |     |     |     |     | 7   |     |     |
|     |     |     |     |     |     | 35  | 42  | 49  | 56  | 63  |     |     |

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     | 5   | 6   | 7   | 8   | 9   |
|     |     |     |     |     |     |     |     |     | 6   |     |     |     |
|     |     |     |     |     | 30  | 36  | 42  | 48  | 54  |     |     |     |

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     | 5   | 6   | 7   | 8   | 9   |
|     |     |     |     |     |     |     |     | 5   |     |     |     |     |
|     |     |     |     | 25  | 30  | 35  | 40  | 45  |     |     |     |     |

## Sum up all the total results to get the final return array.

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |     |     | 45  | 54  | 63  | 72  | 81  |
|     |     |     |     |     |     |     | 40  | 48  | 56  | 64  | 72  |     |
|     |     |     |     |     |     | 35  | 42  | 49  | 56  | 63  |     |     |
|     |     |     |     |     | 30  | 36  | 42  | 48  | 54  |     |     |     |
|     |     |     |     | 25  | 30  | 35  | 40  | 45  |     |     |     |     |
| 0   | 0   | 0   | 0   | 25  | 60  | 106 | 164 | 235 | 220 | 190 | 144 | 81  |

*T**h**u**s*,  (5*x*<sup>4</sup>+6*x*<sup>3</sup>+7*x*<sup>2</sup>+8*x*+9)<sup>2</sup>=

25*x*<sup>8</sup> + 60*x*<sup>7</sup> + 106*x*<sup>6</sup> + 164*x*<sup>5</sup> + 235*x*<sup>4</sup> + 220*x*<sup>3</sup> + 190*x*<sup>2</sup> + 144*x* + 81.

Let’s repeat for
(5*x*<sup>4</sup>+6*x*<sup>3</sup>+7*x*<sup>2</sup>+8*x*+9)<sup>3</sup>.

(5*x*<sup>4</sup>+6*x*<sup>3</sup>+7*x*<sup>2</sup>+8*x*+9)<sup>2</sup>(5*x*<sup>4</sup>+6*x*<sup>3</sup>+7*x*<sup>2</sup>+8*x*+9)  = (25*x*<sup>8</sup>+60*x*<sup>7</sup>+106*x*<sup>6</sup>+164*x*<sup>5</sup>+235*x*<sup>4</sup>+220*x*<sup>3</sup>+190*x*<sup>2</sup>+144*x*+81)(5*x*<sup>4</sup>+6*x*<sup>3</sup>+7*x*<sup>2</sup>+8*x*+9)

## Multiply the previous array with the original array:

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7    | 8    | 9    | 10   | 11   | 12  |
|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|------|-----|
|     |     |     |     | 25  | 60  | 106 | 164  | 235  | 220  | 190  | 144  | 81  |
|     |     |     |     |     |     |     |      |      |      |      |      | 9   |
|     |     |     |     | 225 | 540 | 954 | 1476 | 2115 | 1980 | 1710 | 1296 | 729 |

| 0   | 1   | 2   | 3   | 4   | 5   | 6    | 7    | 8    | 9    | 10   | 11  | 12  |
|-----|-----|-----|-----|-----|-----|------|------|------|------|------|-----|-----|
|     |     |     |     | 25  | 60  | 106  | 164  | 235  | 220  | 190  | 144 | 81  |
|     |     |     |     |     |     |      |      |      |      |      | 8   |     |
|     |     |     | 220 | 480 | 848 | 1312 | 1880 | 1760 | 1520 | 1152 | 648 |     |

| 0   | 1   | 2   | 3   | 4   | 5    | 6    | 7    | 8    | 9    | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|------|------|------|------|------|-----|-----|-----|
|     |     |     |     | 25  | 60   | 106  | 164  | 235  | 220  | 190 | 144 | 81  |
|     |     |     |     |     |      |      |      |      |      | 7   |     |     |
|     |     | 175 | 420 | 742 | 1148 | 1645 | 1540 | 1330 | 1008 | 567 |     |     |

| 0   | 1   | 2   | 3   | 4   | 5    | 6    | 7    | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|-----|------|------|------|-----|-----|-----|-----|-----|
|     |     |     |     | 25  | 60   | 106  | 164  | 235 | 220 | 190 | 144 | 81  |
|     |     |     |     |     |      |      |      |     | 6   |     |     |     |
|     | 150 | 360 | 636 | 984 | 1410 | 1320 | 1140 | 864 | 486 |     |     |     |

| 0   | 1   | 2   | 3   | 4    | 5    | 6   | 7   | 8   | 9   | 10  | 11  | 12  |
|-----|-----|-----|-----|------|------|-----|-----|-----|-----|-----|-----|-----|
|     |     |     |     | 25   | 60   | 106 | 164 | 235 | 220 | 190 | 144 | 81  |
|     |     |     |     |      |      |     |     | 5   |     |     |     |     |
| 125 | 300 | 530 | 820 | 1175 | 1100 | 950 | 720 | 405 |     |     |     |     |

## Sum the results up to get the final return array

| 0   | 1   | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12  |
|-----|-----|------|------|------|------|------|------|------|------|------|------|-----|
|     |     |      |      | 225  | 540  | 954  | 1476 | 2115 | 1980 | 1710 | 1296 | 729 |
|     |     |      | 220  | 480  | 848  | 1312 | 1880 | 1760 | 1520 | 1152 | 648  |     |
|     |     | 175  | 420  | 742  | 1148 | 1645 | 1540 | 1330 | 1008 | 567  |      |     |
|     | 150 | 360  | 636  | 984  | 1410 | 1320 | 1140 | 864  | 486  |      |      |     |
| 125 | 300 | 530  | 820  | 1175 | 1100 | 950  | 720  | 405  |      |      |      |     |
| 125 | 450 | 1065 | 2096 | 3606 | 5046 | 6181 | 6756 | 6474 | 4994 | 3429 | 1944 | 729 |
