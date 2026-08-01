

Captions
0:00:00[MUSIC PLAYING]
0:00:25DAVID MALAN: This is CS50's Introduction to Programming with Python.
0:00:28My name is David Malan, and this week we focus on conditionals.
0:00:32Conditionals, or conditional statements, in Python and in other languages,
0:00:36are this ability to ask questions and answer those questions, in order
0:00:40to decide do you want to execute this line of code?
0:00:43Or this line of code?
0:00:44Or this other line of code instead?
0:00:46They allow you to take the proverbial forks in the road,
0:00:48within your own code, logically.
0:00:50So how might we go about making some of these decisions?
0:00:54Well, it turns out that Python comes with a lot of built-in syntax.
0:00:57For instance, here are just some of the symbols
0:00:59you can use in Python to ask questions.
0:01:01Admittedly, mathematical questions, but we'll start there, if only
0:01:04to keep the examples simple early on.
0:01:07This first symbol, as you might know from math, represents greater than.
0:01:11The second symbol might not look too familiar, because we usually write it
0:01:14all as one thing on a piece of paper.
0:01:16But on a keyboard, if you want to say greater than or equal to,
0:01:19you'd use this symbol instead.
0:01:21This, of course, means less than.
0:01:22This means less than or equal to.
0:01:25And this one's a bit of a curiosity.
0:01:27We've seen, in our look at functions and variables,
0:01:30how we were able to assign values to variables using a single equal sign.
0:01:35But that equal sign didn't represent equality.
0:01:38It represented assignment, from right to left.
0:01:40That's great, because it solved that problem.
0:01:42But it left us in a bit of a bind, because how do we now
0:01:45compare two things, left and right?
0:01:47Well, in Python, and in many languages, you actually use two equal sides.
0:01:51So two equal signs represents equality, comparing the thing
0:01:55on the left and the right.
0:01:56One equal sign, as always, represents assignment,
0:01:59copying the thing from the right to the left.
0:02:01Lastly, this last symbol represents not equal to.
0:02:04So the exclamation point, or bang, followed by an equal sign,
0:02:08means not equal to some value next to it.
0:02:12Well, to ask the questions using these symbols, or any others,
0:02:15we're going to need another keyword in Python.
0:02:18And that keyword, quite simply, as in English, is if.
0:02:21You can ask questions in Python code along the lines of,
0:02:24if the answer to this question is true, then go ahead
0:02:28and execute this code for me.
0:02:30So let's go ahead and write some of these examples here.
0:02:33I'm going to go over to VS Code.
0:02:35And let's go ahead and create a program first,
0:02:36called compare.py, the goal of which is simply
0:02:39to write code that compares values and makes decisions based on those values.
0:02:44Let's go ahead and type code of compare.py,
0:02:47in order to create a brand new file called compare,
0:02:49in which we'll start to express some of this logic.
0:02:52Well, what do we want to compare?
0:02:53Suppose we want to compare, for the sake of discussion,
0:02:56just a couple of integers.
0:02:57But we'd like those integers to come from the user,
0:03:00so that we can make decisions based on numbers
0:03:03we don't know the values of in advance.
0:03:05Well, let's go ahead and do this.
0:03:07As we've done in the past, let's declare it a variable, like x.
0:03:10Let's assign it equal to the return value of the int function,
0:03:15and pass to the int function the return value of the input function,
0:03:19asking the user a question like, what's x, question
0:03:22mark, as we've done in the past.
0:03:24Let's do this one more time with y, asking the user for the value of y.
0:03:29And, again, converting that, ultimately, to an int, as well.
0:03:33So with this amount of the story, we have two variables, x and y,
0:03:37each of which has values.
0:03:38And ideally, we should be able to now compare these values.
0:03:41So suppose I want to make a decision based on the values of these variables.
0:03:45I'm going to use the keyword if.
0:03:46And I'm going to use some of those mathematical symbols
0:03:49to actually ask the question itself.
0:03:51So how about this, if x is less than y, then let's go ahead and just
0:03:55print as much out.
0:03:56Quote, unquote x is less than y.
0:03:59So this isn't a very interesting program yet.
0:04:02I'm literally just stating the obvious, based on the math.
0:04:05But it's allowing me to now introduce some new syntax.
0:04:08And exactly what is the syntax?
0:04:10Well, it's this-- not just the keyword if, which
0:04:12I've added here at the start of line four,
0:04:15but then I asked my question here, x less than y.
0:04:18x is one variable on the left, y is one variable on the right.
0:04:21And, of course, the less than sign is expressing the mathematical question
0:04:24I have.
0:04:25What I've highlighted here is technically
0:04:26called a Boolean expression.
0:04:29A Boolean expression, named after a mathematician named Bool,
0:04:32is simply a question that has a yes or no answer, or technically,
0:04:36a true or false answer.
0:04:38And that's nice because if there's only two possible answers,
0:04:41it's very easy for me, and in turn the computer, to make a decision--
0:04:44do this, or don't do this thing.
0:04:47Now notice, if you come from other languages,
0:04:49you might notice that I have not typed any parentheses.
0:04:53They are not, in fact, necessary, at least in this case, in Python,
0:04:56but I have typed a colon at the end of the line.
0:04:58And even more importantly, at the next line
0:05:01I have begun my line with some indentation,
0:05:04hitting the space bar four times, or just hitting Tab once,
0:05:07which will automatically be converted to the same.
0:05:09That indentation is what tells Python that line five should only
0:05:13be executed if the answer to line four's question is, in fact, true.
0:05:20So if x is less than y, that phrase will be printed thereafter.
0:05:24Well, let's add a few more lines of code.
0:05:25How about another question?
0:05:26If x is greater than y, then let's go ahead and print that.
0:05:30x is greater than y.
0:05:33And let's do one final question, if x equals y, then-- wait a minute.
0:05:38What have I done wrong here?
0:05:41A good eye here.
0:05:42I don't want to assign y to x.
0:05:44If x equals equals y is how I express equality, let's go ahead
0:05:48and print out x is equal to y.
0:05:52So I now have three conditions, if you will,
0:05:56one question asking x less than y, one asking x greater than y,
0:05:59one asking x equals equals y.
0:06:02Let's run the code.
0:06:03Well, down here in my terminal window I'm
0:06:05going to run Python of compare.py and hit Enter.
0:06:08What's x?
0:06:09Let's go with one.
0:06:10What's y?
0:06:11Let's go with two.
0:06:12This should, of course, execute that first line of code
0:06:15and tell me, indeed, that x is less than y.
0:06:18Exactly as I would expect there.
0:06:21Well, what just happened, though, in code?
0:06:24Well, let's take a look, perhaps, at this same code visually,
0:06:28particularly if you're a more visual learner, this, I dare say,
0:06:31is what just happened.
0:06:32So what we're looking at here is a flow chart.
0:06:34It's a diagram of this program's logic.
0:06:37And more technically, it shows the program's control flow.
0:06:41That is, the ability of you, in code, to control
0:06:43the flow of a program, generally from top to bottom.
0:06:46In fact, let me go ahead and zoom in on the top of this flow chart.
0:06:49And you'll see an oval at the very top that says, quite literally, start.
0:06:52That is, irrespective of what shape or layout
0:06:55the diagram is, where your own thinking and logic
0:06:58should start when trying to wrap your mind around this program.
0:07:01Notice that there's an arrow from start to this diamond shape.
0:07:04And inside of that diamond is a question, a Boolean expression,
0:07:07x less than y.
0:07:08And this shape just means, based on the answer to that question,
0:07:12go left or go right.
0:07:14Specifically, go left if the answer is true,
0:07:16or go right if the answer is false.
0:07:19Well, the inputs I typed were one and two, respectively, for x and y.
0:07:24So, of course, one is less than two.
0:07:26So that's why my program printed out, quote unquote, x is less than y.
0:07:32But recall the code.
0:07:34The code then proceeded to ask two more questions.
0:07:37Is x greater than y?
0:07:38Is x equal equal to y?
0:07:40Well, the flow chart depicts those questions, too.
0:07:43Notice that no matter whether the question
0:07:46had an answer of true or false, the arrows both converge back down
0:07:50to this second diamond shape here.
0:07:52And that second diamond shape asks the second question, x greater than y.
0:07:57That, too, has a true or false answer.
0:07:58So we go one way or the other.
0:08:00But if x is one and y is two, then no, the answer is false.
0:08:04One is not greater than y.
0:08:06So logically, in the flow chart, you follow the false arrow this time.
0:08:09And notice, along that false arrow you don't print anything this time.
0:08:13That's why we only saw one printout on the screen.
0:08:16Now, there was still a third question.
0:08:17And this flow chart captures that, as well.
0:08:19The third diamond asks x equals equals y.
0:08:22Now that, too, has a false answer in this case, because one, of course,
0:08:25does not equal equal y.
0:08:27And so we again follow the third false branch here.
0:08:30And that leads us, of course, to stop.
0:08:32And stop just indicates that's it for the program.
0:08:35So I think that's correct.
0:08:38And that particular flow chart does happen
0:08:40to represent the actual code that I wrote.
0:08:44So it's correct.
0:08:45It does what it's supposed to do.
0:08:46It answered the question correctly by printing on the screen x less than y.
0:08:50But what is, perhaps, poorly designed about it?
0:08:53Let's make this first distinction.
0:08:55It's not enough, necessarily, for the code
0:08:56that you write to be correct and do what you intend.
0:08:58Longer term, especially as our programs get longer and more sophisticated,
0:09:02more complicated, we're going to want them to be well-designed, too.
0:09:06Thoughts on in what way this program is arguably not well designed,
0:09:12even though it's correct?
0:09:15Let's see here.
0:09:16Khalid, if I'm saying that right, your thoughts?
0:09:18KHALID: Too many ifs, I think, is getting repetitive.
0:09:21We can make our code more concise, maybe.
0:09:23DAVID MALAN: Yeah, it seems a little repetitive.
0:09:25I'm asking if this, if this, if this.
0:09:28And yet, logically, I should know the answer to some of those later questions
0:09:31once I figure one out.
0:09:33And, in short, if you look at this diagram here,
0:09:35notice that no matter whether I go left or I go right,
0:09:38I'm always asking three questions.
0:09:41No matter what, all of those arrows lead to the first, the second,
0:09:45and the third diamond.
0:09:46So I'm asking three questions, no matter whether any of those answers
0:09:49are true or false.
0:09:50Well how might I go about improving this?
0:09:52Well, let me propose that we introduce another keyword
0:09:55to our Python vocabulary, namely elif.
0:09:57And this, too, is kind of a succinct one.
0:09:59It's a conjunction of else if, in English,
0:10:02which allows us to ask a question that takes into account whether or not
0:10:07a previous question had a true or false answer.
0:10:10Well, what do I mean by that?
0:10:12Well, let me go back to my code here.
0:10:13And let me propose that we now improve upon this, here,
0:10:17by asking ourselves, ultimately, how can we ask fewer questions?
0:10:22And let me go ahead here and propose that
0:10:24instead of asking if, if, if, let's make these conditions potentially mutually
0:10:30exclusive.
0:10:31That is to say, don't keep answering questions once we get back
0:10:35a true answer.
0:10:37So I'm going to change my code up here as follows.
0:10:39Instead of asking if, if, if, I'm going to say, if x less than y, elif x
0:10:45greater than y, elif x equals equals y.
0:10:50So I'm going to implicitly, just like an English,
0:10:52take into account that I'm only going to keep asking myself these questions
0:10:57if I haven't yet gotten a true response.
0:11:00Think about the logic here, the English.
0:11:02If x is less than y, on line four, print out x is less than y.
0:11:07Well, if that's the case, you're done, logically.
0:11:10Because if the English is saying if x less than y, else if x greater than y,
0:11:15those are going to be mutually exclusive if the answer to the first question
0:11:19is true.
0:11:19You don't have to keep asking questions to which you already logically know
0:11:22the answer.
0:11:23So let me go ahead now and run this program.
0:11:25And I think the behavior is going to be the same.
0:11:27Python of compare.py, what's x?
0:11:29Let's do one.
0:11:30What's y?
0:11:31Let's do two.
0:11:32x is less than y.
0:11:33Now, honestly, I didn't really notice a difference when I ran the program.
0:11:37And honestly, my Mac, my PC, my phone nowadays,
0:11:41are so darn fast that these kinds of improvements
0:11:44aren't going to necessarily feel any faster until we're
0:11:47writing bigger, faster programs.
0:11:49But it's laying the foundation for writing better code longer term.
0:11:52Now what is the improvement I've just made?
0:11:54Well, if previously my diagram looked like this,
0:11:57which was problematic insofar as I was asking three questions no matter
0:12:02what, even if I already figured out what I want to print on the screen.
0:12:06This new version of the program that says if, elif, elif, might look
0:12:10a little something like this instead.
0:12:12Now it got a little wider.
0:12:13That's just because we drew the arrows to be a bit wider here.
0:12:16But let's focus on just how many questions are getting asked.
0:12:19Let me zoom in at the top, as before.
0:12:20And let me propose that we note that the start oval is at the very top,
0:12:25and it's asking us to ask one question first.
0:12:27x less than y, is one less than two?
0:12:29But notice here, let me zoom out, if one is, indeed, less
0:12:33than two, we follow this longer arrow down, marked true.
0:12:39We print out quote, unquote x is less than y.
0:12:42But then we immediately follow this next arrow down to the icon that says stop.
0:12:48So that's what's implied by doing if, elif, elif.
0:12:51If we get back a true answer right away to that first if,
0:12:55we're going to print out x is less than y and then stop.
0:12:57We're logically at the end of the program.
0:12:59So this picture is just representing, graphically,
0:13:03what the code is actually doing.
0:13:05But suppose I typed in something else.
0:13:07Suppose that my code actually ran, and I typed in two for x and one for y.
0:13:13That is to say, the answer to the first question is now false.
0:13:16But the answer to the second question is now true.
0:13:19Because, of course, two is greater than one.
0:13:23Well, let's go back to the diagram.
0:13:25Same as before, we start at the very top where it says start.
0:13:28The very first question up here, now, x less than y, is an answer of false,
0:13:33because no, two is not less than one.
0:13:35So we follow this arrow to the next question, this diamond.
0:13:39Is x greater than y?
0:13:40Well, yes, two is greater than one.
0:13:43So now we follow this left arrow, which is true.
0:13:47We print out quote, unquote x is greater than y, and then stop.
0:13:52So what's the improvement?
0:13:53Well, in the first case, we got lucky and we only
0:13:55had to ask one question and boom, we're done.
0:13:58This time, we had to ask two questions, but then boom, we're done.
0:14:01Only if x happens to equal y do we actually find ourselves, logically,
0:14:07getting all the way down to this final elif in my code.
0:14:11And pictorially, only if x is equal to y do
0:14:14we find ourselves going all the way down to the third diamond,
0:14:17the third question, asking is it equal to y or not?
0:14:23Now, hopefully, the answer at that point is not false.
0:14:25We've included a false arrow just so that the program itself
0:14:28is well-defined.
0:14:29But, logically, we shouldn't actually be getting there anyway,
0:14:33because it's got to be less than, or greater than, or equal to in this case.
0:14:37Well, let me pause here to see if there's
0:14:38any questions, now, either on the code version thereof here,
0:14:42or on this diagramming of that very same logic.
0:14:47Questions here, on this control flow?
0:14:52SPEAKER 1: Aren't we supposed to put an else at the end?
0:14:55DAVID MALAN: A good question.
0:14:57And yes-- so that's going to be my third and final approach.
0:15:00And if you don't mind, let's pivot there right away.
0:15:02Identifying a third keyword, that indeed exists
0:15:04in Python, that allows us to be even better at expressing this logic
0:15:09to design this program even better.
0:15:10And that's going to solve a particular problem.
0:15:13So if I take us back to our code here, notice
0:15:16that what I've highlighted earlier, elif x equals equals y.
0:15:20It's not wrong to ask that question.
0:15:23In fact, if you're trying to be especially thorough,
0:15:25it makes perfect sense to check if x is less than y, greater than y,
0:15:29or equal to y.
0:15:31But why don't I need to ask this third and final question?
0:15:37SPEAKER 2: We don't need to ask if x is equal to y any more because, logically,
0:15:42if the two conditionals evaluate to false,
0:15:45there is only one conditional that will evaluate to true.
0:15:50And that is x is equal to y.
0:15:51DAVID MALAN: Exactly.
0:15:52If we're all pretty comfortable with math, and comparisons
0:15:55here, of course x is either going to be less than y, greater than y,
0:15:58or equal to y.
0:15:59But once you rule out the first two scenarios,
0:16:02logically, it's got to be the case that x must equal y.
0:16:05If it wasn't the case, then it's less than or greater than.
0:16:08So Hope proposed that we use this other keyword, else.
0:16:11And how do we use this?
0:16:12Well, exactly as we might in English.
0:16:13Let me go back to my code here.
0:16:15And instead of bothering to ask the third and final question,
0:16:18let's not ask a question at all.
0:16:20Let's just have this catch-all. so to speak, a final line of code that says,
0:16:24else just assume that x is equal to y.
0:16:27Therefore, printing it as well.
0:16:29So what's the upside of that?
0:16:30My code is still going to work exactly the same.
0:16:33And again, my computer is so darn fast, I
0:16:35don't even notice that it's working even faster than it was before.
0:16:39But we would notice these kinds of things
0:16:41if we were doing a lot more work, a lot bigger programs here.
0:16:44But let me run Python of compare.py.
0:16:46Let's do, for instance, one and two.
0:16:49Still works for that.
0:16:50Let's do two and one.
0:16:52Still works for that.
0:16:53Let's do one and one.
0:16:55And it, indeed, now works for that.
0:16:57But in these cases now, let's consider the path we just went down.
0:17:01Previously, our diagram, when we had if, elif, elif in place,
0:17:05looked a little something like this.
0:17:07And notice, they began, we might have asked one question, or two,
0:17:11or worst case, three whole questions.
0:17:13But we can do better than that, using else, as Hope proposed,
0:17:17we can whittle this diagram, now, down to this.
0:17:19And even though it looks like the diagram's getting bigger,
0:17:22notice that it's having fewer building blocks inside of it.
0:17:25There's fewer arrows and there's fewer nodes in this picture.
0:17:29Let's start at the top now.
0:17:30Start leads us to the first question, still. x less than y?
0:17:34If the answer is true, great.
0:17:35We can say as much, x is less than y, and we can stop.
0:17:38If it's not true, if it's false, we can ask the next question.
0:17:41x is greater than y, true or false?
0:17:43If it is, great.
0:17:44We can print x is greater than y, and stop.
0:17:47Else, if it's not the case that x is greater than y, the answer is false.
0:17:51We can just immediately, logically, say x is equal to y.
0:17:56We don't have to add the third question at all.
0:17:58We can just immediately conclude there.
0:18:00So what's the implication here?
0:18:02You can see, with these pictures, a relative decrease
0:18:05in the complexity of a program.
0:18:07The first one was very long and stringy, with lots and lots of questions,
0:18:10unnecessarily, ultimately.
0:18:12The next one got a little shorter.
0:18:13And this one's even shorter still.
0:18:15And again, the fewer lines of code you have, the less likely
0:18:19you are, arguably, to make any mistakes.
0:18:21The easier it is for other people to read.
0:18:23And so, generally, this readability, this simplification,
0:18:26is, indeed, a good thing.
0:18:28Well, let's go ahead and add another piece of capability to Python,
0:18:33and that's this one here.
0:18:34Just like in English, where you can ask this question or this other question,
0:18:37you can say the same thing in Python using literally this word or.
0:18:41So let me go back to my Python code here.
0:18:44And let's propose how we might ask a couple of questions
0:18:47at once this time, perhaps this time considering how we might ask not
0:18:51whether or not it's greater than or equal to,
0:18:54and caring about the precise answer.
0:18:56Let's take a coarser approach here.
0:18:58And let's just try to determine is x equal to y or not?
0:19:04Well, let me go ahead and delete some of this code
0:19:06and change the question we're asking.
0:19:08Let me do this-- well, if I care about whether it's equal or not,
0:19:12let's check the possible scenarios.
0:19:14If x is less than y or x is greater than y, let's go ahead
0:19:19and print out x is not equal to y.
0:19:23Now why is that, no pun intended?
0:19:26If x is less than y, well, it's obviously not equal.
0:19:29If x is greater than y, it's obviously not equal.
0:19:31So we can conclude x is not equal to y.
0:19:35So if we, instead, want to make sure that it is equal to,
0:19:41we can just use Hope's else, using print quote, unquote x is equal to y.
0:19:47And again, why is this?
0:19:49Well, if x is less than y, or x is greater than y,
0:19:52they're obviously not equal.
0:19:53Otherwise, logically, they must be equal, in fact.
0:19:56So let's run this.
0:19:57Let's go ahead and run Python of compare.py.
0:19:59What's x?
0:20:00One.
0:20:00What's y?
0:20:01Two.
0:20:02OK, x is not equal to y.
0:20:03Let's do it again, put two for x, one for y. x is not equal to y.
0:20:08And one third time, how about x is one and y is one.
0:20:12x is now equal to y.
0:20:14Now if we want to compare that visually, too,
0:20:17let me propose that the picture looks a little something like this.
0:20:20And again, this is the exact same thing logically,
0:20:23but it's a pictorial representation thereof.
0:20:25What's the first question?
0:20:26Well, if x is less than y, well, then we follow the true arrow.
0:20:30And we say quote, unquote x is not equal to y.
0:20:33And then we stop.
0:20:35But what if x is not less than y?
0:20:37What if it's greater than y?
0:20:38What if it's two and one, respectively?
0:20:40Then the answer to x less than y, first question, is false.
0:20:44So we go here.
0:20:45We ask the second question, because of the or,
0:20:48and that asks is x greater than y?
0:20:51If so, notice this, we can kind of reuse some of the same parts of this picture,
0:20:55and just say x is not equal to y.
0:20:58We don't need to add arrows and ad boxes unnecessarily.
0:21:01We can reuse lines of code, parts of the picture, just as we have lines of code.
0:21:06And then we stop.
0:21:07Lastly, we have the following.
0:21:09If we know that x is not less than y, we know
0:21:12that x is not greater than y, it must be the case that x equals y.
0:21:16We don't need to ask a third question, another diamond.
0:21:18We can just immediately print as much, and then say stop, as well.
0:21:24Well, what could I do here?
0:21:25I bet I could improve this code slightly.
0:21:28And if we really want to be nitpicky, I would
0:21:31argue that this is now really just a minor refinement,
0:21:34but it's a good habit to get into thinking about.
0:21:37Could my code be better?
0:21:38Could my code be simpler?
0:21:41Could I improve this code further?
0:21:43It's subtle, but could I improve the design?
0:21:47Could I ask fewer questions?
0:21:48Could I tighten it up, so to speak?
0:21:52What do folks think?
0:21:54SPEAKER 3: You can ask is x is just equal to y.
0:21:58Then if you print x is equal to y, else x is not equal to y.
0:22:03DAVID MALAN: Perfect.
0:22:04Recall one of the other symbols we saw on the available list earlier.
0:22:07We can check not just less than, or greater than, or equal to.
0:22:10We can literally ask the question is it not equal to?
0:22:13Why are we wasting time asking if it's less than or if it's greater than?
0:22:17Well, if all you care about is is it not equal, I think we can do exactly that.
0:22:21Let's just ask the one simple question we do care about.
0:22:24And so let me go back up here.
0:22:25And let me just say not both of these questions, let's get rid of the or.
0:22:29Let's just say if x is not equal to y, then go
0:22:33ahead and print x is not equal to y.
0:22:36And that, too, I think is going to work exactly the same.
0:22:39But the picture now looks a little bit different.
0:22:41Notice that this was our flow chart earlier,
0:22:44that represented that same logic.
0:22:45And there's a bit of complexity.
0:22:47You've got to go left, you've got to go right,
0:22:48based on the answer to these couple of questions.
0:22:50If we now take into account what this version of the program looks like,
0:22:53it's even simpler, perhaps the simplest one we've seen yet.
0:22:56When we start off the program, we ask just one, and only one, question,
0:23:00is x not equal to y?
0:23:02And if so, true, we go ahead and print out x not equal to y.
0:23:06If the answer is false, then, of course, it must be equal to y,
0:23:10so we say that instead.
0:23:12And if we really want, we could invert this.
0:23:14If I go back here to my code, and if, for whatever reason,
0:23:17you just prefer to think in terms of equal or not equal,
0:23:20as opposed to not equal or equal, it's really up to you.
0:23:25We could change this to be equals equals.
0:23:27But I'm going to have to change my print statements to be in the opposite order.
0:23:32So let me go ahead, now, and reverse these two here,
0:23:34and move the second one first and the first one second.
0:23:38So now, when I execute this code, I'm asking still just one question.
0:23:42So it's still just as good, just as succinct.
0:23:44But now the diagram, instead of looking like this,
0:23:47is going to change the not equal to equal equal.
0:23:50And we just need to make sure that we print out the right thing, accordingly.
0:23:54And again, here too, just as the code is getting a little more compact, a little
0:23:57more compact, with fewer and fewer characters,
0:24:00so are these diagrams, these flow charts capturing the relative simplification
0:24:05of each of those programs, too.
0:24:08Let me go ahead and pause here to see if there's any questions, now, on any
0:24:11of these versions of code.
0:24:16SPEAKER 4: Yeah, I have a couple of questions.
0:24:19What if indentation is not used?
0:24:22DAVID MALAN: If indentation is not used, your program will not work.
0:24:25So Python is a little different from a lot
0:24:28of languages in that it enforces the indentation requirement.
0:24:32Some of you who have been programming for years
0:24:34might not necessarily be in the best habit of indenting your code properly.
0:24:37And one of the features, arguably, of Python
0:24:40is that it makes you indent your code, or it will not just work.
0:24:44And I think, did you have one other question?
0:24:47SPEAKER 4: Yeah, is the colon necessary?
0:24:50DAVID MALAN: Is the colon necessary?
0:24:52Yes, the colon, too, is necessary.
0:24:55So with Python, what you see is what you get here.
0:24:57And, indeed, it needs to be indented and the colon is necessary.
0:25:01Python does not use, in the same way by convention as C, and C++, and Java,
0:25:05curly braces to connote blocks.
0:25:07Instead, it relies, indeed, on this indentation.
0:25:10Well, let me propose that we introduce one other keyword here in Python,
0:25:14to see exactly how we might combine additional thoughts.
0:25:17And that's going to be literally the word and, a conjunction of one,
0:25:20or two, or more questions that we might want to ask at once.
0:25:24And let me propose, here, that we explore this kind of logic
0:25:28by way of another program altogether, in VS Code, whereby I'll go ahead now
0:25:32and create a new program, say, called grade.py.
0:25:35Let's consider exactly what grade a student should get,
0:25:38based on their score on an exam, or a test, or a quiz,
0:25:40or some other assignment like that.
0:25:42I'm going to go ahead and run code of grade.py, to give myself a new file.
0:25:46And I'm going to go ahead and start by just getting the user's score, again,
0:25:49on some assignment, or test, or the like.
0:25:51And I'm going to store it in a variable called score, equal the return
0:25:55value of the int function, which is going to convert whatever the user's
0:25:58input is when prompted for this score.
0:26:00So again, the user should just oblige by giving me a number like zero, or one,
0:26:04or two, or hopefully much higher than that, like 97, 98, 99, 100,
0:26:09assuming the test or assessment is out of 100 percentage points.
0:26:13Now, how could I go about assigning a grade to the student's score?
0:26:17Well in the US, it's very commonly the case
0:26:19that if you get between a 90 and 100, that's an A.
0:26:22And if it's between an 80 and a 89, it's a B. If it's 70 and 79, it's a C,
0:26:29and so forth, all the way down to F, which should be E,
0:26:32but we'll see that there's a bit of a jump.
0:26:34So how might I express this?
0:26:35Well, I can use conditionals.
0:26:36And I can ask a few questions and then print out the student's grade
0:26:39accordingly.
0:26:40So let me express it like this, if the student's score is
0:26:44greater than or equal to 90, and the student's score is
0:26:47less than or equal to 100, so it's in that range, let's go ahead
0:26:51and print out that their grade shall be an A. Because they're in the 90s,
0:26:55above grades range.
0:26:58elif the score is greater than or equal to 80,
0:27:02and the score is less than or equal to, say, 89, but here I have some options.
0:27:07Logically, I can actually express myself in any number of ways.
0:27:11And maybe just to be a little cleaner, I'm
0:27:12going to say a score is less than 90.
0:27:15So I'm using less than instead of less than or equal to.
0:27:18So I'm making sure that their boundaries between these grades are correct.
0:27:21Then, I'm going to go ahead and give the student a B if it's in the 80s.
0:27:26elif score is greater than or equal to 70, and the score is less than 80,
0:27:31I'm going to go ahead and give them a C.
0:27:34elif the score is greater than or equal to 60, and the score is less than 70,
0:27:40I'm going to go ahead and give him a D. And here's
0:27:43where it's a little anomalous, at least in some schools here, else
0:27:46I'm going to go ahead and give them an F. So we're skipping E altogether,
0:27:51and we're going to give an F, instead, for the grade.
0:27:53So that's the catch-all.
0:27:55And I think, logically, I've gotten this correct,
0:27:58at least based on where I went to school growing up,
0:28:00such that it's going to give an A, or a B, or a C, or a D,
0:28:03else it's going to assume that you got an F.
0:28:06Well, let's try just a few of these here.
0:28:08Let's run Python of grade.py.
0:28:10My score is, let's start strong, 100.
0:28:13I got an A. Didn't do as well the next time, maybe it's a 95--
0:28:17still an A. Starting to slip further, so I got an 89 the next time.
0:28:21That's now, say, a B. And let's say I really had a bad week,
0:28:25and it's now a 71.
0:28:27That's now a C. Or I didn't even submit it at all, that's an F, altogether.
0:28:31So it seems to work.
0:28:32That's not really an exhaustive test, but at least
0:28:35based on some sampling there, my code seems to work as I expect.
0:28:38But let's see if we can't tighten this up.
0:28:40It's not wrong.
0:28:41It's correct.
0:28:42And, indeed, according to my own specifications,
0:28:44I dare say this code is correct.
0:28:45But can we tighten it up?
0:28:46Can we reduce the probability of bugs, now or down the line?
0:28:50Can we increase the readability of it?
0:28:52And can we increase the efficiency of it?
0:28:54Can we get the computer to have to answer fewer questions
0:28:57and still get the same result?
0:28:59Well, let's see what we might do.
0:29:00Let me just switch things up, if only to demonstrate that we can
0:29:03use these symbols in different ways.
0:29:05I could say, as I've done, if score is greater than or equal to 90.
0:29:10But I can actually do this, I can flip it around.
0:29:12Instead of saying greater than or equal to,
0:29:14let's say 90 is less than or equal to score.
0:29:19And here, let's say if 80 is less than or equal to score.
0:29:23And here, 70 is less than or equal to score.
0:29:28And then, lastly, 60 is less than or equal to score.
0:29:31So it's the same thing, logically.
0:29:33I'm just switching things around, just like you could do on paper pencil
0:29:36if you really wanted.
0:29:37But now notice this trick.
0:29:39And this is not possible, for those of you who have programmed in C, or C++,
0:29:42or Java, or other languages.
0:29:44Notice what I can do here is actually combine these ranges.
0:29:48Notice that I'm asking two questions, two Boolean expressions.
0:29:52Is 90 less than or equal to score, and is score less than or equal to 100?
0:29:57Well, Python allows you to nest these things like this,
0:30:01and chain them together.
0:30:02And just like you would on paper pencil in the real world,
0:30:06you can encode in Python, do this, which is just a little cleaner.
0:30:09It's tightening up the code a little bit.
0:30:11It's fewer keystrokes.
0:30:12It's faster to type.
0:30:13It's easier to read, moving forward.
0:30:15So that's arguably better, as well.
0:30:18So that's one improvement.
0:30:19It's largely aesthetic, in this case.
0:30:21It's still asking the same number of questions,
0:30:23but it's doing it a little more succinctly still.
0:30:26Well, what more could I do here next?
0:30:29Well, you know what?
0:30:30Each time I'm deciding these grades, I don't
0:30:32think I have to ask two questions.
0:30:34I don't have to ask, is it greater than 90 and less than 100?
0:30:38Is it greater than 80 and less than 90?
0:30:40If I rethink my logic, I can maybe do this better still.
0:30:45Let me propose that we simplify this further, and just do this.
0:30:48If we know that input, for the moment, is going to be within 0 and 100,
0:30:53we can make some assumptions.
0:30:54We could say something like, if the score is greater than or equal to 90,
0:30:58well, the student gets an A. elif the score is greater than or equal to 80,
0:31:04the student gets a B. elif score is greater than or equal to 70,
0:31:08they get a C. elif the score is greater than or equal to 60,
0:31:13they get a D, else they get an F. So what have I done here?
0:31:19Well, instead of asking two questions every time,
0:31:23checking the lower bounds and the upper bound of that range,
0:31:26I'm being a little more clever here by asking if the score is greater than 90,
0:31:31well, they've obviously gotten an A or better.
0:31:33If your score is greater than 80, well, you either
0:31:36deserve an A if it's really strong, or a B if it's just above 80.
0:31:40But because of the elif logic, we've already checked
0:31:44is the student's score greater than 90?
0:31:46And if it's not, then we're asking the question, well, is it greater than 80?
0:31:50So you implicitly know it's somewhere in the 80 to 89 range,
0:31:54else you know it's in the 70 to 79 range, else it's in the next range
0:31:58down.
0:31:59So it's a minor optimization that allows us to ask fewer questions.
0:32:02But again, it's making the code, arguably, a little more readable,
0:32:05certainly more succinct, an then, hopefully, more maintainable
0:32:09longer term.
0:32:10Any questions, then, on these types of changes,
0:32:15and this type of logic with our code?
0:32:20SPEAKER 4: What if we don't use elif at all?
0:32:22What if we write the code in if?
0:32:25DAVID MALAN: Yeah, so that's a good question,
0:32:27because it's actually going to have an unintended effect here.
0:32:31Let me get rid of the F temporarily, and just
0:32:33focus on A through D. If we revert to where
0:32:36we began today's story, with conditionals, saying if,
0:32:39if, if, if, now our cleverness here of using broader strokes
0:32:45and not using an upper and lower bound ranges
0:32:47is going to come back to be a downside.
0:32:51Let me go ahead and run Python of grade.py.
0:32:53And suppose my score is 95.
0:32:56I am so darn excited.
0:32:58I want my A, but nope.
0:33:00I just got an A, a B, a C, and a D. So logically, that's broken things.
0:33:06Because if you don't make these conditions mutually exclusive,
0:33:09every one of those questions is going to get asked, and therefore answered.
0:33:13And even if your grade is above a 90, it's
0:33:16also, logically, above an 80, above a 70, above a 60,
0:33:20and if I'd kept it in there, I would have failed, as well, with an F.
0:33:23Really good question.
0:33:24Other questions here, on this form of logic?
0:33:28SPEAKER 5: Would there be any better way to clean up
0:33:30even just this simple statement, like we had before,
0:33:33the previous one that you had with the elif?
0:33:36DAVID MALAN: I like your enthusiasm for simplifying things further.
0:33:40I'm going to go out on a limb here and say this is about as good as it gets,
0:33:45at least using only conditional statements.
0:33:48I can, if my mind wanders, think of a slightly more clever way
0:33:52to do this, maybe with something called a loop,
0:33:54or another programming construct.
0:33:55We don't have that yet in our vocabulary.
0:33:57But yes, there's absolutely other ways to do it.
0:33:59But I think not yet if we want to restrict ourselves
0:34:01to just words like if, and or, and else, and elif, and and, and the like.
0:34:07Well, let me propose that we pivot now to use another approach here
0:34:10that uses one other symbol that, up until now,
0:34:12we've not really had occasion to use.
0:34:14Let me propose that we implement a program that we'll call parity.
0:34:18In mathematics, parity can refer to whether a number is even or odd.
0:34:22And that's kind of an interesting question.
0:34:24And it turns out it can be useful in other applications,
0:34:26too, to just ask the question is a given number even or odd,
0:34:29maybe that the user typed in?
0:34:31And let me go ahead and write a new program
0:34:33called parity.py, via code parity.py in my terminal.
0:34:38And let me propose that we use this as an opportunity
0:34:41to introduce the last of those arithmetic symbols,
0:34:45at least most of which we're familiar with, addition, subtraction,
0:34:48multiplication, division.
0:34:49But there's been on this list before, this last one here, a percent sign.
0:34:53And it doesn't mean percentage in this case,
0:34:55when used as an operator in programming in Python.
0:34:57Rather, it represents the so-called modulo operator,
0:35:01for modular arithmetic.
0:35:02Or, at least in our case, we're going to use it to calculate the remainder when
0:35:05dividing one number by another.
0:35:07Well, what do I mean by that?
0:35:09Well, if you take a number like one divided by three,
0:35:12three does not go into one cleanly.
0:35:14So you have a remainder of one.
0:35:16Two divided by three has a remainder of two.
0:35:20Three divided by three has a remainder of zero, because it divides cleanly.
0:35:24Four divided by three has a remainder of one, because you can divide it in once,
0:35:30but then that leaves one, so it has a remainder of one.
0:35:32And then lastly, something like five divided by three
0:35:35has a remainder, of course, of two.
0:35:37So that's all we mean by remainder, how much is left over
0:35:39after dividing one number by another.
0:35:41Well, if I go back now to my code, and I consider how I might implement
0:35:46the question is this number even or odd?
0:35:49Let's consider how we might implement that,
0:35:51since it's perhaps not necessarily obvious how we
0:35:53can use this additional building block.
0:35:55But it turns out it's going to be very useful longer term.
0:35:58Well, let's first just get a number from the user in a variable called x.
0:36:01And I'm going to set that equal to the conversion to int
0:36:04of whatever the user inputs, after asking them what's x, question mark.
0:36:08And we've done that before, many times.
0:36:10How do I now determine if x is even or odd?
0:36:14Well, it turns out, if I have access to a programmatic operator that tells me
0:36:19the remainder, I think I can do this.
0:36:21In fact, let me just ask the group.
0:36:23And this is just from grade school math, perhaps,
0:36:25what does it mean for a number to be even, ?
0:36:28To be clear, a number like 0, 2, 4, 6, 8, 10, 12, 14, 16,
0:36:36those are all even numbers.
0:36:37But what does that really mean?
0:36:38Elena, if I'm saying that right?
0:36:40ELENA: Even numbers that can divide it exactly by two.
0:36:43For example, 2, 4, 6, 8, and 10, and--
0:36:48DAVID MALAN: Perfect.
0:36:49And we could go on all day long, literally,
0:36:51since there's an infinite number of those even numbers.
0:36:53But it's nice that you formulated it in terms of a question
0:36:56that we can ask very clearly.
0:36:58Is this number cleanly divided by two?
0:37:01That is, can we divide it by two with no remainder, a remainder of zero?
0:37:05Well, that's perfect, because if we have this operator, this percent sign, that
0:37:09allows us to answer just that, what is the remainder, we can presumably check
0:37:13is the remainder zero, or is it one?
0:37:15Do we have nothing left over, or do we have one left over?
0:37:19Well, let's ask that.
0:37:20If x divided by two has a remainder of zero, as Elena proposes, let's go ahead
0:37:28and print out something like quote, unquote even.
0:37:30And just say as much to the user.
0:37:32else, I think we can assume that if a number's not even,
0:37:35it's going to be odd, if it's, indeed, an integer.
0:37:38So I'm going to go ahead and print out quote, unquote odd instead.
0:37:41And let's go ahead and now run Python of parity.py in my prompt.
0:37:45What's x?
0:37:45Let's start with two.
0:37:46Two is, in fact, even.
0:37:48Let's start with four.
0:37:49Four is, in fact, even.
0:37:50Let's get interesting with three.
0:37:53Three is now odd.
0:37:54And I think we could do that all day long and hopefully get back, indeed,
0:37:57exactly that answer.
0:37:59But what more could we do here?
0:38:02How could we improve upon this?
0:38:03Well, recall that we have the ability to invent our own functions.
0:38:08And let me just propose, for the sake of discussion,
0:38:10that we're going to eventually find that it's
0:38:12useful to be able to determine if a number is even or odd.
0:38:14And so we'd like to have that functionality built-in.
0:38:17And I don't think Python has a function for telling me just that.
0:38:20But I can invent it using code like just this.
0:38:23So let me go into my earlier version here.
0:38:26And let me propose that we do this.
0:38:29Let me go ahead and write a main function.
0:38:32I'm going to get back into that habit of defining a main function to represent
0:38:36the main part of my program.
0:38:37And I'm going to do what I did before.
0:38:39I'm going to get an integer from the user's input,
0:38:41asking them what's x, question mark.
0:38:44And then I'm going to ask this question.
0:38:46For the moment, I'm going to naively assume
0:38:48that the function already exists, but that's
0:38:50a useful problem-solving technique.
0:38:52Even if I have no idea yet where I'm going with this,
0:38:55how I'm going to invent a function that determines if a number is even,
0:38:58I'm just going to assume that there's a function called "is even,"
0:39:01and I'm going to call it, blindly, like this.
0:39:04If is even, passing in x, then go ahead and print quote, unquote even.
0:39:11So if this magical function called "is even" returns true, as its return value
0:39:17I am going to print out that it's even.
0:39:19Else, otherwise, I'm going to assume that it's, of course, odd.
0:39:23Now the one problem with this program, even if I call main over here,
0:39:27is that is even does not exist.
0:39:30And this program would break if I ran it right now.
0:39:32But that's OK.
0:39:33I have the ability, recall, to invent my own function.
0:39:35So let me define, with def, a function called "is even."
0:39:39I want this function to take an argument.
0:39:42And I'm going to call it n, just a number, generically.
0:39:45I could call it x.
0:39:46But again, I don't want to confuse myself as to which x is which.
0:39:49So I'm going to give it a different name, and that's fine.
0:39:52I'm just going to call it, more generically, n for number.
0:39:54And then I'm going to do this.
0:39:56I'm going to say if N % two equals equals zero, just like before, then,
0:40:03and here's the magic, you, the programmer,
0:40:06can actually return what are called Boolean values.
0:40:10We've seen in Python that Python has stirs or strings, ints or integers,
0:40:16floats or floating point values, all of which
0:40:19are different types of data in Python.
0:40:21Python also has a fourth data type called bool for a Boolean value.
0:40:26And even though this is just adding to our list, the nice thing about bools
0:40:29is that they can only be true or false.
0:40:32An int can be any number of an infinite possible values.
0:40:36A bool can only be true or false.
0:40:39And it must be capital T and capital F if you're writing itself.
0:40:43So if I go back now to my code, and I consider
0:40:46exactly what I want to return here.
0:40:49Well, if n % two equals equals zero, that is,
0:40:53if n divided by two has a remainder of zero, well, I think it's even,
0:40:58to, Elena, your definition.
0:40:59So let's return true, capital T. else, if it doesn't have a remainder of zero,
0:41:05I'm pretty sure, mathematically, it's got to have a remainder of one.
0:41:08But it doesn't matter.
0:41:09I know it's not even, so I'm going to return false.
0:41:13And we return false, instead capital F. And now that we've defined both main
0:41:18and is even, and I'm calling main at the bottom, I think I've got this right.
0:41:23Python of parity.py, Enter.
0:41:25What's x?
0:41:26Let's try something simple, like two.
0:41:28And it's even.
0:41:29Let's do it again.
0:41:30What's x?
0:41:31How about four?
0:41:32Even.
0:41:33Once more, what's x?
0:41:34How about three?
0:41:35And it's odd.
0:41:36Now, what have I done here?
0:41:38I've just made the point that if I want to create my own function called "is
0:41:42even," that answers this question for me,
0:41:44that I can now use, in this program, and heck, maybe future programs
0:41:47that I write, I now have a function that no one gave me,
0:41:51I gave myself, that I can use and reuse.
0:41:53And I can even, perhaps, share it with others.
0:41:55I'm using that function now on line three, just to make a decision.
0:41:59I'm using a conditional up there.
0:42:01And my Boolean expression, something that's true or false,
0:42:05is going to be not something explicit, like x less than y,
0:42:08or y greater than x, or the like.
0:42:11It's going to be a function call.
0:42:13I'm using a function as my Boolean expression.
0:42:15But that's OK because I know, because I wrote it,
0:42:18that that function "is even" returns true or it returns false.
0:42:23And that's all I need in a conditional to make a decision
0:42:26to print even or print odd.
0:42:29So let me pause here to see if there's any questions now on how I've
0:42:33implemented "is even," using this bool.
0:42:36SPEAKER 6: Hello, hi David.
0:42:38First of all, thank you for this wonderful class the day
0:42:41before yesterday and today, sir.
0:42:43I have just one query, based on the background of Java.
0:42:47There, when we used to pass the argument,
0:42:50we can also pass the address of the variables.
0:42:53So is there any sort of this concept in Python?
0:42:57DAVID MALAN: Short answer, no.
0:42:58Those who are unfamiliar with Java or other languages, or C, or C++,
0:43:02there's generally ways to pass values in different mechanisms that allow you,
0:43:06or disallow you, to change them.
0:43:07In Python, no.
0:43:08Everything we're going to see is actually, in fact, an object.
0:43:11But more on that down the line.
0:43:13How about time for one more question here on these bools and these
0:43:17"is evens."
0:43:19SPEAKER 7: So I actually had a question about defining a function,
0:43:23if that's OK.
0:43:24DAVID MALAN: Sure.
0:43:25SPEAKER 7: So if you define one, within your code, like you made it up,
0:43:29are you allowed to use the dot operator like we did name dot strip,
0:43:33and use it like that?
0:43:34DAVID MALAN: Good question.
0:43:35If you've created your own function, can you
0:43:37use other functions, like dot strip, or dot title, or dot capitalize,
0:43:42that we've seen in the past?
0:43:44You can use those on strings.
0:43:46Those functions come with strings.
0:43:49You can't necessarily use them on your own functions,
0:43:51unless your function returns a string, for the examples you gave.
0:43:56I'm returning a bool.
0:43:57Bools have no notion of white space to the left or the right.
0:44:00You can't call strip, you can't call capitalize.
0:44:02But if you were writing a different function
0:44:04that returns a string, absolutely.
0:44:06You could use those functions, as well.
0:44:08Well, let me turn our attention, if I may, back to this example
0:44:10here, and consider, as we now frequently do,
0:44:13can we improve on the design of this code?
0:44:15Can I make this particular program better?
0:44:18And I can.
0:44:19There's a couple of ways here.
0:44:20And I'll show you something that's now generally known as something Pythonic.
0:44:24There's actually this term of art, in the Python world,
0:44:26where something is Pythonic if it's just the way you do things in Python.
0:44:31Which is to say, we've seen already there's
0:44:33so many different ways to solve certain problems.
0:44:35And in the Python community of programmers,
0:44:38there tend to be some ways that are smiled upon more than others.
0:44:41And they tend to relate to features that maybe only Python has,
0:44:45but not other languages.
0:44:46And here's some syntax that you might not have seen in languages like Java,
0:44:49or C, or C++ if you've programmed before.
0:44:52And if you've never programmed before, this too is going to be new.
0:44:55Instead of asking a question like this, if else using four lines, in Python,
0:45:02you can actually collapse this into just one more elegant line, if you will.
0:45:07Instead of asking if n divided by two has a remainder of zero,
0:45:12return true, else return false.
0:45:15Let me delete all of that and just say this, return true if n divided by two
0:45:23has a remainder of zero, else return false.
0:45:27Now those of you who do have prior programming experience
0:45:30might actually think this is kind of cool.
0:45:31You can condense, from four lines into one line, that very same thought.
0:45:35And one of the reasons why Python is popular is that it does
0:45:39tend to read rather like English.
0:45:41It's not quite as user-friendly as most English, or most human languages.
0:45:44But notice, now, the line does rather say what you mean.
0:45:48Return true if n divided by two has a remainder of zero, else false.
0:45:55That's pretty darn close to something you might say, logically, in English,
0:45:58be it about even and odd or really anything else.
0:46:02So that program is going to work exactly the same.
0:46:04Python of parity.py, let me type in two.
0:46:06It's still even.
0:46:07Let me type in three.
0:46:08It's still odd.
0:46:09But I can refine this even further.
0:46:12And again, consistent with this idea of not just writing correct code,
0:46:15but writing better and better code, but still keeping it readable,
0:46:19I can do one even better than this.
0:46:22Notice this value here is my Boolean expression.
0:46:25And it is going to evaluate to true or false.
0:46:28Is n divided by two having a remainder of zero or not?
0:46:33That is, by definition, a Boolean expression.
0:46:35It has a yes/no answer, a true/false answer.
0:46:39Well, if your Boolean expression itself has a true or false answer,
0:46:45why are you asking a question in the first place?
0:46:48Why ask if?
0:46:50Why say else?
0:46:51Just return the value of your own Boolean expression.
0:46:57And perhaps the tightest version, the most succinct, and still readable,
0:47:01version of this code would be to delete this whole line, Pythonic
0:47:05though it is, and just return n modulo two equals equals zero.
0:47:12If it helps, let me add parentheses temporarily,
0:47:15because what's going to happen in parentheses will happen first.
0:47:18n divided by two either does or does not have a remainder of zero.
0:47:24If it does, the answer is true.
0:47:25If it doesn't, the answer is false.
0:47:28So just return the question, if you will.
0:47:31You don't need to wrap it, explicitly, with an if and an else.
0:47:35And in fact, because of order of operations,
0:47:37you don't even need the parentheses.
0:47:39So now this is perhaps the most elegant way to implement this same idea.
0:47:45Now, which is better?
0:47:46This is pretty darn good.
0:47:47And it's hard to take fault with this because it's so very succinct.
0:47:51But it's perfectly OK, and just as correct,
0:47:54to have an if and then an else.
0:47:56Even though it might be four total lines, if that helps
0:47:59you think about your code more clearly, and it helps
0:48:01other people reason about it, as well.
0:48:04So it turns out there's another syntax that you
0:48:06can use to implement the same idea of a conditional,
0:48:08whereby you do something optionally, based on the answer to some Boolean
0:48:12expression.
---
## ⏸️ توقفت هنا (0:48:13)
---
0:48:13And the keyword that you can now use, in recent versions of Python,
0:48:17is called this-- match.
0:48:18Match is a mechanism that, if you've programmed before, is similar in spirit
0:48:21to something called switch in other languages.
0:48:24For instance, let me go ahead here and close out parity.py And let me go ahead
0:48:28and create a new file called house.py.
0:48:31And in house.py, I think what we're going
0:48:33to do is try to implement a program that prompts the user for their name,
0:48:37and then just outputs what house they're known
0:48:39to be in in the world of Harry Potter.
0:48:41So for instance, let me go ahead and do this.
0:48:43Let me give myself a variable called name, set it equal to the return
0:48:46value of the input function.
0:48:47And I'll say something like, what's your name, question mark.
0:48:50And then after that, I'm just going to use
0:48:52a traditional if, elif, else construct to decide what house this person is in.
0:48:58So let me say if name equals equals, say Harry, as in Harry Potter, well,
0:49:03let's go ahead and print out Harry's house, which is Gryffindor
0:49:06in the world of Harry Potter.
0:49:08elif the name is, instead, Hermione, then
0:49:11go ahead and print out also quote, unquote Gryffindor,
0:49:15as she's in the same house, too.
0:49:16elif name equals equals Ron, let's go ahead
0:49:19and similarly print out Gryffindor quote, unquote.
0:49:23And let's make this a little more interesting now.
0:49:25elif name equals quote, unquote how about Draco?
0:49:29Draco Malfoy, in the books-- let's go ahead and print out quote,
0:49:32unquote Slytherin.
0:49:33And just in case someone else's name gets inputted,
0:49:36for now, let's just suppose that we don't recognize them,
0:49:39and say, by default, else print out quote,
0:49:41unquote who, question mark, just to convey
0:49:44that we don't actually have a hard-coded response to that particular name.
0:49:48Let me go ahead, now, and run this as Python of house.py, Enter.
0:49:52And I'll go ahead and type in something like Harry.
0:49:54And voila, we see that Harry is, indeed, in Gryffindor.
0:49:57Let's run it one more time, Python of house.py.
0:50:00Let's type in Draco this time.
0:50:01Slytherin.
0:50:02And now, let's type in an unrecognized name.
0:50:05Let's go ahead and rerun Python of house.py.
0:50:07And let's go ahead and type in Padma, Enter.
0:50:10And who?
0:50:10Because we haven't actually hard-coded with an elif condition in this case,
0:50:14what house Padma is meant to be in.
0:50:17Well, it turns out there's other ways to implement this.
0:50:19Indeed, there's some redundancy here, in that
0:50:22we're checking if Harry, or Hermione, or Ron are all in Gryffindor.
0:50:25I feel like we can at least tighten this code up a little bit,
0:50:28using techniques we've seen already.
0:50:30So let me go ahead and do this.
0:50:31Let me go up here and instead do something like this.
0:50:34Let's get rid of these two blocks of elifs,
0:50:37leaving just Harry's for a moment.
0:50:38And let's use that "or" keyword again, and say or name
0:50:41equals equals quote, unquote Hermione, or name equals quote, unquote Ron,
0:50:47thereby consolidating all three cases, if you will, into just one
0:50:51if statement.
0:50:52Then we still have a separate elif for Draco because he's not,
0:50:55in fact, in Gryffindor.
0:50:56And then the final else to catch anyone else.
0:50:59Let me go ahead now and run this version of the program, Python of house.py.
0:51:03I'll type in Hermione this time.
0:51:05She, too, is still in Gryffindor.
0:51:07Let me try it with Ron.
0:51:08And that, too, still seems to be correct.
0:51:10Well, it turns out there's another approach altogether that can perhaps
0:51:13make your code a little less verbose.
0:51:16You could imagine how complicated this code might
0:51:18get if we had not just Harry, and Hermione, and Ron, but a whole bunch
0:51:21of other names as well, for Gryffindor, for Slytherin, and for all
0:51:25of the other Hogwarts houses.
0:51:26So you could imagine that code just getting pretty unwieldy pretty fast.
0:51:29Well, it turns out another technique you can
0:51:31use is, indeed, this keyword called match, which is very similar in spirit,
0:51:34but the syntax is different.
0:51:36And it allows you to express the same ideas a little more compactly.
0:51:39So let me go back to house.py.
0:51:41And let me propose that I get rid of my current if, elif, else approach,
0:51:45and instead do this.
0:51:47Literally use the keyword match, and type the name of the variable,
0:51:51or value, that we want to match on.
0:51:53And then I'm going to go ahead and include a colon.
0:51:55And then underneath that, I'm going to include, literally,
0:51:58a keyword called case.
0:51:59And the first case I want to consider is going to be Harry.
0:52:02And I'm going to put Harry in quotes, because it's a string or a stir.
0:52:05And I'm going to have another colon at the end of this line.
0:52:08And indented under that one, I'm going to go ahead and, for now,
0:52:11print out Gryffindor, which, of course, is Harry's house.
0:52:13Otherwise, I'm going to have another case for quote, unquote Hermione.
0:52:17And similarly, I'm going to have under that indented,
0:52:20print quote, unquote Gryffindor, close quote.
0:52:23Now I'm going to have another case for Ron, also in quotes, with a colon.
0:52:27Now print quote, unquote Gryffindor.
0:52:29And now I'm going to have a other case for, let's say, Draco.
0:52:33This one gets a little more interesting because Draco, of course,
0:52:35now is in Slytherin.
0:52:37And then I'm going to go ahead and leave it as that for now.
0:52:40So let me go ahead and save this file, and go back down to my terminal window,
0:52:44running Python of house.py, Enter.
0:52:46And let's go ahead and try Harry.
0:52:48And he seems still to be in Gryffindor.
0:52:50Let's run it again for Hermione, Enter.
0:52:52Gryffindor.
0:52:53Let's skip ahead to Draco, and type in Draco's name.
0:52:56He is, indeed, in Slytherin.
0:52:57Now let's try another name that we haven't handled
0:53:00a case for, like Padma again, Enter.
0:53:03And we're just ignored.
0:53:04There's no output whatsoever because there wasn't a case for Padma.
0:53:07Now we could, of course, go back in and explicitly add one for Padma.
0:53:11But what if we, similarly to the else construct,
0:53:14just want a catchall that handles anyone whose name is not explicitly specified?
0:53:18Well, turns out the syntax for that, using this new match statement,
0:53:22is to still have another case, but then to use
0:53:24this single underscore character, which is used in other contexts in Python.
0:53:28But for here, it's meant to say whatever case has not yet been handled,
0:53:32go ahead and print out, as we did before, for instance,
0:53:35quote, unquote who, with a question mark at the end.
0:53:38Now let's go ahead and rerun this Python of house.py.
0:53:42I'll type Padma's name again.
0:53:43And this time, I think we're at least going
0:53:45to get an explicit response indicating who,
0:53:48whereas previously we did not have the equivalent of that.
0:53:50Now, I think we've regressed a little bit.
0:53:53We went from tightening things up by putting Harry, and Hermione,
0:53:56and Ron all on the same line in the same if statement.
0:53:59But here, we have now three case statements, again, for all three
0:54:02of those.
0:54:03Well, we can tighten this code up, as well.
0:54:05But the syntax is going to be a little bit different.
0:54:08I'm going to go ahead and delete these two middle cases for Hermione and Ron.
0:54:12And then up here, next to Harry's name, before the colon,
0:54:15I'm going to go ahead and use a single vertical bar, and then
0:54:18a quote, unquote Hermione.
0:54:19Then another single bar and do quote, unquote Ron.
0:54:23And this is how, using this relatively new match statement,
0:54:26you can say the equivalent of Harry, or Hermione, or Ron,
0:54:30but more concisely than you could using an if statement
0:54:33alone, as we implemented it previously.
0:54:35So now, one final run of the program with Python of house.py.
0:54:40Let's make sure that Harry is still in Gryffindor.
0:54:42Let's make sure that Hermione is still in Gryffindor.
0:54:44Let's make sure that Ron is still in Gryffindor.
0:54:46And indeed, all three of them are.
0:54:48Now, as always with Python and programming more generally,
0:54:51there's going to be different ways you can solve these problems.
0:54:54This is just another tool in your toolkit.
0:54:56Arguably, it has tightened things up.
0:54:58Arguably, it's perhaps a little more readable
0:55:00because there's a little less syntax going on,
0:55:02a little less duplication of equal signs and elif,
0:55:05and elif, and elif all over the place.
0:55:07But ultimately, this would be an equally correct approach to that same problem.
0:55:11But it turns out with a match statement you
0:55:13can do even more powerful forms of matching, as well.
0:55:16Here, we've used it simply to implement the same idea as that if, elif,
0:55:20else construct.
0:55:21And it's worth noting, if you've programmed in some other language,
0:55:24the syntax here is, indeed, correct.
0:55:26You do not need, for instance, a break statement,
0:55:28as has been peppered throughout.
0:55:29And you don't need something like default, or something explicit.
0:55:32You, indeed, just use this underscore as your catchall at the end of the match.
0:55:37So just by adding in some of these new keywords
0:55:40here, like if, and elif, and else, we have now the ability
0:55:45to ask questions about values.
0:55:47We have the ability to analyze input from users,
0:55:50and ultimately make decisions about it.
0:55:52And these, then, where our conditionals.
0:55:54Lying ahead is going to be the ability for us to not only use functions,
0:55:58and variables, and also these conditionals,
0:56:00but also, next, loops-- the ability to do something, now, again and again.
