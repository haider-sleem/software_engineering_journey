

0:00
[MUSIC PLAYING]
Loops
0:24
DAVID MALAN: All right. This is CS50's Introduction to Programming with Python. My name is David Malan, and this week we focus on loops, this ability in Python
0:33
and a lot of other programming languages to do something again and again, a cycle of sorts.
0:38
And let's see if we can't begin by motivating exactly why we have this ability to do things cyclically using these loops.
0:45
I'm going to go ahead here and open up VS Code. And in my terminal window, let's go ahead and create via code cat.py, a Python program that meows like a cat.
cat.py
0:57
And I'm going to go ahead here in this Code tab, and very simply, perhaps, I'm going to start by implementing this cat just by using print.
1:03
We're going to have this cat not make audible sounds, but just print meow, meow, meow on the screen three times.
1:08
Well, I think the simplest way I can do this is just to print meow once, and to print meow again, and to print meow one last time on the screen.
1:18
And now let me go down to my terminal window, let me run Python of cat.py, Enter, and meow, meow, meow.
1:25
All right, so this program works. This program indeed works if my goal is to get the cat to meow three times.
1:31
And let me propose, just to help us wrap our minds around what's going on inside of the computer, let
1:36
me propose that we consider this flowchart. So as before, we have this flowchart that starts with this oval, which just means start reading here.
1:44
And then notice, it goes via arrows to a meow, meow, meow, and then it stops.
1:50
It's perfectly correct, and honestly, it's wonderfully simple, but I daresay we can find fault with my code nonetheless.
1:58
Why is my code arguably poorly designed?
2:03
Now the answer is going to be loops in some way, but let's see if we can identify in what way the code is actually poorly designed in some sense.
2:12
Let's see. Any thoughts. Alex? AUDIENCE: OK. So, I mean, repeating the same action like three times or even more
2:21
is not a good habit. DAVID MALAN: Yeah, I'm just repeating myself. And honestly, it's not that big a deal.
2:27
If we go back to my code here, am I really doing such a bad thing by just printing meow, meow, meow three times?
2:34
Not really, but let's consider the logical extension of this. Suppose I wanted to meow four times or five times or 50 times or 500 times.
2:43
Do you really think, even if you've never programmed before, is the solution to this problem really going to be to hit copy-paste 50 times?
2:50
Like probably not. We can probably do better than that. And beyond it just being ugly at that point, having so many lines of identical code, just
2:57
imagine if you wanted to change the code. Maybe I change my mind and I don't want to make a cat, I want to make a dog. So now it has to say woof, woof, woof multiple times.
3:04
Now I have to change that in 50 different places. And yeah, sure, I could do find and replace,
3:10
but come on, like we're programmers now, there's got to be a better way than just repeating ourselves.
3:15
So I bet we can do better than that if we think about a little harder how we go about structuring this program.
3:22
And we can do that if we augment our vocabulary just a little bit. It turns out in Python, and in other languages,
while
3:28
too, there's a keyword called while. And while is one way that we can express what's called a loop,
3:34
a block of code that's going to do something again and again and again-- 0 times, 1 time, 2 times, 50 times, as many times as we want.
3:43
But while rather leaves to us the particulars
3:48
of how we express ourselves to do something again and again. So let me go back over to VS Code here and let me propose that I do this.
3:56
While is a construct that allows me to ask a question again and again.
4:01
And any time we've seen a question, it's been in the form of a Boolean expression, a question to which the answer is
4:07
true or false. Well, how could I do this? How could I print out meow three times and ask three times a question
4:15
to which the answer is true or false? Well, what if I did some counting? Like literally on my fingers.
4:21
And if I'm trying to count maybe down from three, I want to meow three times, I can put three fingers up and I can meow.
4:28
And then I can put like one of the fingers down and then meow. And I can put one of the fingers down and I can meow.
4:33
Put one of the fingers down. And maybe the question I can ask every time I meow is, do I have any fingers up still?
4:40
Do I have any fingers up still? Do I have any fingers up still? And if the answer is true, keep going. If the answer is false, stop.
4:48
So how can I translate that to code? Well, once we've added this while keyword-- I think we have all the building blocks already, let me propose that I do this.
4:57
Let me propose that I give myself a variable. And I'll call it i for integer, but I could call it anything I want,
5:02
and I'm going to initialize it to 3. Then I'm going to use this new feature of Python, while,
5:07
and I'm going to ask a question, the answer to which must be true or false. And I'm going to say, while i does not equal 0.
5:17
So I'm going to ask the question, while i does not equal 0, do the following.
5:22
Notice the colon at the end of the line. Notice my indentation. And just like with functions, just like with conditionals,
5:28
you indent the lines that you only want to execute as part of this other thing.
5:34
What do I want to do while i does not equal 0? Well, I think I just want to meow.
5:41
But it's not enough just to write this code. If I were to very dangerously run Python of cat.py and hit Enter right now,
5:52
what might happen on the screen? Whether you've programmed before or not.
5:58
Why is this a very bad thing potentially? It's not going to break things, but it might lose control of my computer
6:05
somehow. Any thoughts? Yeah, Timo? AUDIENCE: Hi.
6:11
I think it's going to continue to print out meow since i is always equal to 3
6:18
and the while is always true. DAVID MALAN: Yeah, exactly. If I'm initializing i to 3-- that is, setting it equal to 3 on line 1,
6:26
then I'm asking the question, while i does not equal 0, and that's going to be true, it does not equal 0,
6:31
it obviously equals 3, print meow. And the way a while loop works is that the Python interpreter just
6:38
keeps going back and forth. It goes from line 1 to line 2, then to line 3,
6:45
and then it goes back to line 2 to ask the question again. If the answer is still true, it goes to line 3.
6:50
It then goes back to line 2. If the answer is still true, it goes back to line 3. And to Timo's point, if you're never actually changing the value of i,
7:00
it's always 3, you're just going to be looping literally forever, and this is an accidental infinite loop.
7:07
So we've got to be smarter than that. And I'm not going to hit Enter because I don't want to lose control over my computer here such that it's
7:12
printing out meow forever. Fortunately, if you ever do do that and you find yourself in an accidental infinite loop, Control-C for cancel or interrupt
7:21
is going to be your friend. If you ever seem to lose control, you don't need to reboot or turn off the computer.
7:27
You can just hit Control-C in your terminal window and that will likely fix it.
7:32
All right, well what do I want to do, then, after meowing each time? I think what I'd like to do here is maybe something like this.
7:39
Let me update i to equal whatever the current value is minus 1 here--
7:46
whoops, sorry. Minus 1. So if i on each iteration-- I'm updating i to be one less, one less, one less,
7:55
it should eventually hit 0, at which point the answer to 9.2's question
8:00
will now be false. So let's see if this works. I'm going to go down to my terminal window and run Python of cat.py,
8:06
and I indeed get three meows. Why? Because I've wired this up like a machine in software, if you will.
8:14
I've set i equal to 3, then I keep asking this question. But I keep turning the gears, I keep changing the value of the variable
8:21
to make sure that ultimately it is actually being decremented-- that is, decreased by 1 until we eventually hit 0.
8:30
Now for those of you who think I'm a little more graphically, let me pull up one of our usual flow charts. This is just a representation graphically of the exact same thing.
8:38
Notice what's happening. I first start the program, and then I initialize i to 3,
8:44
and then I ask the first of my questions. Again, the diamonds always represent questions. And the answer is going to be true or false.
8:50
Does i not equal 0? Well, it doesn't, it equals 3. So if I follow the true line, I meow.
8:56
And then I follow this arrow, and I update i to equal i minus 1. At this point in the story, i presumably equals 2 mathematically.
9:05
I follow the arrow. And there's the loop. This is why it's nice to see this graphically, perhaps because you can literally see the loop back and forth.
9:12
Now I ask the question again. Does 2 not equal 0? Well, it does not equal 0, it's 2, so we meow again.
9:20
We change i from 2 to 1. Well, does 1 not equal 0? Well obviously 1 is not 0, so we meow again.
9:27
We decrement i again. i is now 0. Does 0 not equal 0?
9:33
No, it equals 0, so the answer is false and we stop. So there, perhaps more so than any of our flowcharts before,
9:41
do you really see the structure of what's happening inside of the program? And you don't have to get into the habit of making these charts
9:47
or creating these charts, but just as a first pass at what's going on inside of the computer, that's indeed one way to visualize it instead.
9:55
Well let me propose that, like always, there's many different ways to solve this problem. And suppose you just like to think a little differently.
10:01
Maybe you don't like starting at 3 and then counting down to 0. Why? Maybe you're just brain doesn't work that way
10:07
and you prefer to count up instead of down. Totally fine. Let me go ahead and change my code here to set i equal to 1 instead of 3.
10:15
And here, let me just change my logic. Rather than checking for not equal to 0, like maybe you don't like thinking in terms of not because it's a little confusing,
10:23
and it might be, let's just check that i is less than or equal to 3.
10:28
So we'll be a little more explicit. We'll count from 1 up through 3, each time printing meow,
10:34
but I'm going to need to change this line here. Let me see if we can't call on someone to change line for me.
10:40
How do I want to change line 4 to be consistent with counting from 1 up
10:47
to and through 3? AUDIENCE: I would be plus 1 every time you meow.
10:57
DAVID MALAN: Yeah, exactly. In this case, we want to add one not subtract 1. And in fact, if you think about this, this 2 could end very poorly.
11:05
If you start counting at 1 and you keep subtracting 1, subtracting 1, subtracting 1, I think we're going to find ourselves
11:11
with the same problem, which is that we're never going to stop because we're going to keep getting more and more negative as opposed to ever getting up
11:19
to the number 3. So I think you're right, I need to change this to be i equals i plus 1.
11:24
And now notice just for clarity, too, the equal sign is, again, our assignment operator from right to left.
11:30
Logically, this might otherwise strike you as strange. Like how can i equal itself plus 1?
11:35
Well, it doesn't until you execute this code from right to left. You add 1 to i or you subtract 1 from i, and then you update the value of i
11:44
on the left. The assignment copies the value from the right to the left. Well, how else might I do this?
11:49
Well, I will say that most programmers, computer scientists more generally,
11:55
tend to start counting from 0. It's a convention and it actually has upsides even in Python and other languages where generally speaking,
12:02
it's a good thing to start counting from 0 instead of counting like we might in the real world from 1.
12:07
Let's go ahead and adopt that convention now. Let me set i equal to 0, and I need to make a change now.
12:14
Notice, if I don't change my logic, this program just became buggy.
12:19
The cat has a bug. It's now meowing four times if I run it as is. But the easiest fix here would be to change my inequality
12:27
to be this, less than instead of less than or equal to. Now I'm starting at 0, but I'm going up to but not through 3.
12:36
And even though this might, of all the things we've seen thus far, seem maybe the least familiar, most of us might start at 1, 2, then 3,
12:44
it's a good habit to get into now, start at 0, and go up to but not through the value that you care about ultimately,
12:52
3 in this case here. Well, let me tighten things up a bit here. Not only will this now fix my counting problem,
12:57
it now meows 3 times as expected, there's a more succinct way to express i equals i
13:03
plus 1, and this, is because it's such a popular thing to do in code. You can instead just say i plus equals 1, and that's it.
13:11
You don't need to put everything on the right-hand side. This is a special syntax that says the exact same thing, increment i,
13:19
but it does it with a few fewer keystrokes. It's just a little more pleasant to type, it's a little faster to read,
13:24
it's just a convention. Those of you who have programmed in C, C++, Python--
13:29
no, not Python. C, C++, Java, JavaScript might have seen plus-plus before or minus-minus.
13:36
Sorry, Python doesn't have it, so you cannot use that. This is as succinct as your line of code might get.
13:44
All right. Let me pause here to see, then, if there's any questions about these implementations of while loops.
13:53
AUDIENCE: Can we use stuff like for loops which have a certain i-value initialized to it at the start
14:02
and it runs from the particular condition you put into the thing
14:09
and increment it as you go along? DAVID MALAN: Short answer, no, you cannot do what you're describing,
14:15
but there is another type of for loop that we will soon see. But let's come to that in just a moment. Other questions on loops using while here?
14:26
AUDIENCE: So I had a question about that flowchart. DAVID MALAN: OK. AUDIENCE: There were-- yeah. There were certain symbols for the certain kind of the statements were--
14:36
are they certainly used for that kind of statement that they--
14:42
DAVID MALAN: They are. So I deliberate-- I deliberately use certain types of symbols, certain shapes
14:47
here whereby an oval is conventional for start and stop. I used rectangles for any statement of code, like an assignment or a printing
14:56
and so forth. And I used diamonds to represent questions that you might ask,
15:02
conditions as we've seen. If you're doing this for yourself, if you're just trying to make sense of your code and writing it down,
15:07
you certainly don't need to use these formal symbols, but I tried to be consistent with some best practices.
15:13
And in fact, let me come back to the same picture, because this was the first version of our picture, but we've since modified our code a couple of times.
15:19
This, recall, was the version where the question we were asking was i not equal to 0, let me go ahead and just change this code now
15:26
to represent the next version we did, which, recall, changed our logic to start counting from 1,
15:31
it changed our question to check as i less than or equal to 3, but then everything else was the same except for the counting, which
15:39
is now plus instead of minus. And then we refined it a little bit further by counting now from 0 up to
15:47
but not through 3. And we tightened up this code here by just incrementing 1
15:52
by using the slightly more succinct syntax. So at this point, these flowcharts might become less and less useful for us, because once you've wrapped your mind around the concept
16:00
and hopefully the picture helps bring that concept to life, it certainly fine to focus entirely on the code
16:06
and only think about or even draw something like this if you need to wrap your mind around something more complicated
16:12
than you're used to. Well, let me go ahead, if I may, and propose that we transition to another approach of types of loops using another
16:20
keyword here, namely a for loop. And this is a word that does exist in other languages, but doesn't necessarily have as many features as other languages might
for
16:28
use it for. But there is a different type of loop-- not a while loop, but a for loop.
16:33
And a for loop is going to allow us to express ourselves a little differently, but to do so, I propose that the easiest way
16:40
is if we introduce one other idea in Python, which is that of a list. And here, too, no pun intended, we're adding to the list of data types
16:48
that Python supports. We've seen strs or strings. Ints or integers. Floats or floating point values.
16:54
Bools or Boolean expressions. Python also has lists, which is another type of data,
17:00
but wonderfully, this one is probably pretty familiar. A list of things in the real world is a list of things in Python.
17:06
It's a way of containing multiple values all in the same place, all
17:11
in the same variable. So what do I mean by this? Well let me propose that we go back to our VS Code here,
17:18
and let me start fresh with my code here and not use a while loop at all, but let me use this new keyword for.
17:24
The way for loop works is that it allows you to iterate over a list of items.
17:30
So what does this look like? It might look like this-- for i and the following list of items, 0, 1, 2.
17:39
This is my starting point, and on each iteration of this loop-- that is, on each execution of this loop again and again,
17:45
I want to print out meow. Now I'll admit, I kind of like the look of this code already
17:51
even though there's some new syntax here, because it's just shorter than the while loop. The while loop had multiple lines a moment ago
17:58
and it was entirely up to me to decide what i is. I have to check a condition, I have to increment or decrement i.
18:04
Like I was doing a lot of work, relatively speaking, to make that thing turn, to make that loop going to go.
18:10
It was very mechanical in a sense. You can in your mind's eye maybe see the gears turning as all of these variables
18:18
are changing and these questions are being asked. A for loop simplifies all of that, and it just
18:24
says, if you want a variable like i, a number, and you know in advance how many times want this loop to execute-- three
18:31
times, we'll just kind of specify what it is you want i to take on as values explicitly.
18:37
In this loop, i will be automatically initialized by Python to be 0, then meow will be printed.
18:43
Then Python would automatically update i to equal 1, then meow will be printed.
18:48
Then Python will automatically update i to be 2 and meow will be printed. And because that's it for the values in that list, Python will stop
18:57
and it will only meow a total of three times. What is the list? The list in this program is exactly that, 0, comma, 1, comma, 2,
19:05
and notice the square brackets. Those aren't parentheses, those are square brackets that represent a list.
19:11
That's how visually as the programmer-- that's how Python knows as the language that you intend for that to be a list.
19:18
So let me go ahead and run this Python of cat.py, and it works just the same.
19:23
But it's only two lines. It's pretty readable once you have familiarity with that construct, but to my constant point about correctness not necessarily
19:33
being the same as design, in what sense is this program perhaps poorly designed?
19:40
It seems to work. It meows three times, but why might this not
19:45
be the best way to solve this problem? Even if you've never programmed before, again,
19:51
think about corner cases, things that may or may not happen. Think about extreme cases that really test the quality of this code.
19:59
AUDIENCE: OK. I think that because we are saying 0, 1, 2 3 times.
20:06
And then if you want to take a million, you say 1, 2, 3. DAVID MALAN: Yeah, exactly.
20:12
And that's what I mean about thinking about the extreme cases. If you're trying to decide for yourself if your own code is good
20:18
or someone else's code is good, it might look so at first glance, but think about the extreme.
20:23
Well, what if it's not three things, it's a million things? I mean, are you really going to write out 0 through a million or 0
20:31
through 9-- 999,999?
20:38
Like no, you're not going to write that many numbers on the screen there's got to be a better way. So let's do the better way from the get-go
20:45
rather than set the stage for doing something poorly. And the one way we can solve this problem to improve the design
20:52
is don't just manually specify the list of values, use a function, someone else's function that comes with Python
20:59
that gives you the list you want. And the easiest way to do that in Python is to use a function called range that returns to a range of values.
21:07
It expects as input at least one argument, and that number is going to be the number of values you want back.
21:14
Those values are going to start at 0 and go to 1, to 2, and so forth, but they will go up two but not through the number you specify.
21:22
So by specifying range 3, you're essentially being handed back 1, 2, 3 values.
21:29
And by default, those values are 0, 1, and 2, and that's it. But what's brilliant about this is that now, to Hope's point, if I do
21:37
want to meow a million times-- I mean, that is an angry cat, I can now do a million by just typing a million.
21:44
I don't have to literally type 0, comma, 1, comma, 2, comma, 3, comma, 4, all the way up to 999,999, I just do this.
21:53
So that's got to be a better way long-term. So that's indeed one improvement we can indeed
21:59
make here still using a for loop, but now using this range function. And just to show you something else that's Pythonic--
22:05
this is not strictly necessary, but it's commonly done, there's a minor improvement we can make here,
22:11
even if we're just meowing three times. And notice that even though I'm defining a variable i, I'm not ever using it.
22:20
And it's kind of necessary logically, because Python, presumably, has to use something for counting.
22:26
It has to know what it's iterating over. But there's this convention in Python where if you need a variable, just because the programming feature requires
22:35
it to do some kind of counting or automatic updating, but you, the human, don't care about its value, a Pythonic improvement here
22:42
would be to name that variable a single underscore. Just because it's not required, it doesn't
22:48
change the correctness of the program, but it signals to yourself later, it signals to colleagues or teachers that
22:54
are looking at your code, too, that yes, it's a variable, but you don't care about its name because you're not using it later,
23:00
it's just necessary in order to use this feature, this loop in this case here. So just a minor improvement or change there.
23:09
But to really gets you intrigued by what's possible in Python, let's take this one step further.
23:15
So if we really want to be Pythonic, this one, if you've programmed before, is kind of going to blow your mind, so to speak,
23:22
whereby if I want the cat to meow three times, what if I actually do this?
23:27
print, open parenthesis, quote-unquote, meow times 3.
23:34
You have to be kind of a geek to think this is cool, but this is kind of cool. So you can literally just print what you want,
23:40
multiply it by the number of times that you want it, and you will get back exactly that result.
23:47
Now I've kind of made a mistake here. So let's see what this does. It's not quite as beautiful as this code might look to you-- to some of you,
23:56
to me. Let me run Python of cat.py, Enter. OK, it's a really like hungry cat or something.
24:02
It's meowing really fast. But I can fix this, I bet. Let's think about now some of the basic building blocks we've discussed.
24:10
The problem is clearly that literally meow, meow, meow is being repeated three times, but it's not as pretty as I want it.
24:16
I want it to be meow, meow, meow on separate lines. What might be a possible solution here while still
24:22
using this multiplication operator? And think back. We've used plus to concatenate strings.
24:30
You can apparently use multiplication to concatenate strings, but more than once again and again and again.
24:35
How could I clean this up without reverting to my for loop or my while loop and still use multiplication in this way?
24:42
AUDIENCE: We can use the escape sequence which would be backslash n. DAVID MALAN: Amazing. Yes.
24:47
Think back to backslash n, which is the way you as the programmer can express a new line in code.
24:52
And I think, if I take your advice, I put a backslash in there inside of my quotes, so that at the end of every M-E-O-W, there's a new line,
25:02
let's see how this looks. Let me clear my screen and run Python of cat.py. OK, so close.
25:08
I like this. Let me call on someone else. The only thing I don't like-- and I know I'm being really nitpicky now--
25:13
is that it's meow, meow, meow on separate lines, but there's this extra blank line, which I'm just not loving aesthetically.
25:20
AUDIENCE: I think we can make n equal to column--
25:25
column, not-- like a slash n. DAVID MALAN: Yeah. So here, too, like all of these things we've seen in past weeks
25:31
are kind of coming together. Recall that the print function lets you control what the line ending is.
25:37
By default, it's backslash n itself. Which is why at the very end of this print, the cursor is being moved again to the next line.
25:44
Well, we need to just override that. So let me go into my code here and let me change this to comma n
25:50
equals quote-unquote so that it's no longer the default backslash n, it's instead now going to be nothing whatsoever.
25:59
That should eliminate, then, hopefully that additional blank line. So let me run this one last time here, Python of cat.py, Enter,
26:07
and there we have it. So now, at least as programming goes, it's kind of cool that I can distill this into a short line
26:15
and express myself all at once. Now to be fair, it's a little less readable. Like now I've got backslash n, I've got times 3,
26:21
I've got n equals quote-unquote. So you don't have to do things this way. My previous approach with a for loop, totally fine.
26:28
My previous approach with a while loop, totally fine, and in some sense, perfectly well-designed.
26:33
But this is just yet another way to do it, but it's not a good thing if you or your teacher, your colleague, your friend
26:40
are going to struggle to read your own code. But this is a feature of Python that some languages do not, in fact, have.
26:47
All right, well let me propose that things get more interesting still if we're not just meowing three times only,
26:53
but we're meowing some variable number of times. Let's ask the user how many times this cat should meow.
26:58
So let me clear the screen here, and let me figure out, well, how do I get a number from the user?
Validating Input
27:05
The catch here is that if I want the user to give me a number, I'm not doing math, per se, I'm meowing, and therefore, the user
27:12
has to give me a positive value. The user has to give me a positive value. So how can I insist on this?
27:18
Well, if I just do this, n equals int of input, what's n, question mark?
27:25
Well, I want to check like-- I could say if n is less than 0--
27:32
like if it's negative, well I could do this. Well, then ask again. Int, input, what's n, question mark?
27:40
OK, well what if the user still doesn't give me a positive number? What if being really difficult they're not paying attention
27:45
and they typed in two negative numbers? Well, if n is less than 0, well, let's do it again. n equals--
27:53
this does not end well. You can't infinitely many times keep checking, is it negative,
27:58
is it negative, or is it negative? The program would never be done written. So we can do this I think better maybe with a loop.
28:05
So let me propose this. A very common paradigm in Python, when you want to get user input that matches a certain expectation you have,
28:14
that it's all positive, that it's all negative, or just something like that, you just immediately say while true.
28:20
You deliberately, and a little dangerously but a very conventionally, induce an infinite loop.
28:25
Now what is an infinite loop? It's just one that goes forever. And we've seen how that can happen accidentally mathematically.
28:31
It's absolutely going to happen when you say while true. Why? Well, the answer to the true question is always true.
28:39
So this is a way of deliberately inducing a loop that by default is going to go forever. So we're going to need a way of breaking out of this loop when
28:46
we have the number we want. The convention, though inside of this otherwise an infinite loop is to ask the question you care about,
28:52
like give me an int by prompting the user for input. Like what's n, question mark? And then just ask your question.
28:59
So if n is less than 0, then I think we want Python to just continue
29:04
to prompt the user again. That is, we want the code to stay in the loop, recall the input function,
29:09
and hope that the user gives us a better answer. If this time around it's less than 0, so let's just literally use Python's keyword continue, which says
29:16
just that-- continue to stay within this loop. Else, if it's not less than 0, let's go ahead and just break out
29:24
of the loop altogether using another keyword in Python, break. Break will break you out of the most recently begun loop in this case
29:31
if it's not the case that n is less than 0. So this will work, and it will allow us to get a value that 0 or greater
29:38
from the user, but I think we can tighten it up further so as to not bother having an if, and, and else.
29:43
Why don't we instead just say, if n is greater than 0, go ahead and break?
29:49
In fact, it's not that interesting a program if we even allow the user to type in 0. So let's wait until they give us an integer that is greater than 0
29:56
and then break out of this loop. And what can I now do down here? For i in range of whatever that value n is, print meow.
30:07
And honestly, I don't need i here, so let me come back to that principle before. And let me just change it to an underscore
30:12
just to be Pythonic, if you will. So what's going on? Lines 1 through 4 deliberately implement an infinite loop
30:20
that otherwise by default is going to go forever. But I'm asking a question, inside of that loop,
30:26
after getting an int from the user on line 2, I'm then checking, is it greater than 0?
30:32
Or is it 0? Is it negative? None of which makes sense for meowing cat. Like I want the cat to meow at least one time.
30:38
So if it is greater than 0, break. And this break statement, even though it's indented, indented twice,
30:45
has the effect of breaking out of the most recently begun while loop.
30:50
So once the user gives you a positive value, then we get to line 6, at which point we meow that many times because
30:58
of line 6 and 7. So if I run this now Python of cat.py, Enter, well, what's n?
31:03
Let's start with 3 where we began, meow, meow, meow. Well this time, let me go ahead and increase the size of my terminal window
31:10
just temporarily. Let me run Python of cat.py, let me do it 10 times, meow 10 times now
31:16
appears on the screen. And the takeaways here are not just that we can meow 10 times or do something again and again, but this
31:22
is a very common paradigm in Python when you want to do something again and again and again, but only until the user actually gives you
31:31
a value that you care about here. And let me propose actually now that we practice
31:36
a little more what we've been preaching, especially when it comes to, say--
31:41
especially when it comes to say writing your own functions. Now that I'm doing all this meowing, it might
31:46
be nice to actually have a meow function that the inventors of Python didn't envision, so let me do this.
31:52
Let me actually get rid of all this code and let me go ahead and do this. Let me go ahead and say define a main function, as I've done before,
31:59
and let me just blindly call meow 3. Meow doesn't exist yet, but when it does, that'll be great.
32:05
So let me go ahead now and define meow. So am I meow function should take as input
32:11
a parameter called n or anything I want, and this part's pretty easy now. How do you meow n times?
32:17
Well, for underscore n, the range of n, go ahead and just print meow. So same code as before, nothing new here,
32:24
I'm just putting that logic inside of a meow function that's going to have this side effect of printing meow.
32:30
And now, as before, let me go down here and let me make sure I call main. And if I now run this code, Python of cat.py, meow, meow, meow.
32:39
It's always going to do three because I've hardcoded to 3. Well, let's make one improvement here.
32:44
Let me go ahead now and maybe do this. Let me ask the user for a number.
32:50
So let's say something like this, number equals get number. All right. Unfortunately, there is no function in Python
32:57
called get number that gets a positive number from the user, but I can invent that. So define get number, open paren, close paren.
33:05
And then inside of this function, let me do this. While true, go ahead and get a number from the user,
33:11
converting it to an int asking them, what's n, question mark? And then if n is what I want, it's a greater than 0 value,
33:19
a positive number, I don't want to break this time necessarily,
33:24
although I could. I instead want to return the value so I can actually do this instead.
33:30
And this, too, is a feature of Python. This ability not to just break out of a block of code, but also to return a value in code.
33:38
To actually return a value gives you the ability, ultimately, to return explicitly a value so that your function has not just a side
33:47
effect, necessarily, but it actually hands back, just like input does, just like int does, just like float does, an actual value to the user.
33:56
Now to be clear, I don't have to return n here. I can still break out of the loop as I've done in the past with code
34:02
like this, but then after the loop, I still have to return. And so what's happening here is that if you use break to get out of the loop,
34:10
but you need to hand back a value from a function, you still have to use the return keyword now
34:15
explicitly either in the loop as I did or now outside of the loop but still inside of the function.
34:24
The last thing I'm going to do here now is change that 3, which we hardcoded earlier, to actually be the value of the variable we've gotten from the user
34:31
so that now down here, if I run Python of cat.py, Enter, what's n? I can type in 3, I get my three meows, or if I only want one,
34:40
I now get one meow instead. All right. So if we now have this ability to do things again and again in these loops,
34:48
let's see if we can't solve some other problems via which to express ourselves cyclically, but get back some interesting answers as well.
34:55
And let me propose, for instance, that we look a little more closely at these lists. It turns out that in Python, and really, in programs in general,
Iteration with Lists
35:03
it's useful to have a list of values, because we're going to be able to work with more and more data, larger and larger data sets.
35:10
So let me propose that we come back to VS Code here and let's do something that's perhaps a little familiar to some folks,
35:15
the world of Hogwarts. And let me go ahead and code up a file called Hogwarts, and let's see if we can't have a list of students at Hogwarts here.
35:23
So I have a new tab called hogwarts.py. and let me go ahead and propose that I just define in this program
35:30
a list of students whose names I know in advance. So I'm not going to get user input for now. I'm just going to know from the get-go that the three
35:37
students I want to consider are these. Our variable is going to be called students. It's going to equal, as I've done in the past, a square bracket, which
35:44
means, hey, here comes a list. And those values are going to be Hermione in quotes, because it's a string; Harry in quotes, because it's a string; and then Ron in quotes,
35:53
because it's a string as well. So this is a list of length 3. It's similar in spirit to my list of length 3 earlier,
36:00
but that had 3 ints, 0, 1, 2. Now I have a list of three strings instead.
36:06
And this isn't very useful at the moment, but let me just do something as a check for myself.
36:11
Let me print out each of these students. Well wait a minute, how do I print the contents of a list?
36:19
Well, in the past, when we've printed a variable, we've just printed out the name of the variable.
36:24
But I don't want to print out all of Hermione and Harry and Ron all at once. Maybe I want to print out Hermione first, then Harry, then Ron.
36:33
So I need a way to express more precisely which value do I want from this list? And the way you do this in Python is you use square brackets in another way.
36:42
If you have a variable-- in this case, called students, and you want to go inside of that variable and get a specific value--
36:49
that is to say, you want to index into the list, you use square brackets this way using numbers inside of the square brackets.
36:57
And here's where we see that it is useful to think and count in terms of 0
37:02
on up instead of 1 on up. These lists in Python are, shall we say, zero-indexed.
37:08
The first item in a list is at location 0, the second item in a Python list
37:13
is that location 1, and the third is that location 2. So you're always kind of off by one mentally, but you get used to it,
37:19
if you've never programmed before, over time. So let me print out all three students. So let me print out students bracket 0, then students bracket 1.
37:27
Then lastly, let me print students bracket 2, and this is my third and final line. And of course, if I run this code, it probably does what you would guess.
37:35
If I run Python of hogwarts.py, there's Hermione, Harry, and Ron each on their own lines there.
37:41
But there's got to be a better way, especially if I don't know in advance who's going to be in this list, if next year there's some new students at Hogwarts,
37:48
we can use a loop to do something automatically without having to manually type out 0 and then 1 and 2.
37:54
Well, here's another feature of Python. You can use a for loop not just to count from 0 to 1 to 2,
38:01
you can use Python to just iterate over anything. Not just numbers, but strings. So I could actually do this.
38:07
For student in students, colon, and then indented underneath that,
38:13
I can say print student. Now it doesn't matter if I have 3 students or 4 or 400,
38:19
these two lines of code, this loop will print all of those students for me one at a time.
38:24
So if I now run Python of hogwarts.py, there's the same list, but I don't need to know in advance how long that actual list is.
38:32
Now notice, I made a conscious decision here. I didn't call this variable underscore, because this time I'm
38:39
using the variable. And while I could do this, now, no, no, no, no, your code is getting way too cryptic.
38:46
If you're naming the variable underscore and you're using the variable underscore, now you're helping no one.
38:51
Now you're confusing the reader, yourself down the line, you should call your variables what they are.
38:57
So a very appropriate name, though I'm sure you could come up with others, would be student, and here, you could say you would stay student as well.
39:04
If you'd prefer to be more succinct, it's not unreasonable to do something succinct in a loop like this. For s in students, using maybe the same letter that the list
39:13
itself begins with, but again, why bother? Python is meant to be more readable. If you have a list of students, iterate over them one student at a time.
39:22
Let me pause here to see if there's now questions about lists as I've now defined them, a list of strings in this case,
39:28
or using a for loop now to iterate over and print each of those names.
39:33
AUDIENCE: Yeah. So is it not necessary to initiate student in this case? Or we can just declare a variable in the loop?
39:40
DAVID MALAN: Good question. You do not need to manually initialize it. Python takes care of initializing the student variable to Hermione
39:47
first, then Harry second, then Ron third. Unlike other languages, you don't need to initialize it to something yourself,
39:53
it just exists and it will work. Other questions on loops and lists in this way?
39:58
AUDIENCE: Since you describe break, so is there any concept of continuing so that we can skip a particular case in loops?
40:04
DAVID MALAN: Yes. You can continue using another syntax as well. We haven't shown that. For now we focused only on break.
40:10
AUDIENCE: OK. So can this for loop work with either hash tables or different kind
40:15
of tables or arrays? DAVID MALAN: Indeed. So we're getting ahead of ourselves there, but there are yet other types of data in Python,
40:22
and indeed, you can use a for loop to iterate over those as well. Anything that is iterable, so to speak, is
40:28
a piece of data that can be used with a loop like this. But more on those-- more on those soon.
40:34
In fact, let me transition here to show just another way of solving this same problem, because up until now when we've used loops,
len
40:40
we really have relied on numbers, and that's fine if you prefer to stay in that space.
40:45
Suppose I did want to iterate using numbers like i and 0, 1, 2, and so forth.
40:50
Let me propose that we could change this code as follows. If you would prefer to think about, or if the program you're
40:56
trying to implement requires that you use numbers like this, you might do this. For i in-- well, I don't want to just say students,
41:04
because then i is not going to be a number. i is going to be literally Hermione, then Harry, then Ron.
41:13
I need to iterate from 0 to 1 to 2. If I a list with three elements has these locations, 0, 1, 2,
41:21
I need to create a loop somehow that starts at 0 and ends at 2. Previously when I wanted to do that, I needed range,
41:28
but this 2 is not going to work. I can't just say in the range of students, because students is not a number, it's not an integer,
41:36
so you can't pass it to range. Range expects an integer. But there is a solution here.
41:41
It turns out that there is a function in Python called length or len, L-E-N,
41:47
that will tell you the length of a list and other things down the line, too. And now I think I can assemble these building blocks and a way that can
41:55
allow me to use numbers in this way. So range doesn't take a list of strings, it takes a number,
42:02
and ideally, that number is going to be 3, so I get a range of values, 0, 1, and 2. So I think I can nest my functions like this.
42:10
If I first get the length of the students list, that's going to be 3, then I pass that return value as the argument
42:18
to range, that's going to give me back a range of values, 0, then 1, then 2.
42:23
And what that's going to allow me to do then in code if I want is not just this. I could do print now students bracket i, and this is now
42:33
where the syntax we're seeing is getting very expressive-- new and perhaps unfamiliar.
42:39
But if I can do open bracket, 0, close bracket, or open bracket, 1, close bracket, or open bracket, 2, close bracket, turns out,
42:47
I can actually put a variable in there and I can express any number inside of those brackets so as to print these all out dynamically in a loop.
42:54
Let me do this, Python of hogwarts.py, Enter, there's Hermione, Harry, and Ron.
43:00
And now if I'm just curious, I just want to poke around or maybe I want to do a ranking, like who are the top three students in the school or in Gryffindor?
43:08
Well, I can print multiple things at a time, we've seen. Let me print out not just the students at location
43:14
i, but rather, let's print i first and then the student at location i. So two things to print, and we know that print can take two arguments,
43:22
we've seen that before, they'll be separated by a space. Let me go ahead and rerun this. Now I see that, OK, Hermione is the top student, but she's in zeroth place.
43:31
That's a little weird. Like we don't need to show the human using my program that we started counting at 0.
43:37
I can clean this up. I can just add 1 to the i up here, and now we see a top three list of students.
43:43
Hermione is number 1, Harry's number 2, and of course, Ron is number 3. So we can get access to all of those same values as well.
43:50
Are there any questions now on these lists? Any questions now on these lists?
43:58
This length, these ranges, or otherwise? AUDIENCE: My question is, for i in range, can you explain this once more?
44:08
DAVID MALAN: Sure. So let me rewind in time. We started off doing this.
44:13
For i in 0, 1, 2, and then we print it out meow three times in that way.
44:20
The way that for loop works is that it creates for you a variable that I've called i, but I could call it anything I want.
44:27
It then assigns i initially to the first thing in the list. It then automatically assigns i to the next thing in the list.
44:34
And then it assigns i to the third thing in the list. And each time it does all of the indented code underneath.
44:41
We realize, though, that this is not going to scale well if I want to do something like a million times. So we introduced range instead.
44:48
That has the effect of doing the same thing. It returns to me a range of values-- a list of three things, really,
44:55
so the behavior is exactly the same. If we now fast forward to this Hogwarts example now, though, what I'm doing
45:01
is just combining these smaller ideas. I'm still creating a for loop. I'm still creating a variable called i.
45:08
I want to do it over a range of values, but how many values? Well, if I use the length function and pass to the length function
45:15
the list of values, length's purpose in life is to tell me how long is this list, and it's 3.
45:21
So that's almost as though before, I had just done something like this, but I don't want to hardcode 3, I want to dynamically figure out
45:29
how many students are at Hogwarts. So I'm just composing, composing, composing, or nesting all of these various ideas.
45:36
All right, if I may, let me transition now to-- in Hogwarts still to introduce one final type of data before
45:42
we combine everything with a few final programs. It turns out in Python, there's not just strings, not just
Dictionaries
45:49
ints, not just floating point values, not just bools, not just lists there are also what are called dictionaries or dics, are a data structure that allows you
45:58
to associate one value with another. Literally a dictionary like in the human world.
46:04
If you were to open a dictionary, be it in English or any other human language, what's inside of a dictionary? Well, it's a bunch of words and definitions.
46:12
A computer scientist, though, and a programmer would describe those more generically as keys and values, something
46:19
associated with something else. That's all a dictionary is. It allows you to associate something with something else.
46:25
And notice, this is already more powerful, more interesting than a list. A list is just a set of multiple values.
46:32
But a dictionary is two-dimensional, if you will. Just like a human dictionary, a book, it associates something
46:39
with something else like words with their definitions. Now what does this actually mean in practice?
46:44
Well suppose that we wanted to keep track of who is in what house at Hogwarts.
46:51
Well, I could do it using lists alone. Let me go back to VS Code here and let me just temporarily-- but in a way that I'm not going to like ultimately--
46:59
let me create another variable called houses, set it equal to Gryffindor, corresponding to Hermione's house,
47:06
Gryffindor, corresponding to Harry's house, and Gryffindor, corresponding to Ron's house. And let's add Draco in there.
47:12
So we now have four instead of three students just so we have a little variety, and he was in Slytherin.
47:18
So now we have two lists. And we could just agree amongst ourselves
47:24
that whoever is first in the students variable lives in the first value in houses.
47:31
Whoever is second in students lives in the second house. Who's ever third in students lives in the third house.
47:37
We could do that. But honestly, that is going to break down quickly when we have a lot of students, when we have a lot of houses,
47:44
and what if we want to keep track of more things than that? What if we want to keep track of every student's house and the patronus, this image that they conjure up magically?
47:52
Well, then we need a third list like-- this is just going to get messy quickly if we're just on the honor system
47:58
using multiple lists where everything lines up logically. It doesn't end up well when your code gets more complicated.
48:05
But I do want to implement this idea. I want to associate something with something. A student with a house, a student with a house, a student with a house
48:12
and so forth, so how can I go about doing this? Well, let me go back to my code here and let
48:18
me propose that we do this using a Python dictionary. And this is the last of the new syntax, really, that we'll see .
48:25
Here's the new syntax. Instead of using square brackets, we're going to use curly braces for dictionaries as well.
48:32
We've seen curly braces in the context of f strings completely unrelated. Sometimes you run out of keys on the keyboard and the authors of a language
48:40
need to start reusing symbols in different ways, that's what's about to happen. We're using curly braces in a different way.
48:46
Now so let me create a variable called students. And let me go ahead and set it equal to open
48:51
curly brace and closed curly brace. This is an empty dictionary at the moment. And here's how a dictionary works.
48:58
It allows you to associate something with something else, and you do that like this. Hermione, quote-unquote, colon, and then the value thereof.
49:07
What do you want to associate with Hermione? Well, Gryffindor. What do I want to associate Harry with?
49:13
Well, I want to associate him with Gryffindor. What do I want to associate Ron with? Well, I want to associate him with Gryffindor.
49:21
Well, this is actually not going to-- this is going to get very ugly quickly. Once we add in Draco and Slytherin, my code is going to get too long,
49:27
it's going to start wrapping. So this is purely aesthetic. It is perfectly acceptable in Python and other languages
49:33
to format your code a little more readily and just add new lines if it makes it more readable. And one way of doing this might be as follows.
49:40
I still have my curly brace up here, I still have my curly brace down here, but notice, it's a little more readable now
49:47
in that I have my keys on the left, my somethings, and my values on the right, my other somethings.
49:53
It's just a little easier to skim top to bottom. You could format it differently as well. But I'm going to go ahead and add in now Draco
50:00
who lives, of course, in Slytherin. So now I have each of these keys on the left
50:07
and values on the right, which is really, again, just a code implementation of this idea, a little chart
50:13
that you might write up with paper pencil when associating something with something else. So how do I now use this code in an interesting way?
50:20
The syntax is almost the same. If I want to print out the very first student, Hermione's house,
50:26
I could do this. Print out the name of the variable, but I need to go inside of the variable.
50:31
I need to index into it. And what's neat about dictionaries is that whereas lists
50:38
have locations that are numeric-- 0, 1, 2; Hermione, Harry, Ron respectively,
50:45
dictionaries allow you to use actual words as your indices, so to speak,
50:50
your indexes to get inside of them. So if you want to print out Hermione's house,
50:55
the key you care about is, quote-unquote, Hermione, and what this syntax here will do-- notice, it's not a number 0 or 1 or 2.
51:04
It's literally Hermione's name. This is like going to the chart earlier and saying, all right, give me Hermione
51:11
is my key, Gryffindor is the value. That's what we're doing here syntactically. We're looking up Hermione and getting the value thereof.
51:18
So if I go back to my code, that should print out Gryffindor. And if I do this a few times, students, bracket, quote-unquote,
51:24
Harry should give me Harry's house. Print students, open bracket, Ron, that should give me Ron's house.
51:30
And then lastly, if I do this with students, bracket, Draco, that should give me Draco's house.
51:35
Now it's a little manual still, and I bet we can improve this, but let me run Python on hogwarts.py and we should see Gryffindor, Gryffindor, Gryffindor, Slytherin, which
51:44
is exactly what we'd expect. Now all we've done, again, is we've just now moved from having just a simple list of names to, again, two dimensions,
51:52
associating like we would on paper-pencil something with something else, keys with values respectively.
51:58
Allow me, if you will, even though I realize this is getting a little fancy, allow me to escalate things slightly here and transition from looking
52:07
at just, for instance, that pattern there, just a hard coding those values
52:13
there to actually printing these out more dynamically. Let me go ahead and use our loop, and this question came up earlier as well,
52:19
let me go ahead and say for each student in students,
52:25
go ahead and print out, for instance, the students variable at--
52:31
well, let's just say student first. Let's keep it simple. So this is not going to be that interesting yet, but when I run Python of hogwarts.py and hit Enter, notice, what should I see?
52:41
Let me take a question here to see what am I going to see when I hit Enter now when I'm doing for student in students?
52:48
AUDIENCE: Yeah, I think we will only see keys. DAVID MALAN: Perfect. So good intuition. It could have gone both ways.
52:53
Could have been values, the houses. But when you use a for loop in Python to iterate over a dictionary, by design,
53:01
it iterates over all of the keys. So we should see, I think, Hermione, Harry, Ron, and Draco.
53:07
Let me hit Enter now, Enter, and indeed, you're exactly right, we see just the keys. But that's not really that useful if what I really care about
53:15
is who lives where, can I print out both? Well, I think I can. Let me go ahead and do this.
53:21
Let me print out not just the student's name, the key, but let me use the key, their name, to index into the dictionary.
53:30
If I know the word in the dictionary, let me look up its definition. If I know the student's name, let me look up their house,
53:35
and the syntax for this, just like a list, is students, bracket. And just like in the past we used i when i was a number,
53:44
we can also with a dictionary use a string. So if the student's name is the key, then this syntax, students,
53:55
open bracket, student, close bracket will go to Hermione's location
54:00
and get back her house. Will go to Harry's location and get back his house and so forth. So if I do Python of hogwarts.py, Enter, now I
54:08
see Hermione, Gryffindor; Harry, Gryffindor; Ron, Gryffindor; and Draco Slytherin. Now it looks like I've given them all new last names,
54:14
but I can clean that up. This is just a print thing. Let's go ahead and change our separator from the default space
54:20
to maybe a space, comma. And just using print features now, let me run the same program again, Enter,
54:26
now I've just got some nice pretty commas in there to make clear that Hermione's last name is not, in fact, Gryffindor,
54:31
but that's just a print detail. Any questions, then, on these dictionaries and what I've just done?
54:37
Questions on these dictionaries and this looping over then here?
54:45
AUDIENCE: I just can't get my head around the for student in students.
54:52
If I'm-- just correct me if I'm right. Does that mean it imports the list of students and uses the indexes--
55:01
or in other words, Hermione, Harry, and Ron as the indexes in the actual--
55:09
the list of students? DAVID MALAN: Correct. So this is just a feature of Python. When you use a for loop with a dictionary, what happens is this.
55:17
If this is the dictionary here with the keys on top and the values on bottom, you get to choose what the variable is called.
55:22
I called my variable student just because it makes sense, because I want one student at a time. And what for loop does, just like it did with numbers before,
55:29
the 0, the 1, and the 2, it allows me to, for instance, set student equal initially to Hermelin's name.
55:35
And then the next iteration of the loop, the next cycle, sets student equal to Harry's name, then Ron, then Draco.
55:42
It just happens automatically. Like that is what the Python interpreter does for you when it sees a for loop like that.
55:49
So it's very similar in spirit to iterating with a for loop over a list, but rather than iterate over the numeric location,
55:55
0, 1, 2, it iterates over the bold-faced keys in this representation here
56:01
graphically. And allow me to give us one other example on Hogwarts before we look at one other familiar domain.
56:09
At the risk of things escalating a little bit, let me propose that we continue the story with one final Hogwarts
56:15
example like this. What if we have more information about each of our students?
56:21
And this is inevitable. If you're implementing a program that's a database with people or customers,
56:26
or employees or anything else, you can imagine having a lot of data about anything you're representing in your program
56:33
here. For the sake of discussion, suppose that every student at Hogwarts, of course, has a name, they have already a house, but they also have a patronus.
56:41
For those unfamiliar, this is the animal or entity that comes out of the end of their wand when they make a certain magical spell.
56:48
The point here being is that we want to associate not just one thing with the student, but multiple things
56:55
as well-- their name, their house, and their patronus in this case. Well, what might code like this look like?
Lists of Dictionaries
57:02
Well, let me go back to hogwarts.py and let me start fresh for just a moment. And let me propose that I enhance this with a bit more data.
57:10
And this data is going to look as follows. My students variable now, I'm going to propose we think of it as a list.
57:18
What if we have a list of dictionaries as follows? Indeed I want to literally implement this picture here.
57:24
So notice that my previous picture just represented a single dictionary. But suppose I wanted to compose a list of dictionaries.
57:33
That is, for students-- so a list of four students. And suppose that each of those students is itself a dictionary,
57:41
a collection of key value pairs, keys and values, something and something else.
57:48
Well, here's one other way we can do this in code. Let me go back to VS Code here and let me define a variable called
57:55
students that is equal to a list. And I'm going to preemptively move my cursor onto separate lines,
58:01
because I know this is going to be long, and I want to fit all of the elements of this list inside of it.
58:07
I'm now going to create a dictionary, one dictionary per student. And how do I create a dictionary? I just use those curly braces.
58:13
But it's up to me to define what those keys are. And let me propose that one key this time won't be the student's name explicitly, it
58:20
will literally be the word name, and there, going to have the name Hermione. The same student is going to have another key called house
58:28
and the value is going to be Gryffindor. And the same student is going to have a third key called patronus,
58:34
and the value of that is going to be-- I had to look it up-- an otter, according to the book.
58:39
Now I'm going to create a second dictionary inside of this list. And again, a dictionary is like literally
58:44
like the human dictionary of words. It's a book that contains keys and values, words and definitions.
58:50
What are the three words I'm storing in each of my dictionaries? Name, house, and patronus. What are the definitions of those words for Hermione?
58:58
Hermione, Gryffindor, and otter respectively. For Harry, the definitions are going to be different in this new dictionary.
59:05
Let me give myself another pair of curly braces and say this, name, quote-unquote, colon, Harry.
59:12
House here is, again, going to be Gryffindor. And this one I knew, his patronus, is going to be, in this case, a stag.
59:21
Next, a third dictionary. The name here will be Ron. And I'm going to go ahead and do that just like this.
59:27
Next, I have the house, and he, too, was Gryffindor. Lastly, had to look this one up, Ron's patronus was a Jack Russell terrier.
59:38
Lastly is Draco. In a fourth dictionary now-- so another pair of curly braces,
59:45
the name of the student is, of course, Draco. The house of this student is Slytherin.
59:50
And Draco, interestingly enough, at least according to the internet, has no patronus.
59:57
Was never revealed in the books or the movies. So it turns out, this is actually a wonderful teachable moment.
1:00:02
There is a special key word in Python that is literally None, and N-O-N-E,
1:00:08
with the first letter capitalized. This represents officially the absence of a value.
1:00:14
So I could a little sloppily do something like quote-unquote, but does that mean I didn't get around to typing it or not?
1:00:20
It's a little clear semantically to say literally None, a special keyword in Python to make clear that I know Draco has no patronus,
1:00:29
it's not just an oversight on my part. Now that I have this, what do I have in the computer's memory?
1:00:36
I have a list. How do I know it's a list? Because I see a square bracket at the beginning and another square bracket
1:00:42
at the end. That's just my visual clue, OK, I don't know necessarily what else is going on here, but there's a list of something.
1:00:48
What is in that list? Well, here, too, the syntax is our clue. Because this line 2 starts with a curly brace and ends with a curly brace,
1:00:57
I just know, that is a dictionary, a collection of key value pairs. Now this all fit on my screen perfectly, so I
1:01:04
didn't bother moving all of the key value pairs onto new lines, it would have made it really tall, so I kept it all together here this time.
1:01:11
But how many keys does this first dictionary have? Put another way, in Hermione's physical dictionary,
1:01:17
how many words are in that dictionary? Three. The words are name, house, and patronus.
1:01:22
What are the three definitions or values of those words in Hermione's dictionary? Hermione, Gryffindor, and otter respectively.
1:01:31
And the same story goes for Harry, then for Ron, then for Draco, I have, by design, chosen
1:01:39
to give them dictionaries that have all the same keys, all the same names,
1:01:44
but they all have unique values. And that's my design, that's my prerogative as a programmer.
1:01:50
So why is this useful at the end of the day now? I have access to a whole collection of interesting data about all
1:01:57
of these students, and I can still do a loop. I can say for students in students, that's
1:02:02
going to allow me to iterate over this list of students. And let me go ahead and print out just one thing at a time.
1:02:08
Let me print out the current student's name. So as complicated as the dictionary is, this should be pretty comfortable.
1:02:14
For student in students is just going to iterate over every student in the list. 1, 2, 3, 4 total.
1:02:20
The next line is just going to print out the value of the name key. It's like opening a physical dictionary, looking up the word name,
1:02:27
and giving us Hermione, Harry, Ron, and Draco respectively from each dictionary. So if I run this version of Hogwarts and hit Enter, there, I get all three
1:02:36
of their names. But what if I want more information than that? I want both their names and their houses.
1:02:42
Well, just add to print's arguments student, open bracket, house,
1:02:47
close bracket. All right, let's go ahead and run this. Python of hogwarts.py and hit Enter.
1:02:53
So I now see Hermione, Gryffindor; Harry, Gryffindor; and so forth. Well, we can aesthetically clean this up a little bit by adding a separator with print, like a comma and a space,
1:03:01
just so that when I run this again, I now see some comma separating these values. But recall that students have not just a name, not just
1:03:08
a house, but also that patronus. So if we want to print out that, too, we now have the syntax via which to go into that same dictionary for each student
1:03:18
and output their patronus as well as their house in their name. So if I run this program one final time, now I
1:03:24
see all of the data in this here dictionary. So this is a lot to absorb all at once, I'm sure.
1:03:31
It's the last of our new data types. On top of lists, we have these dictionaries, but again, a dictionary, at the end of the day,
1:03:37
is just a collection of values similar to these values here that allow you to associate keys with values.
1:03:44
And the first version of this program associated literally the student's names with their houses, but then I realized
1:03:51
in my next version, wait a minute, what if every student has not just a name in a house, but a patronus? Let's actually standardize the names of our keys
1:03:59
to be name, house, and patronus, and then the values of those keys can actually be the data, like Hermione, Gryffindor, otter, and so forth.
1:04:08
Questions now on these dictionaries and iteration thereof? AUDIENCE: I just was wondering, suppose the dictionary is very huge,
1:04:18
and if I want to look up for a specific student, so how do I know where to look that student from?
1:04:26
Like can we sort it out in alphabetical order or numeric order or anything like that?
1:04:32
DAVID MALAN: In short answer, yes. One of the features of Python is that it makes these dictionaries very highly
1:04:37
performant for you. That is, even if they're very large, as they will be in future weeks when we manipulate more data, Python will find the data
1:04:45
you care about quickly for you. And in fact, that is a feature of the language, that is a feature of a dictionary to get you the data quickly.
1:04:53
And there are functions that you can use. You can sort the data, you can sift through it, you can do very performant operations as we eventually will.
---
## ⏸️ توقفت هنا (1:05:01)
---
1:05:01
Allow me, then, to propose, as we wrap up these loops, that we solve just a few final problems that will perhaps
Nested Loops
1:05:08
evoke fond memories of yesteryear, at least for me, wherein one of my favorite games growing up was this one here on the original Nintendo.
1:05:15
And this is a two-dimensional world where the characters move up, down, and right, not so much to the left, in jumping over
1:05:23
pyramids and obstructions like these. And allow me to propose that we use this just for inspiration, not to do something that's quite as colorful or graphical as this, but just
1:05:31
to focus on, for instance, this barrier in the middle of the world here that Mario or Luigi had to jump over.
1:05:38
And so this here seems to be like three bricks stepped on top of one another. And we won't do things quite graphically,
1:05:44
but let's just implement a very simple Python-based version of this textually using maybe just hashes for bricks.
1:05:50
Because there's a pattern here, one on top of the other, and I bet we can solve this in any number of ways.
1:05:56
Well, let me switch back over to VS Code here and let me propose that we create a program called mario.py using code
1:06:03
in the terminal window. And then up here, let me start by implementing that same picture as simply as I can, printing out just literally the hash,
1:06:11
and then the hash, and then a third final hash. This is going to be a very textual approximation of it,
1:06:17
but I think if I run Python mario.py, I've got a very simple version of that same column of bricks, so to speak.
1:06:25
But you can imagine that certainly in a game where maybe these columns get higher or lower,
1:06:31
it would be nice to write code that's actually a little more dynamic than that and doesn't just use print, print, print, which is literally
1:06:37
copy and paste, it would seem. So let me at least adopt some of today's lessons learned and instead do something like this.
1:06:44
For underscore in range of 3, let's now print out just one of these at a time.
1:06:50
But the fact that I've now used a 3 to range means if I want to change it to something bigger or smaller,
1:06:55
I change it in one place not in three or more places. And this code, too, of course, if I got it right,
1:07:01
is just going to print out the exact same thing. So we're iterating here.
1:07:06
But let's see if we can't now integrate our discussion of writing functions of our own to begin writing something a little more dynamic
1:07:13
and solving more complicated problems ultimately. One of the nice things about functions is that they allow us to not just write code that we can use and reuse,
1:07:21
they allow us to create abstractions, if you will. An abstraction is a simplification of a potentially more complicated idea.
1:07:28
And we've seen this a few times over the course of the weeks. For instance, we had a function called hello, which, granted, didn't do
1:07:35
all that much, it just printed hello. But it allowed me to think about the function as exactly what it does,
1:07:40
not generically printing something, but literally saying hello. I've been able to get a number using something similar by defining
1:07:48
my own function like get number. Well let me go ahead and, for instance, assume for the moment
1:07:53
that I've had the forethought to, in my function main, use a function called print column.
1:07:59
That seems as good a name as any to use a function that prints a column of bricks.
1:08:05
Well, how can I go about now implementing this abstraction, this simple idea of print column with actual code?
1:08:12
Well, we've seen before with def, we can do just that. Let me define a function called print column. Let me accept as its input, generically speaking, a parameter called height.
1:08:21
I could call it n or h, but it would be a little more explicit now with height just so I remind myself what it's doing.
1:08:27
And now I think I can just borrow some of that same code from before. For underscore n range of height, go ahead and print out a single hash.
1:08:37
And then at the end of this whole program, let's just call main. So I've kind of complicated the code.
1:08:43
It doesn't do anything more just yet, but it's setting me up for solving what I think are going
1:08:48
to be more sophisticated problems. If I run Python of mario.py, we're back where we began. But I now have a function, an abstraction, print column,
1:08:57
that's going to allow me to think about printing some chunk of the world of Mario at a time.
1:09:03
And I can do this in different ways, too. Notice that if I really want, I could do something like this.
1:09:09
I could implement now print column in different ways, especially if I am using print column all over my code,
1:09:15
or maybe still, a colleague of mine, a friend, someone else on the internet is using my print column function.
1:09:21
What's also nice about functions you've written is you can change the underlying implementation details of them,
1:09:27
but so long as you don't change the name of the function or its parameters or what it returns, if anything no one else knows the difference.
1:09:35
You can change the internal implementation as much as you want if you want to improve it or make fixes over time.
1:09:41
So for instance, another way we could implement print column, recall, would be something like this. A bit clever with one hash and then a new line,
1:09:48
and then maybe we could do multiplication of strings, and then end this line with quote-unquote.
1:09:54
Again, it's OK if you're not comfortable with this syntax. This was a more clever approach we saw in the past.
1:09:59
But if I run Python of mario.py here, I'll still see a column of three. But what's important here is that main does not
1:10:07
need to know that the underlying implementation of print column
1:10:12
has changed. Well, let's transition to a different dimension, if you will, and rather than print out just these vertical bricks, let's
1:10:19
fast forward in the game to this part of the world here. At some part, Mario encounters these bricks in the sky,
1:10:25
that if he jumps up underneath, they become coins. And so he gains to his score. But let's go ahead and focus only on those coins,
1:10:32
and let me propose that we print out, oh, just these four question marks here. And let me go back to VS Code here.
1:10:38
And let me propose that within VS Code here, just like before, we try to abstract this away. So let me go ahead and get rid of this version,
1:10:45
because we're now going horizontal instead of vertical with our output. And let me just say, well, print row four times.
1:10:53
Let me just abstract away the problem at hand. I don't know yet how I'm going to print those four question marks,
1:10:59
but let's call it print row 4, and I'll assume I'll now solve this problem. Let's now go down that rabbit hole of solving the problem.
1:11:06
Define a function called print row. It's going to take a width instead of a height, because it's horizontal instead of vertical.
1:11:14
And how can I do this? Well now, we have an opportunity to do string multiplication even more
1:11:19
elegantly. I can say quote-unquote, question mark, times width. And this is a very pretty Pythonic way of printing what could otherwise
1:11:28
be a loop, and that's fine, but this is going to go ahead and print those question marks for me. Let's do Python of mario.py, Enter, and now I've got four question marks.
1:11:37
It's not nearly as pretty as the more graphical version, but it is at least a building block toward having
1:11:44
now a reusable function like print row. And why am I doing all this? Like why are we over engineering the solution to these problems
1:11:52
by having print column and print row? Well, it's a useful problem-solving technique. As soon as your world does not look one-dimensional
1:12:00
like this or with the column version, but what about this? Later in Super Mario Brothers does Mario have to jump down into this world
1:12:08
where there's a lot of these underworld barriers. And this one here, for instance, looks like a square.
1:12:13
It's two-dimensional there's a height and a width to it. And that is to say there's a bunch of different ways
1:12:18
we could implement this thing if, maybe for discussion, it's like a 3-by-3 grid, a 3-by-3 square of sorts.
1:12:26
Well, how can we go about solving this here problem? Well, let me propose we come back to VS Code
1:12:32
and let me propose that we think about this in a couple of different ways. I could do this like this.
1:12:39
If I know where I'm going, maybe I'm a seasoned programmer, let me go ahead and do this.
1:12:45
Let me print out a square, the width, and the height of which is 3. That's an abstraction. I'm just taking for granted for a moment that there is already
1:12:52
a function called print square that's going to be with 3 and height 3 as well. But someone's got to implement this, and at the moment,
1:12:59
there's only me at the keyboard, so let's go ahead and implement that square. Let me go ahead and define a function called
1:13:05
print square that takes in a specific size, both for height and for width.
1:13:10
And here's where we have an opportunity to use some of those loops. And we can use those loops in a way we haven't yet.
1:13:16
If I want to print out all of these rows, but also, all of these columns,
1:13:21
I now have to think not just cyclically like a loop allows, but I need to think two-dimensionally.
1:13:26
And if you're familiar with like an old school typewriter or even a printer nowadays, it generally prints from top to bottom.
1:13:33
So even if you have multiple columns, you print out one line at a time, and while you're on that line, the printer or the typewriter
1:13:41
prints from left to right. And that's the mental model to have with your black and white terminal window.
1:13:46
All of the output for every example thus far starts at the top and goes down to the bottom.
1:13:52
From top to bottom, left to right. So we have to generate our output, our square in that same way.
1:13:58
So let me propose that we do this. Let me propose that we know we need to iterate this many times, 3 or more
1:14:04
generally size. So let me do this. For i in the range of size, what do I need to do three times?
1:14:12
Well, I want to print out what? 1, 2, 3 rows of bricks.
1:14:17
But within each row of bricks, what do I want to print? 1, 2, 3 bricks specifically.
1:14:24
So if we go back to our diagram here and I stipulate that it's indeed meant to be a 3-by-3 square, 3 wide and 3 tall,
1:14:33
what did I want to do to print the first row? I want to print brick brick, brick.
1:14:40
What do I want to print on the second row? brick, brick, brick. And the third row, brick, brick, brick. So I'm doing three things three times.
1:14:48
There's a lot of printing that must happen. So let me go back to my code here and let me propose now
1:14:53
that we think of this outer loop that I've just started as representing each of our rows.
1:15:00
For i in range of size is going to ensure, no matter what I do next, that I can print out 1, 2, 3 rows, or more generally,
1:15:10
size, where size could be 3, but it could be smaller or larger. What do I want to do on each of the rows?
1:15:17
Well, just like an old school typewriter or printer, on each row, I want to print out brick, brick, brick; brick, brick, brick; brick, brick,
1:15:24
brick. Well, that sounds like a cycle, some kind of loop. So maybe I can have inside of one loop another loop.
1:15:31
I don't want to use i again because I don't want to use the same variable and mess up my counting. So I'm going to by convention use j.
1:15:38
Very common to use i and then j-- maybe k, but after that, you shouldn't keep nesting inside of each other.
1:15:44
Let me go ahead and say for j in range of size 2, because it's a square, and then each of these rows,
1:15:50
let me print out a single hash, but no new line, but after each row,
1:15:57
let me print only a new line. So there's a lot going on here, especially if you've never
1:16:03
touched Python, let alone loops, but notice what I've done here, too, and I'll add some comments for clarity.
1:16:10
For each row in square, for each brick in row, print brick.
1:16:22
And here is where comments, and more generally, pseudocode can really help explain to yourself and to others
1:16:28
what your lines of code are doing. On line 8, I'm iterating from i equals 0 on up to size.
1:16:35
So 0, 1, 2. On line 11, I'm doing the exact same thing, but using j from 0, 1, 2.
1:16:41
But that's good, because i represents how each of my rows. And while I'm on each of those rows, inside of this outer loop,
1:16:49
I'm going to do brick, brick, brick; 1, 2, 3; 1, 2, 3; 1, 2, 3. But I don't want my cursor to keep moving to the next line
1:16:56
while I'm on a row, so I'm just overriding that line ending. But let me ask you a question of the group
1:17:03
now, why on line 16 do I have a print here all by itself?
1:17:10
Why do I have a print all by itself? Notice that it's below the inner loop, but inside
1:17:19
of the outer loop, so to speak. What is that loop on line 16 doing ultimately?
1:17:26
AUDIENCE: Every time you finish a line, you have to add a new line at the end of it.
1:17:33
So print, it prints a new line. DAVID MALAN: Perfect. I don't want a new line after every brick.
1:17:40
I only want to do that at the end of the row, and that's why my comments now are perhaps enlightening.
1:17:45
Notice that this loop here is just iterating for each brick in the row.
1:17:51
Once I'm done with that inner loop, so to speak, once I'm done with these highlighted lines here, to Evelyn's point,
1:17:57
I need to print out one blank new line. And we've not done this before, but when you call print with no arguments,
1:18:03
all you get is that automatic line ending, the backslash n where the cursor moves to the next line.
1:18:09
So if I now go back to my terminal window and run mario.py, I think I should get a 3-by-3 square.
1:18:16
And it doesn't quite look like a square on my screen because these hashes are a little taller than they are wide, but it is, in fact,
1:18:22
3-by-3. But let me propose, as we've always done here, how we might tighten up this code further.
1:18:28
Just for clarity's sake, let me get rid of my comments for a moment just so we can see how many lines of code we have total.
1:18:35
And let me propose that we maybe do this. Let me propose that, you know what, this inner loop,
1:18:41
especially if you're having trouble wrapping your mind around one loop inside of another loop, you don't strictly need it.
1:18:47
What if we do this trick again? What if we print out inside of the outer and only loop each
1:18:54
of those hashes times the number of times we want them? We draw inspiration from an earlier approach
1:19:00
and we run Python now of mario.py, same result, but now, print square is really nice and compact.
1:19:07
It has one explicit loop, and it's still printing out using string multiplication all of the hashes at once on that row.
1:19:15
If you like abstraction and you'd like to wrap your mind more around what the code is doing, well, let's do this.
1:19:21
If you're not quite clear on what's going on, let's propose that you implement a function called print row, passing in size.
1:19:28
And let me propose that this print row function, it simply take in that width
1:19:33
and print out the individual hash times that many times.
1:19:39
In other words, here's an opportunity for abstraction, whereby, well, what does it mean to print a row?
1:19:45
Well, when you're implementing print square, I don't really care what it means to print a row, I just need to know that someone's taking care of printing the row.
1:19:53
You can pass the buck to another function altogether. And how does print row work? Well, it could use a for loop, it could use this string multiplication trick.
1:20:02
This is a way to take a larger program-- and this is probably the most complicated one we've looked at thus far--
1:20:08
and to decompose it into these smaller components, that once assembled,
1:20:13
achieve your final idea. Seeing no questions, that's the end of our look at loops
Conclusion
1:20:19
in Python, this ability to do things cyclically again and again, and when we combine those with conditionals, this ability
1:20:25
to ask and answer questions and combine them with our functions and variables, we really now have most of the building blocks
1:20:31
we need to solve much larger, much more interesting, much more personal questions. So in the weeks to come, we'll start to see exactly what could go wrong,
1:20:39
though, when we do so, but we'll introduce you to all the more tools via which you can troubleshoot those same problems.
1:20:45

