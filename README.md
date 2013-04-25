pyCocomo
========

**Simple COCOMO II Analysis function in Python**

## Usage ##

Simply use the function "cocomo" to perform analysis.

## More info on COCOMO II ##

Read the wikipedia article available [here](http://en.wikipedia.org/wiki/COCOMO)

## Example ##

Please see the following example of very simple analysis of an organic project with 2000 LOC:

       import cocomo
       cocomo.cocomo(2000, 'O', 1)

*Note: The 'O' and 1 could be emitted as they are the defaults but were inserted for completeness*
