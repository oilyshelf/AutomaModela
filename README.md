# AutomaModel

![Tests](https://github.com/oilyshelf/AutomaModela/actions/workflows/tests.yml/badge.svg)

## How to install
- You need Python > 3.10
- install dependencies with "pip install -r requierments.txt"
- Put your BPMN Modell and Excelfiles in to one Folder
- in App.py change Path to your Folder destination and the BPMN Model Filename 
- run "python App.py"

# AutomaModela Dokumentation
Full version <a href="https://docs.google.com/document/d/11ZN01-dTEDpHgsVwQmmHDDAJblJ9TS9Ip1c9r6X-nXE/edit?usp=sharing">here</a>

# Term Definitions


## The Process 

The Process is the set of all Elements defined in the bpmn File. The Process can either be ready , on going , done or canceled.


## Token

AutomaModela is traversing the Process with an so called Token , it stores information about his own id , the Dataframe, a priority and the time it was last evoked. Also it keeps track of the route it took through the process.


## Dataframe

The Dataframe is the main Datastore, on the Dataframe all Transformation are performed. The Token starts with an empty Dataframe, which you can imagine like an empty Table. No column, no rows, but it knows what it is. It  behaves the same way like a Table with columns and rows.

look at pandas Dataframe for more information 


## Data Types

These data types will be recognized and stored in the Dataframe. The Dataframe also from default knows more types but these are the ones you can work with trough Automamodela.


### number


#### int


```
regex →(-?\d+) 
whole numbers
```



#### float


```
regex →(-?\d+\.\d+)
real numbers
```



### string


```
regex →("[^"]+") 
Text
```



### None


```
regex →(None)
representation of nothing
```



### bool


```
regex →(True|False)
```



## Argument Types

In addition to the Data Types, there are special types to use in Task and throughout the process. All Data Types are also Argument types 


### attribute


```
regex →(`[^`]+`)
represents a Column Name
```



#### Attribution Map

**attribute=datatype**

**Used in some Task to assign a data type to a specific attribute **


### expr


```
regex →(.+)
An expression consist of Data Types, Attributes and special Expr Function
These Represent a form of Calculation, allowing dynamically values based on the Values in the Dataframe 
```



#### query

a expr focused on a True or False condition to Filter through the Dataframe 


#### flowprio

**regex → #(\d)**

a way to set the Flow Priority for a given Token, mainly used in Gateways.


# Flow Priorities 

What are Flow Priorities, flow Priorities can be set on any sequenceflow in the Process. Its main usage is in Gateways. With a set priority you can decide which path will be taken first.


# Task-functions

These functions inside a BPMN:Task will be recognized and categorized by AutomaModela.

Task functions are written as a Sentence. 

Parameters in the sentence will be marked in curly braces providing a parameter name and data type like so `{name:data type}`. If a parameter can take on different data types it will be denoted with an Pipe like so `{name:int|float}`.

Some functions require a variable length of parameters it will be denoted like followed `[{name:int}]*`.

The parameters need to be separated with a comma. So for the last example a  these two are valid answers:



* `1,2,3`
* `1`

Also Function can have optional “functionality” these will be marked with normal braces, additionally will the parameter provide a default value which will be used if the Sentence is not extended.Also you can use the sheer presence of a sentence as an optional bool. bool’s which are just the sentence will appear as impl_bool_{num of parameter} in the descriptions.


```
Example:
( from the sheet named {sheet_name:string|int = 0})
```


**Note that internally you can imagine the sentence as a regex expr and the parameters are matched by the regexs above. so it needs to match one to one.**


## Load and Save Data


### load data from excel file {file_name:string}( from the sheet {sheet_name:string|int = 0})( and set the index to the column {index:attribute|None = None})


#### Parameter Description:



* file_name (required):string → Name of the Excel File where to load the Data from
* sheet_name (optional): string or int | defaults to 0 → Defines the Name or Index from which Sheet the Data is taken from
* index (optional) string or None | defaults to None → Select a Column to be used as an index, when None creates an range based index


#### Transformation performed: 

Load a Table from the specified sheet and stores its content as an Dataframe inside of the Token


### save data to excel file {file_name:string}( in to the sheet {sheet_name:string = “Sheet1”})( and also keep the index)


#### Parameter Description:



* file_name (required):string → Name of the Excel File where to Save the Dataframe to
* sheet_name (optional): string | defaults to “Sheet1” → Defines the Name of the Sheet where the Data will be saved to 
* impl_bool_3 (optional) bool | defaults to False → Should the index be saved in the ExcelFile ?


#### Transformation performed: 

Save the Dataframe currently stored in the Token to specific Excel File , will override Excel File if present !


## Views

View Functions will permanently Change the Dataframe inside the Token , there are called view in the Sense that you change the perspective of the Data 


### select the rows where {query:query}


#### Parameter Description:



* query:expr → provide an query aka booleanExpression to filter the Data 


#### Transformation performed: 

Dataframe will check the condition/query  for every row only keeping the ones who evaluate to True 

### select the columns named [{column:attribute}]*


#### Parameter Description:



* column → Which Columns should be kept in the Dataframe


#### Transformation performed: 

Dataframe will cut down itself to the columns specified and will change the order accordingly to the order specified in the call

### rename column from {from_col:attribute} to {to_col:attribute}


#### Parameter Description:



* from (required):string or attribute → Define which column to rename
* to (required):string or attribute → Define the new Name for the column


#### Transformation performed: 

Dataframe will simply rename the specified column, will fail if new name is already present



### delete the data( but keep the columns)


#### Parameter Description:



* impl_bool_1: bool (optional) defaults to False: if True will keep the Column Names (for e.g use in a inclusive Gateway to filter Data) 


#### Transformation performed: 

Dataframe will delete all its content


## Updates on the Data Row Based


### add row with the values [{value:dtype}]*

**or**


### add row with the values [{column:attribute}={value:dtype}]*


#### Parameter Description:



* value (required):string|int|float → Defines the value added to the row
* column(optional notation):attribute → Defines the specific attribute to assign the value to


#### Transformation performed: 

Adds a Row to the Dataframe either by using the first notation and matching the values by position (index is not required) or the second method using a dict object to add the row (will not change the Dataframe layout) → either way providing not the right amount of values or wrong data types operation will fail



### delete row with the values [{value:dtype}]*

**or**


### delete row with the values [{column:attribute}={value:dtype}]*


#### Parameter Description:



* value (required):string|int|float → Defines the value present in the row which needs to be deleted 
* attribute(optional notation):attribute → Defines the specific attribute to assign the value to


#### Transformation performed: 

Deletes the Row in the Dataframe where the values match either by using the first notation and matching the values by position (index is not required) or the second method using a dict object to match the row (will not change the Dataframe layout) → either way providing not the right amount of values or wrong data types operation will fail

In short will perform a query with equals so atribbute1 == value1 and … attributeN == valueN and then delete that row 



![alt_text](images/image19.png "image_tooltip")



### change row from [{org_value:dtype}]* to [{new_value:dtype}]*

**or**


### change row from [{column:attribute}={org_value:dtype}]* to [{column:attribute}={new_value:dtype}]*


#### Parameter Description:



* orgValue (required):string|int|float → Defines the value present in the row which needs to be changed
* changeValue (required):string|int|float → Defines the value to change to
* attribute(optional notation):attribute → Defines the specific attribute to assign the value to


#### Transformation performed: 

Changes the Row in the Dataframe where the values match either by using the first notation and matching the values by position (index is not required) or the second method using a dict object to match the row (will not change the Dataframe layout)  to the desired new Values→ either way providing not the right amount of values or wrong data types operation will fail

In short will perform a delete Operation with the orgValues and then an add with the changeValues 



## Updates on the Data Column Based


### add column {column:attribute} with the value {value:expr}


#### Parameter Description:



* column (required):string or attribute → Define name of the new Column
* value (required):string or int or float or attribute or None → Define value to assign to the new Column


#### Transformation performed: 

Dataframe will add a new Column with the value defined , if the value is an expr for each row the expr will be evaluated (look in the background for the expr case) **Note will fail if expr can't be evaluated !!**



### change column {column:attribute} to the value {value:expr}


#### Parameter Description:



* column (required):string or attribute → Define name of the Column to change 
* value (required):string or int or float or attribute or None → Define value to assign to the Column


#### Transformation performed: 

Dataframe will change a  Column with the value defined , if the value is an expr for each row the expr will be evaluated (look in the background for the expr case) **Note will fail if expr can't be evaluated !! **



### set column {column:attribute} to the value {value:expr}

shortcut to write add or change column → if not presents calls add column else change column


### delete column {column:attribute}


#### Parameter Description:



* column (required): attribute → Define name of the Column to delete


#### Transformation performed: 

Dataframe will delete the column with the name column → will not fail if column is not in Dataframe


## Special Functions


### do nothing 

does nothing


### set index to {column:attribute} 


#### Parameter Description:



* column (required):attribute → Define name of the Column to set index to


#### Transformation performed: 

Dataframe set the index to the specified column **Note if using a column as index the column will not be able to be used as an attribute ** 


### reset the index( and keep the old one as a column) 


#### Parameter Description:



* keep:bool (optional ) defaults to False → keep the old index as a column


#### Transformation performed: 

Dataframe set the index back to a range based index if keep than the replaces index will be integrated as a column




## Special Special Functions


### dotOperation special case write → (.{anypandasfunc})

will try to a execute a function which is based on pandas Dataframe Library as so 

Dataframe = Dataframe.dotOperation


# Gateways

Gateways have different types of behavior based one the type (Parallel, Exclusive or Inclusive) and if there is a closing (multiple flows in one out) or an opening (one in multiple out). Gateways are all about deverting the Process into multiple paths and controlling the flow.


## Opening Gateways

Every Opening Gateway Type (Parallel, Exclusive or Inclusive) has its own “Theme” which it follows but it can be customized with some OpeningFunctions. Every type has their own OpeningFunctions fitting their theme.

Ever Type has also a Default Operation, which will be used if you provide no name

The Notions are the same as the Task Functions but with an extra of adding information on what is needed on the outgoing flows.

For Inclusive and Exclusive Gateways there is an option to add a default flow, which will trigger if no other flow is triggered and will simply pass the Token without doing anything to the specified route. **Note you can mark a flow with a parameter as default but when it comes to worse and the default flow is chosen, no transformation or anything accurse. **


### Query Order

by providing an additional priority (see flow priorities) u can decide which flow will be executed first.


### Parallel Gateway (defaults to copy)

The Opening Parallel Gateway is described as “Fork” with the idea to parallelize the Process therefore all routes are always taken. Here the Opening Functions don't need flow names but some are defined for convenience.


#### copy | Flow Parameters:blank

Every outgoing flow will get a copy of the Token.


#### new( and keep)|Flow Parameters:blank or bool

if only “new” provided every outgoing flow will get a brand new token.

when “new and keep” is used you can mark flows with a bool, all marked with True will simply get a copy of current Token. blank flows will default to False

    


### Exclusive Gateway (defaults to check)

Like the name implies this Gateway chooses only one outgoing flow to pursue. All Flows except the Default Flow will need an flow parameter 


#### check( but do not transform) | Flow Parameters:query

In order of the defined flow priorities every flow will be checked if the specified query will result in a non-empty Dataframe. The first one with a non-empty Dataframe will get the taken passed to. The query will also be executed on the Dataframe , except the optional part is specified.


#### is empty |Flow Parameters:bool

check if the Token passed to is empty. The Flow with the value True will get the Token if the Dataframe is empty and the one with False if not.

**Note: only use two flows also a good way to use this Function is to have on normal flow with either True or False and a default flow which will get the Opposite**


### Inclusive Gateway (defaults to splice)

An Inclusive Gateway is fairly similar to the exclusive one, only it will pass down a token to every flow which is determined to be trough “true” will get a Token.


#### splice|Flow Parameter:query

Similar to the check function. Check flow (ordered by flow priority) with the specified query. If the query will result in a non-empty Dataframe pass this flow a copy of the Token with the query performed. Removes Row from the current Token if a copy is created. So if for example the first query was successful the next flow will query on the Dataframe minus the rows which were used from the first. **Note use the expr function @ALL to get the current status of the spliced Dataframe. But it will leave behind an empty Dataframe so use it best as the last flow (highest value in flow priority) to save some time writing queries ;)**

  


#### reset|Flow Parameter:query

Same as spliced but will not remove rows from original Dataframe.


## Closing Gateways


### Exclusive Gateway

Since the Opening variant decides on one Flow the Closing Gateway is more or less a passthrough for the Token ,synchronizing the different paths back to a main one. 


### Inclusive Gateway and Parallel Gateways

In Terms of Functionality these two Gateway work the same but you should remember what the Opening Gateway did to make the best use out of them.

Both will wait for all Tokens to arrive before proceeding further. Incase of Opening Parallel Gateway it's all the flows and for Inclusive Gateways it's all the Flows that had a query with a non-empty result. 

You have to  assign a Combine Operation to the Gateway which will combine all the Tokens back to one.

Both Gateways have a standard combine operation assigned if no one should be chosen.

So the Inclusive Gateway will perform a Concat and the Parallel Gateway will perform a join. 

How will they be executed first the Token with the Highest Priority will be chosen as base or left and then all other tokens represent right and one after the other will be “merged” in to the left one


## Combination-Functions

Combine Function will only be performed if there are a minimum of two Token and the way they work is that a basis Token will be chosen and one by one the other Tokens will be added to it. The basis Token is either based on the Token with the highest Flow priority or will be the one first to arrive. **Note the first to arrive  means in practicality the flow with least residenze aka with the least amount of other elements after the Opening Gateway.**


## Combination-Functions(Focused on Parallel Use Case)


### Join Modifier (%left|right|outer%)

to do al left outer , right outer  or full outer join instead just use left , right or outer in front of the join


### %left|right|outer% join( on index)

basically a natural join, but will go over multiple columns if there will be multiple sets of matching columns(use join on to guarantee the right columns are chosen )  → will fail if no matching sets are found

will perform a join on the “two” indices of the Dataframes, **Note probably don't use it better in generell setting indices, will not be helpful, especially because they don't really act like a key in relational algebra.  → will fail if no matching sets are found → will also fail on the standard provided indices and indices need to share the same name **


### %left|right|outer% join on {column:attribute}

a short version of an equi join with the same name for columns.


### %left|right|outer% join on {left_col:attribute} == {right_col:attribute}

will try to perform an equi join , make sure the columns are present, if both Dataframe have the same column name there is no guarantee for picking the “right” on  

column1 is the one in the Basis Token and column2 the other Token(s).


### join where {query:expr}

basically is a cross operation followed by an filter operation (**note Dataframes will be joined one by one**) simulates a theta join



### cross

same as the cross from relational algebra 


## Combination-Functions(Focused on Inclusive Use Case)


### concat

same as the set operation of Union but keeping the duplicates


### union

same as the set operation of Union 


### intersect

same as the set operation intersect


### difference

same as the set operation symmetric difference  


### subtract

same as the set operation difference, will use the basis Token as the one from which will be subtracted.


# Expr Functions

These are the Components you can use to build besides the other data types to build up an expr. Every dtype can also be replaced with an attribute and the function will be called for every row in the Dataframe 


## Data Comparisons aka booleanExpression


#### a:dtype == b:dtype → equal


#### a:dtype != b:dtype→ not equal


#### a:dtype >= b:dtype → more or equal than


#### a:dtype &lt;= b:dtype → less or equal than


#### a:dtype &lt; b:dtype → less  than


#### a:dtype > b:dtype  → more than 

**Note need to be as the same data type exception being numbers**


## Data Manipulation

The Function will be written down according to the Data Types but providing an attribute this function will be called for every row in the Dataframe **Note if some function has an abbreviation is often times better to call the abbreviation **


### number


#### a:number + b:number →number


#### a:number - b:number → number


#### a:number * b:number → number 


#### a:number / b:number → float


#### a:number **of:int → 

<p id="gdcalert40" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert41">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>




#### @root_of(a:number, base:int = 2)→number (

<p id="gdcalert41" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: equation: use MathJax/LaTeX if your publishing platform supports it. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert42">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>

)


### int


#### a:int // b:int →int (typical coding divide between ints no rest e.g. 3//2 = 1 and not like 3/2 = 1.5)


#### a:int % b:int → int


### float


#### @round_to(a:float, places:int = 2)→float (e.g.  2.123 → 2.12)


#### @floor(a:float)→int (e.g 2.12 →2)


#### @ceil(a:float)→int (e.g 2.12 →3)


### string


#### @concat(a:string, b:string) →string 

**abbreviations but there only work with matching dtypes**


##### a:string + b:string →string


##### a:attribute(string) + b:attribute(string) →attribute(string)


#### @substr(a∶string∣attribute,start∶int,end∶int∣None=None)→string∣attribute (@substr(“abc”, 0,1) → “a”) (if end is None go to the end of the string)


#### @strip(a:string, special_char:str|None = None) → string (@strip(“ a ”) → “a”)


#### @split(a:string,on_what:str, keep_appearance:int = 0 ) → string (@split(“a,b”, “,”) →”a” )


#### @replace(a:string, where:int, with:str) → string (@replace(“aaa”, 1, “b”) → “aba”)


#### @replace_all(a:string,what:int, with:str) → string (@replaceAll(“aba”, “a”, “c”) → “cbc”)


### bool and booleanExpression 


#### (~b) or (**not** b) →bool  


#### (a and b) or (a & b) →bool  


#### (a or b) or (a | b) →bool  


#### (a & ~b) →bool  

**Note no real xor symbol use this hack **


## Data Conversion 


#### @to_string(a:int|float) →string


#### @to_int(a:string*|float) →int ( for floats same as calling floor(a))


#### @to_float(a:int|string*) →float

***Note:string → number only works if the string is a number with the right type **

**e.g @toFloat(“2.2”) → 2.2 ✅ @toInt(“2.2”) →❌**


## Data Reduction


## @get_sum(a:attribute(number)) →number (a = [1,2,3] so @sum(a) → 6)


## @get_prod(a:attribute(number)) →number (a = [2,2,3] so @prod(a) → 12)


## @get_min(a:attribute(number)) →number (a = [1,2,3] so @min(a) → 1)


## @get_max(a:attribute(number)) →number (a = [1,2,3] so @max(a) → 3)


## @get_mean(a:attribute(number)) →number (a = [1,2,3] so @mean(a) → 2)


## Data Evaluation

These Functions will treated as a booleanExpression


#### @is_empty(a:attribute) → return True if value in a is in any way shape or form equal to None (Null, Nan, etc.)


#### @contains(a:string, c_str:string, at:int|None =None) e.g. @contains(“abc”,”a”) →True


#### @starts_with(a:string, c_str:string) e.g. @startswith(“abc”, “ab”) →True 


### Special


#### @ALL → use only in query and as the only word → will return the whole Dataframe unchanged 
