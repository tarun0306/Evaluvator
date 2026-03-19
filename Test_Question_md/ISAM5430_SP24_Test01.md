# Selection statements

***For three integers, calculate the average of all the non-zero
remainders whose quotients are non-zero.***

1.  Without using a loop, input three **integers**.

2.  Determine which quotients of the two numbers from the three numbers
    entered are not zero.

3.  Include all the non-zero remainders that satisfy the conditions
    above into the average ($\\frac{\\text{sum}}{\\text{count}}$).

4.  If such an average exists, print out the average.

$$\\frac{a}{b} = quotient + \\frac{\\mathbf{\\text{remainder}}}{b}\\text{,\\ where\\ }b \\neq 0,\\ quotient \\neq 0,\\text{\\ and\\ }\\mathbf{\\text{remainder}} \\neq 0.$$

<img src="media/image1.png" style="width:2.17687in;height:0.67413in" alt="A number and arrows with black text Description automatically generated with medium confidence" />
<img src="media/image2.png" style="width:2.62585in;height:0.71749in" alt="A number symbols and numbers Description automatically generated with medium confidence" />

# Sentinel Control Loop

***For a sequence of non-zero integers, calculate the average of all the
non-zero remainders whose quotients are non-zero.***

1.  Using a loop, Input a sequence of integer pairs (*a* and *b*) until
    any integer entered is zero.

2.  For each pair, determine which quotient of the pairs entered (*a*
    and *b*) is not zero.

3.  Include all the non-zero remainders into the average
    ($\\frac{\\text{sum}}{\\text{count}}$) whenever that condition is
    true.

4.  Print out the average if such an average exists.

<img src="media/image3.png" style="width:1.90476in;height:2.38495in" alt="A math test with red text Description automatically generated with medium confidence" />
<img src="media/image4.png" style="width:2.50517in;height:1.89116in" alt="A white background with black text Description automatically generated" />

# Min, Max, Previous Values

***Determine the number of values entered between the maximum number
with an increasing last digit and the minimum number with a decreasing
last digit in a sequence of non-repeated values entered.***

1.  Enter a sequence of integers until two identical numbers are entered
    continuously.

2.  ***Maximum number with an increasing last digit***: find the
    **<u>MAXIMUM</u>** of the numbers entered in increasing order when
    its last digit is in increasing order compared to the previous
    number.

3.  ***Minimum number with a decreasing last digit***: find the
    **<u>MINIMUM</u>** of the numbers entered when its last digit is in
    decreasing order compared to the previous number.

4.  <img src="media/image5.png" style="width:2.94861in;height:2.92292in" />Print
    out the number of values (*count*) entered that lie between these
    minimum and maximum values if such maximum and minimum points exist
    in the sequence of numbers entered.

| **Count** | **Input** | **Comment**                      |
|-----------|-----------|----------------------------------|
| 1         | 73        | First                            |
| 2         | 55        | Max = 73 (73 is considered here) |
| 3         | 27        |                                  |
| 4         | 26        | Min = 26                         |
| 5         | 71        |                                  |
| 6         | 21        | (same 1 has no effect)           |
| 7         | 87        | Max = 87                         |
| 8         | 97        | (same 7 has no effect here)      |
| 9         | 11        | Min = 11                         |
| 10        | 25        |                                  |
| 11        | 25        | *Sentinel*                       |

Count = 1.
