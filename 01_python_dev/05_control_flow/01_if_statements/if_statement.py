# if statement is an amazing and important concept in any programming language
# We will have a look at if elif and else to handle a control flow of our program

# I am sure we have been to cinema to watch a movie one time or another
# There are automated cinema ticket machine and asks questions against the age restriction applied to the movie before issuing the ticket

age = 15
# step 1
if age >= 18:
    print("Thank you, please proceed to buy a ticket ")
# step 2
elif age < 18:
    print("Sorry you are not at the correct age to watch this movie, please choose something else")
# step 3 - we can also use elif instead of second if
# what if anything else is entered by customer
else:
    print("Opps This is not a correct again, please try again")