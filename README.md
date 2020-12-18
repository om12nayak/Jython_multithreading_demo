# Jython_multithreading_demo

Requirements:
-	You should have JDK 7 or above, from (https://www.oracle.com/in/java/technologies/javase-downloads.html)
-	You should install the recent Jython version, from (https://www.jython.org/installation.html)

To run:
-       You can go to the bin folder where jython is installed, for e.g., C:\xx_y\jython2.7.2\bin and run the following (or you can just add in env variables)
        ```jython jython_threading_example.py```

Note:
-	When you run with Jython , the python threading module also gives the same result, as Jython converts python threading module to Java thread.
-	However I have used Java thread and commented the python thread module.

Test results for the code:
-	Using Python interpreter with Python threading module – 61 secs
-	Using Jython interpreter with Python threading module – 6 secs
-	Using Jython interpreter with Java thread module – 6 secs (Recommended but sometimes developers use the 2nd one just to use some system defined python threading methods like join, etc)

For learning more about Jython please visit https://jython.readthedocs.io/en/latest/
