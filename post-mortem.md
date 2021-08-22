# What was the purpose of your program?

To view and search a database of registered users. 

# How could your program be useful in the real world?

The program would be useful for the real world anywhere where someone would be writing a large piece of software, including a login and registration system. This would be a registration or user database module in that larger program. 

# What is a problem you ran into, and how did you fix it?

I ran into a good deal of problems, and in fact I don't really consider the program 100% finished, as my ambitions for the program would have taken too long to put into place. 

Problems that I encountered, but overcame: 
 - line 24, I had tried to make that an if statement, and for the life of me I couldn't figure out how to make that work, but I'm happy with the solution I discovered. 
 - pretty-printing the data, I used the "tabulate" module for this. 
 - you could enter a player number of 0 and it gives you the top row of the csv file
 - the search function (on line 42) didn't work 100%, more specifically, sometimes it doesn't find a result if the query has a capital letter, and sometimes it prints lines multiple times (because it goes by entry and not by line, I don't know how to fix this)

# Describe one thing you would do differently the next time you write a program.

Well, several of the problems I outlined in the above question were still unfixed when I was writing the postmortem and I was just going to submit it as is, but explaining them out made me think of solutions for them. Maybe I should capitalize on that in future projects. 

# How could your program be generalized and useful in other areas? 

Anywhere where a database of information needs to be read, and if it's expanded upon, maybe written to as well. 
