Solution for the [friday-puzzle-241](http://richardwiseman.wordpress.com/2014/01/20/answer-to-the-friday-puzzle-241)
------------------------------------

You take one of the coins out of the box and look at one of the sides.

It's a head. 

What's the probability that the other side also contains a head?

The answer is 2/3.

I was sure it is 1/2 but [Ken Haley](https://www.facebook.com/ken.haley.98) convinced me
in his [comment](http://richardwiseman.wordpress.com/2014/01/20/answer-to-the-friday-puzzle-241/#comment-133886):

      I knew this would generate a lot of discussion. Those who still think the answer
      is 50/50, try it. Put two pennies in a bag and mark one of the tails (with a little
      scratch or magic marker) indicating it should be a heads. Shake the bag and remove
      a coin and observe one side. If it's tails (the one you didn't mark), don't count
      that trial–we're only interested in cases where you see a head. Otherwise, turn
      the coin over and record whether it's heads or tails. Repeat 100 times, and see
      if the number of heads you get is closer to 50 (1/2) or 67 (2/3).

But to prove it, I wrote a little [python program](coins.py)

A typical result of the program is:

    the experiment was done 10000 times but we accepted only 7543 cases where the coin was H
    the probability of Head = 66.9%


If you want to run the code, [paste it into](http://www.compileonline.com/execute_python_online.php)
