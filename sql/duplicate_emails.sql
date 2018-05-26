# Write your MySQL query statement below

SELECT DISTINCT(Email)
FROM(
SELECT m.Email
  FROM Person as m
  WHERE
   (SELECT COUNT(DISTINCT (Id)) as cnt from Person p WHERE p.Email = m.Email) > 1
)T