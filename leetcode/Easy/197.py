'''
다음날보다 온도가 높은 id를 찾는 문제
date_add를 이용하면 풀 수 있다.
'''

# Write your MySQL query statement below
select w2.id from weather w1 join weather w2
where date_add(w1.recorddate,interval 1 day) = w2.recorddate and w1.temperature < w2.temperature