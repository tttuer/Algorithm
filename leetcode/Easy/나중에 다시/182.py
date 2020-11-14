'''
중복된 값이 있는 것을 찾는 문제
그룹으로 묶고 같은 값이 2개 이상인 것을 찾는다.
'''

# Write your MySQL query statement below
select email from person group by email having count(email) > 1