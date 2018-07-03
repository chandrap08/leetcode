# Write your MySQL query statement below


SELECT DISTINCT s1.* from
    stadium s1,
    stadium s2,
    stadium s3
WHERE s1.people >= 100 AND s2.people >= 100 AND s3.people >= 100 AND
(
    (s2.id = s1.id +1 AND s3.id = s2.id + 1 AND s3.id = s1.id + 2)
    #s1,s2,s3
    OR
    (s1.id = s2.id + 1 AND s3.id = s1.id + 1 AND s3.id = s2.id + 2)
    #s2,s1,s3
    OR
    (s3.id = s2.id + 1 AND s1.id = s3.id + 1 AND s1.id = s2.id + 2)
    #s2,s3,s1
)
ORDER BY s1.id
