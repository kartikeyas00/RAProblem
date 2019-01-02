# Resident Assistants' matching with the job of their choice
This project focuses on finding the stable matching for two asymmetric arrays which in this case are the group of students 
applying for the Resident Assistant jobs and the number of Resdient Assistant jobs. Here every Resident Assistant Jobs has 
a floor assigned to it. For example Resident Assistant JOB 1 is for FLoor 1.

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
J | Job2 | Job1 | Job3 | Job4 | Nojob
E | Job1 | Job2| Job4 | Job3 | Nojob
S | Job3| Job1 | Job2 | Job4 | Nojob
M | Job4 | Job3 | Job2 | Job1 | Nojob
