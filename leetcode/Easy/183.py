'''
구매를 안한 고객을 찾는 문제
not in을 이용하여 문제를 풀 수 있다.
'''

# Write your MySQL query statement below
select name as Customers
from customers 
where id not in (select customerid from orders)