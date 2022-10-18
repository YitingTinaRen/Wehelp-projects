# Week 5 Assignment
## Req 3 results
1. 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
![First data in member DB](/week-5/img/1.png)

2. 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
![All data in memberDB](/week-5/img/2.png)

3. 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
![Order by time](/week-5/img/3.png)

4. 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
![limit data](/week-5/img/4.png)

5. 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
![username is test](/week-5/img/5.png)

6. 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
![username is test and password is test](/week-5/img/6.png)

7. 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
![use update command](/week-5/img/7.png)

## Req 4 results
1. 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
![Total member](/week-5/img/4-1.png)

2. 取得 member 資料表中，所有會員 follower_count 欄位的總和。
![Sum of follower_count](/week-5/img/4-2.png)

3. 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
![Average of follower_count](/week-5/img/4-3.png)

## Req 5 results
![message table](/week-5/img/5-0.png)
1. 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
![all message include member name](/week-5/img/5-1.png)

2. 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
![username is test with message and member name](/week-5/img/5-2.png)

3. 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
![aggregate function included](/week-5/img/5-3.png)
