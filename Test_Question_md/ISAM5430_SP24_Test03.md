# Loop: *sum and the largest base-N digit*

Determine the sum of all the Base-N digits and the largest Base-N digit
in a given integer.

1.  Create a console application that prompts the user to enter two
    numbers:

    1.  Integer (can be positive or negative) and

    2.  Base-N (must be positive)

2.  The app should iteratively ensure that the base-N entered is
    positive, i.e., *re-prompt if a negative or zero is entered*.

3.  The app should break down the given integer into base-N digits by
    repeatedly fetching the remainders as Base-N digits and dividing the
    integer by N.

4.  Then, the app then calculates and displays the sum of all these
    Base-N digits.

5.  The app also determines the largest Base-N digit and displays it.

<table>
<thead>
<tr class="header">
<th><p>Enter an integer</p>
<p>346251</p>
<p>Enter base-N (must be positive)</p>
<p>10</p>
<p>Sum of base-10 digits = 21.</p>
<p>Max base-10 digit = 6.</p></th>
<th><p>6 is the largest digit in 346251 (base-10).</p>
<p><span class="math display">3 + 4 + 6 + 2 + 5 + 1 = 21</span></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter an integer</p>
<p>10</p>
<p>Enter base-N (must be positive)</p>
<p>-3</p>
<p>Enter base-N (must be positive)</p>
<p>3</p>
<p>Sum of base-3 digits = 2.</p>
<p>Max base-3 digit = 1.</p></td>
<td><p>The app asks the user to reenter the Base-N because a negative <span class="math inline"> − 3</span> is entered.</p>
<p>10 in Base-3 is 101,</p>
<p>so its sum is <span class="math inline">1 + 0 + 1 = 2</span> and</p>
<p>the maximum digit is 2 here.</p></td>
</tr>
<tr class="even">
<td><p>Enter an integer</p>
<p>-233573869</p>
<p>Enter base-N (must be positive)</p>
<p>16</p>
<p>Sum of base-16 digits = 79.</p>
<p>Max base-16 digit = 14.</p></td>
<td><p>Negative sign in <span class="math inline"> − 233573869</span> is dropped, so</p>
<p><span class="math display">(233573869)<sub>10</sub> = (<em>D</em><em>E</em><em>C</em>0<em>D</em><em>E</em><em>D</em>)<sub>16</sub></span></p>
<p>Thus, “E” is the largest hexadecimal digit, which gets translated to 14. And, the sum is</p>
<p><span class="math display"><em>D</em> + <em>E</em> + <em>C</em> + 0 + <em>D</em> + <em>E</em> + <em>D</em></span></p>
<p><span class="math display">13 + 14 + 12 + 0 + 13 + 14 + 13 = 79</span></p></td>
</tr>
</tbody>
</table>

# Array/Nested Loop: *insertion counts*

Given an array, build a new array that contains the **number of
insertions** required for each corresponding element in an insertion
sort without actually sorting the array.

1.  Create a method that accepts an array.

2.  The method returns the count array with the same length as the
    original array.

3.  In a nested loop, the method then counts the number of
    ***insertions*** necessary for each element and store them into the
    count array.

4.  Please analyze how insertion sort works before implementing it. The
    solution can be simplified without fully implementing the insertion
    sort algorithm. You can do it in *O*(*n*<sup>2</sup>) time.

    1.  In insertion sort, we compare each element with the ones before
        it.

    2.  An “***insertion”*** occurs when we move an element greater than
        the key element to one position ahead; doing so will create
        space for the key element.

    3.  For example, consider the array {1, 10, 23, **<u>5</u>**, 2}. To
        insert the element 5 before the element 10, we need to perform 2
        ***insertions***.

        1.  First, move 23 forward to create space for 5: {1, 10, \_\_,
            23, 2}.

        2.  Second, move 10 forward to create space for 5: {1, \_\_, 10
            ,23, 2}.

        3.  Finally, insert 5 at the correct position: {1, **<u>5</u>**,
            10, 23, 2}

    4.  Since we just need to count the ***number of insertions***, we
        do not need to physically sort these elements.

<img src="media/image1.png" style="width:4.91838in;height:2.80132in" alt="Lightbox" />

In the example above, for {23, 1, 10, 5, 2} array,

the returned count array will be {0, 1, 1, 2, 3}.

# Dictionary: *sum of all the largest numbers repeated in every different frequency*

Given an array with many repeated values, calculate the sum of all the
largest numbers repeated in every different frequency using
Dictionaries.

1.  Create a method that accepts an array as input.

2.  The method should then count the occurrence of each number in the
    array and store them into a dictionary.

3.  Next, the method iterates through the dictionary to identify all the
    largest numbers for different frequencies.

4.  Finally, it should sum up all the products of these values with
    their corresponding frequencies to determine the “sum of all the
    largest numbers repeated in every different frequency.”

5.  Return 0 when the input is array is invalid (i.e., null).

6.  To achieve *O*(*n*) time complexity, we can use two dictionaries:
    one ***for counting the occurrences*** and another for ***tracking
    the largest value for different frequencies***.

<table>
<thead>
<tr class="header">
<th><em><strong>Input Array</strong></em></th>
<th><em><strong>Returned Sum</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>{ 1, 2, 3, 2, 7, 3, 4, 4, 5, 5, 4, 5, 1, 6, 1, 1 }</p>
<p><em><strong>Occurrence Dictionary</strong></em></p>
<table>
<thead>
<tr class="header">
<th><strong>Key</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
</tr>
<tr class="odd">
<td>3</td>
<td>2</td>
</tr>
<tr class="even">
<td>7</td>
<td>1</td>
</tr>
<tr class="odd">
<td>4</td>
<td>3</td>
</tr>
<tr class="even">
<td>5</td>
<td>3</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1</td>
</tr>
</tbody>
</table></td>
<td><p><span class="math inline">4 × 1</span> <span class="math inline"> + 2 × 3</span> <span class="math inline"> + 1 × 6</span> <span class="math inline"> + 3 × 5</span> <span class="math inline"> = 32</span></p>
<p><em><strong>Max Dictionary</strong></em></p>
<table>
<thead>
<tr class="header">
<th><strong>Key</strong></th>
<th><strong>Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>4</td>
<td>1</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
</tr>
<tr class="odd">
<td>1</td>
<td>6</td>
</tr>
<tr class="even">
<td>3</td>
<td>5</td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="even">
<td>null</td>
<td>0</td>
</tr>
</tbody>
</table>
