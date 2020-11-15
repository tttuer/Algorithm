'''
중복된 값을 지우는 문제
'''

# Write your MySQL query statement below
delete a from person a join person b
where a.id > b.id and a.email = b.email