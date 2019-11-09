# Resident Assistants' matching with the job of their choice using gale shapley algorithm!
This project focuses on finding the stable matching for two asymmetric arrays which in this case are the group of students 
applying for the Resident Assistant jobs and the number of Resdient Assistant jobs. Here every Resident Assistant Jobs has 
a floor assigned to it. For example Resident Assistant Job1 is for FLoor1.

Every candidate has their preference for every job and the employer has a preference for every candidate attached to every job as shown 
below.

Job | #1 | #2 | #3 | #4 | 
--- | --- | --- | --- |--- |
Job1 | J | E | S | M | 
Job2 | M | J | S | E | 
Job3 | J | M | E | S | 
Job4 | J | M | E | S | 
NoJob | M | S | J | E | 

CANDIDATES | #1 | #2 | #3 | #4 | #5|
--- | --- | --- | --- |--- |--- |
J | Job2 | Job1 | Job3 | Job4 | No Job
E | Job1 | Job2| Job4 | Job3 | No Job
S | Job3| Job1 | Job2 | Job4 | No Job
M | Job4 | Job3 | Job2 | Job1 | No Job

After obtaining the optimal matching, sensitivity analysis has also been performed to check the optimal matching on different preference orders. Different preference orders had been obtained by iterating the first element through the last element by swiping the first element with the next position and moving it towards the last. Here element is a Job or a candidate in a preference order. Total number of preference order combination obtained were 121,500,000. Number of different matchings obtained for all the different preference order combinations are 58.

Code can be modified to perform different analysis.
