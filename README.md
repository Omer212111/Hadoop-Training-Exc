# Hadoop-Training-Exc
Exercise 1 
Q1. How many files are there? 
6 
Q2. Did number of mapper change? 
no it was 6 in both runs
Q3. Did number of reducer changed? 
yes from 3 to 6
Q4. Did number of output files change? Why? 
yes from 3 to 6 because each reducer creats one output file 
Q5. What does the value of 'Merged Map outputs' represents and how is it calculated? 
the Merged Map outputs represnts the total number of intermediate map output the hadoop needs to merge before sending it to the reducer. and it is calculated the following way:
num of intermediate map output = input size \ block size
Exercise 2 
Q1. Is your change in the mapper or in the reducer? 
the code needs to be changed only at the mapper because the mapper is the one responsible to the mechanics of tokenize the words
Q2. Please submit your code in GitHub 
______________________________ 
Exercise 3 
Q1. Is your change in the mapper or in the reducer?
the change will only be at the reducer because he is the ine responsible for creating the output files and in this assigment the change is only about which words to present.
Q2. Please submit your code in GitHub 
______________________________
the codes will be submitted in diffrent commits.
