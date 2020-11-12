'''
매니저보다 많이 버는 직원을 찾는 문제
join을 써서 해결할 수 있다.
'''

# Write your MySQL query statement below
select a.Name as Employee
from Employee as a join employee as b
where a.salary > b.salary
and a.managerid = b.id