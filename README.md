# Python Budget Calculator 

## Example output
```
python3 main.py
*************Food*************
Initial deposit        1000.00
Groceries               -10.15
Restaurant and so on    -15.89
Transfer to Clothing    -50.00
Total: 923.96

***********Clothing***********
Transfer from Food       50.00
Flea market             -25.55
Total: 24.45

*************Fun**************
Initial deposit         100.00
Berghain                -35.00
Total: 65

Percentage spent by category
100|
 90|
 80|
 70|
 60|
 50| o
 40| o
 30| o
 20| o     o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  F
     o  l  u
     o  o  n
     d  t
        h
        i
        n
        g
```

## User input

The idea is that the user can run the expense tracker from the command line by reading their CSV file containing the budget data. Here's an example of what the CSV file structure could look like:

```
Category,Amount,Type,Description
Food,1000,DEP,initial deposit
Food,10.15,WDRW,groceries
Food,15.89,WDRW,restaurant and more foo
Food,50,TR,Transfer to Clothing

```

## Formatting 

|Category|Type|Amount|Description|
| --------- |:-------------:| ------------- |-------------|
Food|DEP|1000|Initial deposit
Food|WDRW|10.15|Groceries
Food|WDRW|15.89|Restaurant
Food|TR|50|Clothing
Clothing|DEP|500|Initial deposit
Clothing|WDRW|25|Shoes
Health|DEP|200|Initial deposit
Fun|DEP|1000|Initial deposit
Fun|WDRW|50|Berghain
Fun|WDRW|120|Opera
Food|WDRW|85|Coffee and cakes 
Health|WDRW|60|Urban Sport
Health|WDRW|10|Medicine
Health|WDRW|40|Supplements

Note:
 
 1. Your header must look like this:

 |Category|Type|Amount|Description|
 | --------- |:-------------:| ------------- |-------------|

 2. You must only use folloving types:
  - DEP = deposite
  - WDRW = withdraw
  - TR = transfer(to other category)
  
 3. If you use TR, the description should be the name of the category to which you transfer the amount:
 
 Food|TR|50|Clothing
 | --------- |:-------------:| ------------- |-------------|
