select e1.name
from Employee e1
Join (SELECT e.managerId, number
FROM Employee e
Join (select ee.id as id,count(ee.managerId) as number,ee.managerId,ee.name
       from Employee ee
       group by ee.managerId
       ) eee
on e.id =eee.id
where number>=5) e2
on e1.id = e2.managerId
