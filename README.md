# Hadoop_assignment

Question:

Consider, you have a text document as input. Count the number of times a word
occurs in the document. Develop a MapReduce framework based on Python
threads. The data will be read from a file, stored in-memory and will run on a
single computer.
You need to simulate MapReduce using the Python programming language. Use
the required libraries to solve the problem. Other than map and reduce, in
practice there need to exist other components, for example the results from a
map need to be shuffled before being sent to reduce processes: if the two
instances of the word ‘Apple’ were sent to distinct reduce processes, the count
would not be correct. Word counting could be implemented with a map function
that would emit an entry for every word found with a count of 1, and a reduce
function would sum all the map entries for the same word.
Let’s see this in action with a typical example of a MapReduce application: word
counting.

![Screenshot 2023-04-25 130715](https://user-images.githubusercontent.com/95910633/234207240-20a47392-1c00-4339-a578-988d06fcc271.png)

Obtained Output:

![Screenshot 2023-04-25 123252](https://user-images.githubusercontent.com/95910633/234207563-36fc3c88-01d0-4a9d-9e54-0aa609ca1530.png)

![Screenshot 2023-04-25 124158](https://user-images.githubusercontent.com/95910633/234207600-e95c38b0-a86f-440e-9d6c-4fb241146dc9.png)

![Screenshot 2023-04-25 124247](https://user-images.githubusercontent.com/95910633/234207628-6ef2658b-b621-4b73-b3db-e5de282e9c19.png)
