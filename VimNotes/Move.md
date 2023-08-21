## Vim keyStoke

## MovingCursor

### Horizonal



f+{char}: find first char in cur line,using ; to excute again

t+{char}: until f


w : moving word by word with the front forward

b : backward as w

e : same as w but with end

ge : as you might guess

Tips:
WORD are seperated simply on SPACE varied from the detail definition of word , when manioulating the big WORD , just use the UPPPER case of instrucation above.


### More extremel
#### often 
^ : to the first non-blank char
$ : to the end of a line

#### not that ususal
0 : to the first of a line
g_ : to the non blank char  of a line

### Vertical

{  }:move by paragraph

ctrl + D/U : move down/up half a page at a time

/{pattern} : search forward in a file using n to next N to Back

?/{pattern} : Backward

/* : search the word under cursor in file forward.

/#  : Backward


gd: go to the defination of the (fucntion)


gg : go to the top of the file

{line}gg : go to a specific line

G: to the end of the file 

% : jump to the matching ({[]}){match} whrej

{}:  {}