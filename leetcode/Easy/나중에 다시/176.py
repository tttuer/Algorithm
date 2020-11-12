'''
2번째로 높은 값을 찾는 문제
ifnull안에 쿼리를 작성하여 값이 없으면 null을 출력하게 해야한다.
또한 중복값을 포함하지 않도록 distinct를 써준다.
'''

# Write your MySQL query statement below
select ifnull((select distinct salary from Employee order by salary desc limit 1,1),null) as SecondHighestSalary 