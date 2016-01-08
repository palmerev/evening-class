# Algorithms
<dl>
<dt>Algorithm</dt><em>noun</em>
<dd> a process or set of rules to be followed in calculations or other problem-solving operations, especially by a computer.</dd>
</dl>

An algorithm is a process for solving some problem that takes some input and gives some output. Studying algorithms helps us hone our ability to understand different kinds of problems and describe solutions in ways that can be executed reliably. You have your own algorithms for brushing your teeth or making a sandwich, but describing the steps involved to a computer may be more difficult than it first appears.

There are two key aspects of algorithms to consider:
  - Correctness: _Does is solve the problem?_
  - Efficiency: _How fast is it?_

## Searching
There are a few ways to approach searching a collection or list of items. Consider this situation: You're looking up your friend John Smith's name in a phone book (look in the white page's for someone's personal phone number):

![phone book](http://hereandthere.us/wp-content/uploads/2010/10/PhoneBook.jpg)

What are some strategies?

You could start at the beginning and go page by page. Will you eventually find him this way? Yes.

But is there a better way?

Maybe you try every flipping every _two_ pages. You can now get through the entire phone book in _half_ the time. Will you eventually find him this way? Maybe. Unless he happens to be sandwiched between the two pages you just flipped. This algorithm is more efficient, but not reliably correct.

Instead you may find the idea of starting at the beginning of the phone book ridiculous, since you know that John Smith's name will be somewhere in the middle. So you start in the middle. If you end up in a section before 'S', you know to look in the section right (later) half. Otherwise, you look in the left. Then you repeat this process with whatever section remains.

***

The first two approaches demonstrate **linear search**, examining pages in order from beginning to end. The last approach demonstrates **binary search**, which uses a strategy that eliminates portions _half_ of the remaining pages each time. The power of dividing input in half each time makes binary search a very efficient algorithm. Let's understand why:

_What if more pages were added to the phone book so that it doubled in size?_

Say the phone book has 2000 pages instead of 1000 Using linear search, you'd have 1000 more pages to flip through in the worst case. However, using binary search, how much more would you need to do? You could start in the middle of the book, and with only _one_ more halving, arrive at the same answer. If the book doubled in size again the next year, you'd only have to do _two_ more halvings.

As the input gets even bigger, the time it takes to perform these two searches diverges even more. Until we get curves that look like this:

![plot of linear vs logarithmic growth](http://www.equestionanswers.com/c/images/log2n.gif)

The x-axis `n` represents the input size, and the y-axis `f(n)` represents the time that an algorithm `f` takes to perform. Linear search grows proportional to the input size, so the growth curve is **linear** (in blue). Binary search uses the strategy of dividing input in half. It turns out that the number of times a number can be divided in half is the log<sub>2</sub> (from here on, just "log") of that number.

#### Logarithms


A logarithm is the opposite of exponent. For example two to the third power is an exponent: 2<sup>3</sup> == 2 x 2 x 2 == 8. log<sub>2</sub>(8) essentially asks the question: "To what power do I raise 2 to get 8?" Based on the previous example, the answer is 3. log<sub>2</sub>(8) is 3, log<sub>2</sub>(16) is 4, log<sub>2</sub>(32) is 5, and so on.
Doubling the input to log<sub>2</sub> gives a number one larger. Sound familiar?

The big idea is that the execution time of log(n) algorithms grows _very slowly_, which means that they're great for dealing with large data sets.

#### Big-O Notation

When looking at the efficiency of an algorithm, we can consider the best, worst, or average case performance. The worst case performance is almost always of greatest concern because we don't tend to guard against things going better than expected. :) We also don't tend to care so much about the absolute runtime of the algorithm as how fast the runtime increases as the inputs get very large.

Often worst case performance is denoted with a capital 'O', or big-O, along with the order of growth:

`O(n), O(log(n))`


Pseudocode for Binary Search:
```
1. Let min = 0 and max = n-1.
2. If max < min, then stop: target is not present in array. Return -1.
3. Compute guess as the average of max and min, rounded down (so that it is an integer).
4. If array[guess] equals target, then stop. You found it! Return guess.
5. If the guess was too low, that is, array[guess] < target, then set min = guess + 1.
6. Otherwise, the guess was too high. Set max = guess - 1.
7. Go back to step 2.
```

## Sorting

**Selection Sort**
Selection sort works by finding the next-minimum element of the list on each pass over the list and putting it in the proper place.

```
for i until the last element:
    min = i  # assume i is the minimum to start out
    for j greater than i:
      find the minimum
    if min != i:  # if min isn't already in the right place
      swap(i, min)
```



**Sources:**

https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/implementing-binary-search-of-an-array
