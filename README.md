# TimetablingSolutions-to-SOBS
Converts the Timetabling Solutions output into a format suitable for SOBS

[https://www.timetabler.com/](https://www.timetabling.com.au/)

[https://sobs.com.au/](https://sobs.com.au/)

Input: eMinervaTTable.txt

Output: eMinervaTTable_SOBS.csv

Timetabling Solutions give us this:
1. Period
2. ClassName
3. Room
4. Teacher
5. SDayName
6. FDayName
7. Subject
8. YearLevel

SOBS Expects this:
1. Day_No     : This is day number from the timetable
2. Period     : The period import code
3. RollClass  : The first part of the booking description
4. ClassName  : The second part of the booking description
5. Room       : The room import code
6. Teacher    : The staff member import code
