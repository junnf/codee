# codee

######web framework
########Flask
########Tornado

#########sql健忘
select a.username, b.* from user a Inner Join text b ON a.userid = b.userid;

EXTRACT

ROLLUP

####where语句不能放聚集函数
SELECT product_cd, SUM(a) x from account where status = 'ACTIVE' GROUP BY product_cd HAVING SUM(a) >= 100;

###子查询， 连接， 事务， 视图， 元数据

#####子查询
避免子查询 NOT IN (x,y,NULL)情况， 产生未知结果

=any 与 in等效

关联子查询，非关联子查询
