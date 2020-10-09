# if statements

https://www.youtube.com/watch?v=m2Ux2PnJe6E 

## Timings

45 - 60 Mins

## This lesson includes

* using if
* else if - elif
* cleaning up with else 
* there are no switch or case statements 

This will be a basic introduction into the use of if statements and they will be common place throughout your coding career.

## using if

The if statement itself is a core staple of handling control flows allowing you to pass variables that meet certain criteria through a group of clauses to action against. There is no better way to see this other tha nto get started.

first of all let's consider an automated cinema ticket machine and asks the question are you over 18? it would need to respond accordingly dependent on the input (and of course trusting that people are honest)

```python
age = 19

if age > 18:
    print("You are the correct age to watch this film and can buy a ticket")
```

* `age = 19` - set our age variable as 19
* `if age > 18:`  as you can see the if statement need to use an operator to actually action the clause. If statements need an argument at each stage to then action a piece of code
    * `print("You are the correct age to watch this film and can buy a ticket")` - this will only execute when the age variable is over 18.
    
If we now run the code we should see the if statement print.

but what if we put 18 in?... if you put 18 in and run the code we should see nothing because 18 is equal, therefore we need to use the equals sign alongside the greater than operator:

```python
age = 19

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")
```

Now if we run our code again we should see the correct print message again. if we change our age variable to 15 and run the code once again we receive nothing due to the fact that we do not have a statement to capture this. Now we could write it as below:

```python
age = 15

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")

if age < 18:
    print("I'm afraid you are not the correct age to watch this film")

```
Now the above code will work fine if you play around with the age variable but it is important to know that theses are two completely different clauses and when writing large bulk processes within these files it can become difficult to follow and there is a much more elegant way.

## if, else if (elif)

As there can be multiple statements in place and all relating to an age check it makes sense to keep them cleanly under one statement:

```python
age = 15

if age >= 18:
    print("You are the correct age to watch this film and can buy a ticket")
elif age < 18:
    print("I'm afraid you are not the correct age to watch this film")
```
the `elif` is the same as the if statement in it's need to validate something and should be treated in the same way i.e. you are making a decision against two reference points.

if you now change the age you should see the same output as the two if statements but are now cleanly contained under the one control block and is easier to read to boot!

That' great if all films were managed by age ratings but there are some open ranges such as PG & Universal.

let's try out new code as below and remember to comment out the previous code.

```python
film_rating = "Universal"

if film_rating.lower() == "universal":
    print("all age groups can watch this film")
elif film_rating.lower() == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif film_rating.lower() == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
elif film_rating.lower() == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
```

running the code here will return "all age groups can watch this film" and you will see that we've used the `or` statement to cover both 12 and 12A. note that the must state what it is matching against i.e. you could write the below:

`elif film_rating.lower() == "12" or "12a":` as clean and as tempting as this may look it simply won't work.

## Cleaning up with else

There is one last area we have not yet discussed which is what happens if we pass a film rating that is not picked up??? that's right nothing will happen and this is where the `else` statement comes into play.

The `else` statement captures anything that is not picked up in the rest of the statement and is essentially a catch all so add the else statement as below:

```python
film_rating = "12a"

if film_rating.lower() == "universal":
    print("all age groups can watch this film")
elif film_rating.lower() == "pg":
    print("General viewing, but some scenes may be unsuitable for young children.")
elif film_rating.lower() == "12" or film_rating == "12a":
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif film_rating.lower() == "15":
    print("No one younger than 15 may see a 15 film in a cinema.")
elif film_rating.lower() == "18":
    print("No one younger than 18 may see an 18 film in a cinema.")
else:
    print("this is not a correct rating, please use unniversal, pg, 12, 12a, 15, 18")
``` 

You will see that we do not need to pass any arguments to the else statement as it is a blanket capture all. If you now change the `film_rating` to something that is not within the if/elif clauses it will now be picked up by the else clause.

## There are no switch or case statements 

In other languages there are such things as switch clauses or case statements that serve close to the same purpose as the if statement. Python has chosen to kindly bin these functions in the view of keeping code (and libraries) DRY! and I for one am grateful for it :-)

## Summary

although this is a basic run through you have seen that you can use the if, elif and else statements quickly and easily. We will be seeing much more as we go through this course, in fact I would be bold enough to say it will be a rare occasion in a program where an if statement won't occur.

You just:
* using if
* else if - elif
* cleaning up with else 
* there are no switch or case statements 