# Game plan

## Problem Definition
Tic Tac Toe (TTT) game: Player 1 and Player 2 will take turns to input their desired position to place their marks (X or O). One winner will emerge when a player succeeds in placing three of their marks in a horizontal, vertical or diagonal row.

### Program stop conditions:
- Win condition: 1 user to have consecutive hatch positions be it horizontally, vertically or diagonally. (Loser will be the other user)
- Draw condition: No consecutive positions met when all hatch positions are filled.
- Restart game condition: Abrupt stop to restart all values
### Inputs
- 1 digit whole integer only from positions 1 to 9 
### Output
- A sequence of user input or if no values are changed at the position then it will be default as its position value.

```
# Displays this

  1 | 2 | 3 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9 

```

## Cases
### Initial case
- At INITIALIZE: Display TTT table at each individual position to user (see bottom code)
	- Updates TTT table with user input 
	- Program validates end conditions at every user input
	- Show win condition and 'Win text'

```
# At INITIALIZATION Displays this

  1 | 2 | 3 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9 

# Prompt for user input
[First User]
Enter your desired position in whole number (1-9): _

```

### NG Cases
```
(a) Reject all inputs except for integers 1 - 9
Inputs: i, asd, 12, -230, [], 0, symbols etc.
Output: Please enter a 1 digit whole number from 1 to 9 only.

(b) Catch already entered inputs:
[First User]
Enter your desired position in whole number (1-9): 1

Output:
  X | 2 | 3 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9 

---------------------------------------------------------

[Second User]
Enter your desired position in whole number (1-9): 1

Output:
  X | 2 | O 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9 

Error: Second User please try again with another number.
#TODO maybe can give user suggestions (Low priority)
---------------------------------------------------------

```

### OK cases:
```
# Draw condition

[First User]
Enter your desired position in whole number (1-9): 1

Output:
  X | 2 | 3 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9 

---------------------------------------------------------

[Second User]
Enter your desired position in whole number (1-9): 3

Output:
  X | 2 | O 
 -----------
  4 | 5 | 6 
 -----------
  7 | 8 | 9 

---------------------------------------------------------

[First User]
Enter your desired position in whole number (1-9): 5

Output:
  X | 2 | O 
 -----------
  4 | X | 6 
 -----------
  7 | 8 | 9 

---------------------------------------------------------

[Second User]
Enter your desired position in whole number (1-9): 9

Output:
  X | 2 | O 
 -----------
  4 | X | 6 
 -----------
  7 | 8 | O 

---------------------------------------------------------

[First User]
Enter your desired position in whole number (1-9): 6

Output:
  X | 2 | O 
 -----------
  4 | X | X 
 -----------
  7 | 8 | O 

---------------------------------------------------------

[Second User]
Enter your desired position in whole number (1-9): 4

Output:
  X | 2 | O 
 -----------
  O | X | X 
 -----------
  7 | 8 | O 

---------------------------------------------------------

[First User]
Enter your desired position in whole number (1-9): 2

Output:
  X | X | O 
 -----------
  O | X | X 
 -----------
  7 | 8 | O 

---------------------------------------------------------

[Second User]
Enter your desired position in whole number (1-9): 8

Output:
  X | X | O 
 -----------
  O | X | X 
 -----------
  7 | O | O 

---------------------------------------------------------

[First User]
Enter your desired position in whole number (1-9): 7

Output:
  X | X | O 
 -----------
  O | X | X 
 -----------
  X | O | O 

# Draw condition met
Match Draw!
---------------------------------------------------------

# Win conditions
(W1)
Output:
  X | X | X 
 -----------
  O | O | 6 
 -----------
  X | O | O 

(W2)
Output:
  O | X | X 
 -----------
  O | O | O 
 -----------
  X | X | 9 

(W3)
Output:
  O | X | X 
 -----------
  4 | O | O 
 -----------
  X | X | X

(W4)
Output:
  O | X | X 
 -----------
  O | O | 6 
 -----------
  O | X | X

(W5)
Output:
  O | X | X 
 -----------
  O | X | O 
 -----------
  X | X | 9 

(W6)
Output:
  X | X | O 
 -----------
  4 | O | O 
 -----------
  X | X | O 

(W7)
Output:
  O | X | X 
 -----------
  O | O | O 
 -----------
  7 | X | O

(W8)
Output:
  O | 2 | X 
 -----------
  O | X | O 
 -----------
  X | X | O

```




