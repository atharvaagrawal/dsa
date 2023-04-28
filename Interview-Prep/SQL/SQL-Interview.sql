use test;

select * from EMP;

-- --->1. Display all the information of the emp table.
 Select * from emp ;
  
-- ---> 2. Display unique jobs from EMP table.
 SELECT DISTINCT Job FROM EMP GROUP BY Job ;

-- --->3. List the details of the emps in asc order of their salaries.
  
SELECT * FROM EMP ORDER BY Sal ASC ;

-- ->4.List the details of the emps in asc order of the  Deptnos and desc of Jobs.

SELECT * FROM EMP ORDER BY Deptno ASC, Job DESC ;

-- ->5.Display all the unique job groups in the descending order

SELECT  DISTINCT JOB FROM EMP ORDER BY JOB DESC;

-- ->6. Display all the details of all  NET

SELECT  * FROM EMP WHERE JOB='.NET';

-- ->7. List the emps who joined before 2015.

SELECT * FROM EMP WHERE JOINDATE < '2015';

-- -> 8. List the Empno, Ename, Sal, Daily Sal of all Employees in the ASC order of AnnSal.

SELECT EMPNO,ENAME,SAL,SAL/30 FROM EMP ORDER BY SAL*12 ASC;

-- ->9.Display the empno , ename, job, hiredate,exp of all Java

SELECT EMPNO,ENAME,ENAME,JOB,JOINDATE  FROM EMP WHERE JOB='JAVA';

-- ->10. List the empno, ename, sal, exp of all emps working for DEPT 10.

SELECT EMPNO,ENAME,SAL FROM EMP WHERE DEPTNO=10;


-- ->11. Display the details of the emps whose Comm Is more than their sal.

-- ALTER TABLE EMP ADD COMMMONEY;

UPDATE EMP SET ENAME='ANT';
SELECT * FROM EMP;

-- -> 12.List the emps in the asc order of Designations

SELECT * FROM EMP ORDER BY JOB;

-- ->13.List the emps along with their exp and daily sal is more than Rs.1500

SELECT * FROM EMP WHERE SAL/30 > 1500

-- ->14. List the emps who are either OF DEPT ‘SAP’ or ‘PA’ in the desc order

SELECT * FROM EMP WHERE DEPT='SAP' OR DEPT='PA' ORDER BY DEPT DESC

--->15.List the emps who joined on 2012-05-12
--- 2018-02-01 in asc order of seniority.

SELECT * FROM EMP WHERE JOINDATE='2012-05-12' OR JOINDATE='2018-02-01'  ORDER BY JOINDATE


--->16. List the emps who are working for the deptno 10 or 20

SELECT * FROM EMP WHERE DEPTNO=10 AND DEPTNO=20

--->17. List the emps who are joined in the year 1981

SELECT * FROM EMP WHERE YEAR(JOINDATE)=2015

--->18. List the emps who are joined in the month of Aug 1980

SELECT * FROM EMP WHERE YEAR(JOINDATE)=2015 AND MONTH(JOINDATE)=2

--->019.List the emps whose annul sal ranging from 220000 and 450000

SELECT * FROM EMP WHERE SAL*12 BETWEEN 220000 AND 450000

--->20. List the emps those are having five characters in their names.

SELECT * FROM EMP WHERE ENAME LIKE '____'

--->21. List the enames those are starting with ‘s’
--> and with fiVe characters

SELECT * FROM EMP WHERE ENAME LIKE 'T%'

UPDATE EMP SET ENAME =LOWER(ENAME)

--->22. List the emps those are having four chars and
--- third char must be ‘r’

SELECT * FROM EMP WHERE ENAME LIKE '__B%'

--->23. List the 5 character names starting with ‘s’
---and ending with ‘h’

SELECT * FROM EMP WHERE ENAME LIKE 'A%H'

---24. List the emps who joined in January

SELECT *,DATENAME(YEAR,JOINDATE) FROM EMP


---25. List the emps who joined in the month of which
--- second character is ‘a’

SELECT *,DATENAME(MONTH,JOINDATE) FROM EMP WHERE DATENAME(MONTH,JOINDATE)='f%'

---26. List the emps whose sal is 4 digit number ending with zero

SELECT * FROM EMP WHERE (SAL BETWEEN 1000 AND 9990) AND SAL%10=2

---27.List the emps whose names having a character set ‘ll’ together

 SELECT * FROM EMP WHERE ENAME LIKE '%BB%'

---28.List the emps those who joined in 80’s

 SELECT * FROM EMP WHERE YEAR(JOINDATE) BETWEEN '2001' AND '2010'

 
---29.List the emps who does not belong to deptno 20

 SELECT * FROM EMP WHERE DEPTNO != 20

 
---30. List all the emps except ‘SAP’ & ‘HR’ in asc
--- order of salaries

  SELECT * FROM EMP WHERE DEPT!='SAP' AND DEPT!='HR'

---31. List the emps who joined in before or after 1981

  SELECT * FROM  EMP WHERE YEAR(JOINDATE) != 2015

---32. List the emps whose empno not starting with digit 78

  SELECT * FROM EMP WHERE CAST(EMPNO AS CHARACTER) LIKE '101'
---33. List the emps who are working under ‘Mgr’

SELECT JOB,SUM(SAL),COUNT(JOB) FROM EMP GROUP BY JOB

SELECT JOB,COUNT(JOB),SUM(SAL) FROM EMP GROUP BY CUBE(JOB)


SELECT SUM(SAL),EXTRACT(MONTH FROM HIREDATE) FROM EMP GROUP BY EXTRACT(MONTH FROM HIREDATE) ORDER BY EXTRACT(MONTH FROM HIREDATE) ASC


select extract(month from [field_name])

SELECT MGR IN
(SELECT EMPNO FROM EMP WHERE JOB='MANAGER')  ;

---034. List the emps who joined in any year but not
---belongs to the month of March

SELECT * FROM EMP WHERE HIREDATE NOT LIKE '%4%'

  
---35. List all the clerks of deptno 20.

SELECT * FROM EMP WHERE DEPTNO=20 AND JOB='CLERK'
  
---36. List the emps of deptno 30 or10 joined in the year 1981
             
SELECT * FROM EMP WHERE (DEPTNO IN(30,10)) AND (EXTRACT(YEAR FROM HIREDATE) = 1981)

       
--->37. Display the details of ‘Smith’

SELECT * FROM EMP,DEPT WHERE ENAME='SMITH' AND EMP.DEPTNO=DEPT.DEPTNO
  
--->38. Display the location of ‘Smith’

SELECT LOC FROM EMP,DEPT WHERE ENAME='SMITH' AND EMP.DEPTNO=DEPT.DEPTNO


--->39. List the total information of emp table along with dname
--->and loc of all the emps working under ‘Accounting’ & ‘Research’ in the asc deptno


SELECT EMP.*,DNAME,LOC FROM EMP,DEPT WHERE (DNAME='ACCOUNTING' OR DNAME='RESEARCH') AND EMP.DEPTNO=DEPT.DEPTNO ORDER BY EMP.DEPTNO ASC


--->40. List the empno, ename, sal, dname of all
--->the ‘Mgrs’ and ‘Analyst’ working in NEWYORK, DALLAS with an
---> exp more than 7 years without receiving the Comma Asc order of Loc.

SELECT EMPNO,ENAME,SAL,DNAME FROM EMP,DEPT  WHERE (LOC IN('NEWYORK', 'DALLAS')) AND DEPT.DEPTNO=EMP.DEPTNO AND  MONTHS_BETWEEN(SYSDATE,HIREDATE)/12 > 20  ORDER BY LOC ASC

--->41. List the empno, ename, sal, dname, loc, deptno,
--->job of all emps working at CHICAGO or working for
--->ACCOUNTING dept wit ann sal > 28000, but the sal
--->should not be = 3000 or 2800 who doesn’t belongs
--->to the Mgr and whose no is having a digit ‘7’ or ‘8’
--->in 3rd position in the asc order of deptno and desc order of job.

  
SELECT EMPNO,ENAME,SAL,DNAME,LOC,EMP.DEPTNO,JOB FROM EMP,DEPT WHERE LOC='CHICAGO' AND DNAME='ACCOUNTING' AND  SAL*12 > 28000 AND ( SAL != 3000 OR SAL != 2800) AND EMP.DEPTNO=DEPT.DEPTNO AND ( MGR NOT LIKE '__7%' OR  MGR NOT LIKE '__8%') ORDER BY EMP.DEPTNO ASC ,JOB DESC;




  --->42. Display the total information of  the emps along with grades in the asc order

SELECT EMP.*,GRADE FROM EMP,SALGRADE WHERE EMP.SAL BETWEEN LOSAL AND HISAL
  
---> 43. List all the grade2 and grade 3 emps

SELECT EMP.* FROM EMP,SALGRADE WHERE GRADE IN(3,2) AND SAL BETWEEN LOSAL AND HISAL
   
--->44. Display all grade 1,2 Analyst and Mgr

SELECT EMP.*,GRADE FROM EMP,SALGRADE WHERE (JOB IN ('ANALYST','MANAGER') ) AND (SAL BETWEEN LOSAL AND HISAL) AND GRADE IN (1,2)   
   
--->45. List the empno, ename, sal, dname, grade, exp, ann
--->sal of emps working for dept 20 or 10.

SELECT EMPNO,ENAME,SAL,DNAME,GRADE,MONTHS_BETWEEN(SYSDATE,HIREDATE)/12 EXP ,SAL*12 ANUAL_SAL  FROM EMP,DEPT,SALGRADE WHERE (EMP.DEPTNO IN (10,20)) AND EMP.DEPTNO=DEPT.DEPTNO  AND SAL BETWEEN LOSAL AND HISAL


--->46. List all the information of emps with loc and
---the grade of all the emps belong to the grade ranges
---> from 2 to 3 working at the dept those are not starting
---> with char set ‘OP’ and not ending with ‘S’ with the
---> design having a char ‘a’ any where joined in the year
---> 81 but not in the month of Mar or Sep and sal not end
---> with ‘00’ in the asc order of grades.

SELECT EMP.*,LOC,GRADE FROM EMP,SALGRADE,DEPT WHERE (GRADE IN(2,3) ) AND SAL BETWEEN LOSAL AND HISAL AND DNAME NOT LIKE 'OP%' AND DNAME NOT LIKE '%S' AND JOB LIKE '%A%' AND EXTRACT(YEAR FROM HIREDATE)=1981
AND ( EXTRACT(MONTH FROM HIREDATE) NOT LIKE '%MAR%' OR   EXTRACT(MONTH FROM HIREDATE) NOT LIKE '%SEP%') AND SAL NOT LIKE '' AND EMP.DEPTNO=DEPT.DEPTNO ORDER BY GRADE ASC

--->47. List the details of the depts along with empno, ename or without the emps

SELECT DEPT.*,EMPNO,ENAME FROM EMP,DEPT WHERE DEPT.DEPTNO=EMP.DEPTNO
  
--->48. List the details of the emps whose salaries more than the employee BLAKE

 SELECT * FROM EMP WHERE SAL>(SELECT SAL FROM EMP WHERE ENAME='BLAKE')

--->49. List the details of the emps whose job is same as ALLEN.

SELECT * FROM EMP WHERE JOB=(SELECT JOB FROM EMP WHERE ENAME='ALLEN')

--->50. List the emps who are senior to King

SELECT * FROM EMP WHERE HIREDATE < (SELECT HIREDATE FROM EMP WHERE ENAME='KING')