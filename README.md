# Resident Assistant matching with the floor of their choice
This project focuses on finding the stable matching for two asymmetric arrays which in this case are the group of students 
applying for the Resident Assistant jobs and the number of Resdient Assistant jobs. Here every Resident Assistant Jobs has 
a floor assigned to it. For example Resident Assistant JOB 1 is for FLoor 1.

Every candidate has their preference for every job and the employer has a preference for every candidate attached to every job as shown 
below.

#Employers preference for every candidate
Job1	J	E	T	S	M	R
Job2	J	E	S	T	M	R
Job3	M	J	S	E	T	R
Job4  S	M	J	E	T	R
NoJob	R	T	S	M	E	J

#Candidates' preference for every Job
J	Job1 Job2 Job4 Job3 Nojob
E	Job2 Job1 job3 Job4 Nojob
S	Job2 Job3 Job4 Job1 Nojob
M	Job4 Job2 Job3 Job1 Nojob

