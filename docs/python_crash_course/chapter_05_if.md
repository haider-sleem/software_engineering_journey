Note 1: 
The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data. 
If you have a specific final condition you’re testing for, consider using a final elif block and omit the else block. 
As a result, you’ll be more confident that your code will run only under the correct conditions.

---------------------------------------
Note 2: 
However, sometimes it’s important to check all conditions of interest. 
In this case, you should use a series of simple if statements with no elif or else blocks. 
This technique makes sense when more than one condition could 
be True, and you want to act on every condition that is True.

In summary, 
if you want only one block of code to run, use an if-elif-else 
chain. If more than one block of code needs to run, use a series of independent if statements.

-----------------------------------------
Note 3:
You learned to handle certain items in a 
list differently than all other items while continuing to utilize the efficiency of a for loop. 

You also revisited Python’s style recommendations to ensure 
that your increasingly complex programs are still relatively easy to read and understand.