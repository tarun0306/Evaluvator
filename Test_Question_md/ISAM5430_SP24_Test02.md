# Array 1: Larger Running Averages

Calculate the average of all the numbers greater than their previously
running averages.

1.  Create a function that accepts an integer array.

2.  The function then calculates and returns the average of all the
    values that **<u>EXCEED</u>** the running average of their previous
    numbers.

    1.  Previous numbers of a value refer to all the numbers (with a
        lower index) that occur before that value.

    2.  Therefore, if a value doesn’t have any previous values, that
        value will not be considered in the average.

    3.  The running average of all the previous numbers is calculated by
        taking the sum divided by the count starting from the first
        element till the previous element.

3.  If the function cannot determine any such values, it returns zero.

<table>
<thead>
<tr class="header">
<th>Input</th>
<th>Output</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{7, 3, 1, 8, 2, 4, 5, 0, 9}</p>
<p><em>You should try out other numbers too.</em></p></td>
<td><span class="math display">$$\frac{8 + 5 + 9}{3} = 7.33$$</span></td>
<td><table>
<thead>
<tr class="header">
<th>Index</th>
<th>Item</th>
<th>Previous Sum</th>
<th>Running Average</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>7</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>1</td>
<td>3</td>
<td>7</td>
<td>7.00</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1</td>
<td>10</td>
<td>5.00</td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td><strong>8</strong></td>
<td><strong>11</strong></td>
<td><strong>3.67</strong></td>
</tr>
<tr class="odd">
<td>4</td>
<td>2</td>
<td>19</td>
<td>4.75</td>
</tr>
<tr class="even">
<td>5</td>
<td><strong>4</strong></td>
<td><strong>21</strong></td>
<td>4.20</td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td>5</td>
<td>25</td>
<td><strong>4.17</strong></td>
</tr>
<tr class="even">
<td>7</td>
<td>0</td>
<td>30</td>
<td>4.29</td>
</tr>
<tr class="odd">
<td><strong>8</strong></td>
<td><strong>9</strong></td>
<td><strong>30</strong></td>
<td><strong>3.75</strong></td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="even">
<td>{ 3, 2, 1 }</td>
<td><span class="math display">0</span></td>
<td>There are no values that exceed their previously running averages.</td>
</tr>
<tr class="odd">
<td>null</td>
<td><span class="math display">0</span></td>
<td>There are no valid values in a null array.</td>
</tr>
<tr class="even">
<td>{ }</td>
<td><span class="math display">0</span></td>
<td>There are no valid values in an empty array.</td>
</tr>
<tr class="odd">
<td>{ 1 }</td>
<td><span class="math display">0</span></td>
<td>1 has no previously running average.</td>
</tr>
</tbody>
</table>

# Array 2: Nested Loop

Create a new array by repeating the values from the original array,
excluding one of the smallest numbers each time, while preserving the
original order.

1.  Create a method that accepts an *array*.

2.  The method creates and returns a new array *newArray* that
    essentially has a length of

$$\\frac{array.length \\times \\left( array.length + 1 \\right)}{2}$$

3.  First, copy all the values from the original array into the
    *newArray*.

4.  Within the nested loop, insert all the previously inserted values,
    excluding one of their smallest values, into the *newArray*.

5.  Iterate through Step 4 until there are no more elements to insert.

6.  For maximum credit, your time complexity should be
    *O*(*n*<sup>2</sup>). The space complexity should be
    *O*(*n*<sup>2</sup>) for the result array. Do not create an
    additional array. Do not sort the array.

<table>
<thead>
<tr class="header">
<th>Original array</th>
<th>New array</th>
<th>Original array</th>
<th>New array</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{ 7, 3, 1, 8, 2, 4, 5, 0, 9 }</p>
<p>Each time, the smallest number is dropped from the sequence.</p></td>
<td>7, 3, 1, 8, 2, 4, 5, 0, 9,<br />
7, 3, 1, 8, 2, 4, 5, 9,<br />
7, 3, 8, 2, 4, 5, 9,<br />
7, 3, 8, 4, 5, 9,<br />
7, 8, 4, 5, 9,<br />
7, 8, 5, 9,<br />
7, 8, 9,<br />
8, 9,<br />
9</td>
<td><p>1, 2, 2, 1, 3</p>
<p>Each time, one of the smallest, repeated numbers is dropped from the sequence.</p></td>
<td>1, 2, 2, 1, 3,<br />
2, 2, 1, 3,<br />
2, 2, 3,<br />
2, 3,<br />
3</td>
</tr>
<tr class="even">
<td>null</td>
<td>null</td>
<td>{ 0 }</td>
<td>{ 0 }</td>
</tr>
<tr class="odd">
<td>{ }</td>
<td>{ }</td>
<td>{ 2, 1 }</td>
<td>{ 2, 1, 2 }</td>
</tr>
</tbody>
</table>

# Binary Search: Positive Root of a Parabola

Use binary search to approximate the positive root in integer for a
given parabola function.

1.  Create a function named *f*(*x, b, c*) that accepts three arguments.

    1.  Integer *x*;

    2.  An integer *b*;

    3.  Positive integer *c* (we will assume positive *c*, such that
        *c* &gt; 0);

2.  The function then calculates and returns the integer value from the
    following equation:

*f*(*x*) = *x*<sup>2</sup> + *b**x* − *c***.**

1.  This function produces a parabola.

2.  This a concave function because the root of the second derivative of
    *f*(*x*) is positive, i.e., *f*<sup>″</sup>(*x*) = 2.

3.  A root refers to the value of *x* when f(*x*) = 0.

4.  Thus, there are always two calculated roots from the Quadratic
    formula:

$$\\frac{- b \\pm \\sqrt{b^{2} + 4c}}{2}\\text{\\ when\\ }f\\left( x \\right) = 0.$$

5.  **Note:** This parabola function always has a negative and positive
    root because the numerator, $- b \\pm \\sqrt{b^{2} + 4c}$, with
    4*c* &gt; 0 will result in both negative and positive values, thus
    implying that the root can never be 0.

<!-- -->

3.  Create a second function called “**FindRoot**” that accepts two
    positive integers: *b* and *c*.

4.  The “**FindRoot**” function uses the **<u>binary search
    algorithm</u>** to find the positive integer root *x* of the
    Parabola function by calling the first function
    *f*(*x*, *b*, *c*) ≈ 0.

5.  Since we are searching for the positive root, we need to locate the
    search region between 1 and the ***high*** value (since the root has
    to be positive).

    1.  To estimate the ***high*** value, we’ll iteratively double the
        search value starting from the value 1 until *f*(high) ≥ 0.

    2.  This approach ensures that the number of operations remains
        logarithmic (*O*(log *n*)).

6.  Having determined the ***high*** value, use the binary search to
    locate the integer root that intersects the *x*-axis.

7.  Time complexity: *O*(*l**o**g* *n*), Space complexity: *O*(1). Make
    sure you write some codes to test the cases on the following page.

|        
 **b**   |       
          **c**  |                                 
                  **f****(****x****)**             |                                                                   
                                                    Graph                                                              |                             
                                                                                                                         **+** **r****o****o****t**  | calculated                                       |
|--------|-------|---------------------------------|-------------------------------------------------------------------|-----------------------------|--------------------------------------------------|
|        
  − 2    |       
          3      |                                 
                  *x*<sup>2</sup> − 2*x* − 3       | <img src="media/image1.png" style="width:2in;height:1.29825in" /> |                             
                                                                                                                        3                            |                                                  
                                                                                                                                                      $$\\frac{2 + \\sqrt{4 + 4 \\times 3}}{2} = 3$$    |
|        
 2       |       
          3      |                                 
                  *x*<sup>2</sup> + 2*x* − 3       | <img src="media/image2.png" style="width:2in;height:1.28319in" /> |                             
                                                                                                                        1                            |                                                  
                                                                                                                                                      $$\\frac{- 2 + \\sqrt{4 + 4 \\times 3}}{2} = 1$$  |
|        
 10      |       
          75     |                                 
                  *x*<sup>2</sup> + 10*x* − 75     | <img src="media/image3.png" style="width:2in;height:1.34513in" /> |                             
                                                                                                                        5                            |                                                  
                                                                                                                                                      $$\\frac{- 10 + \\sqrt{400}}{2} = 5$$             |
|        
  − 10   | 75    |                                 
                  *x*<sup>2</sup> − 10*x* − 75     | <img src="media/image4.png" style="width:2in;height:1.35426in" /> |                             
                                                                                                                        15                           |                                                  
                                                                                                                                                      $$\\frac{10 + \\sqrt{400}}{2} = 15$$              |
|        
  − 100  |       
          1000   |                                 
                  *x*<sup>2</sup> − 100*x* − 1000  | <img src="media/image5.png" style="width:2in;height:1.27273in" /> |                             
                                                                                                                        109                          |                                                  
                                                                                                                                                      $$50 + 10\\sqrt{35} \\approx 109.2$$              |
