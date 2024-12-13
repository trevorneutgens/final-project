#Not Sure if you want to use these data fields but they were the first things that came to mind for me.


import sqlite3

conn = sqlite3.connect('Students.db')
cur = conn.cursor()
cur.execute('create table students (StudentID integer primary key not null, Name text, StudentAge integer, AcademicMajor text,'
            'GPA integer, YearsOfSchooling integer, ClassLevel text, ')
