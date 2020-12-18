# Jython_multithreading_demo

Requirements:
-	You should have JDK 7 or above
-	You should install the recent Jython version

To run:
        `jython jython_threading_example.py`

Note:
-	When you run with Jython , the python threading module also gives the same result as Jython converts python threading module to Java thread.
-	However I have used Java thread and commented the python thread module.

Test results:
-	Using Python interpreter with Python threading module – 61 secs
-	Using Jython interpreter with Python threading module – 6 secs
-	Using Jython interpreter with Java thread module – 6 secs (Recommended but sometimes developers use the 2nd one just to use some system defined python threading methods like join, etc)
