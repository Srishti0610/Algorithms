__#Name#__

Design and Analysis of Algorithms
String Matching Algorithms

__#Description#__

Implementation of string matching algorithm in python.
Three methods
- Naive Method
- Knuth Morris Pratt Method
- Rabin Karp Method


__#Installation#__

python 3.9 or higher
pip

Alternatively can be run in jupyter notebook


__#Usage#__

There are three seperate python files for the three algorithms
- Naive Method
- Knuth Morris Pratt Method
- Rabin Karp Method
There is one set of sample string and pattern provided in the zip folder
The three files can be run using the following commands on command prompt

``bash``
python <filename>
python naiveStringMatching.py
python RabinKarpStringMatching.py
python KMPStringMatching.py
``

The python file reads the string and pattern files and provides the indexes where the pattern matches. Also the time taken is calculated using the monotonic time function in nanoseconds and is converted to seconds.

The KMP and Rabin Karp programs run effeciently if the dataset is large.
In case of small dataset, the naive performs better and has similar runtime as Rabin Karp. 
KMP is more effecient.

