# Week5 Assignment

## Task 2: Create database and table in your MySQL server
```sql
CREATE TABLE member(
id INT UNSIGNED NOT NULL AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
email VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
follower_count INT UNSIGNED NOT NULL DEFAULT 0,
time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id)
);
```
![task2](task2.png)

## Task 3: SQL CRUD

### Task 3.1
```sql
INSERT INTO member(name, email, password, follower_count) VALUES
('test', 'test@test.com', 'test'),
('charlene', 'charlene@test.com', 'charlene'),
('airy', 'airy@test.com', 'airy'),
('alfie', 'alfie@test.com', 'alfie'),
('tommy', 'tommy@test.com', 'tommy');
```
![task3-1-2](task3-1-2.png)

### Task 3.2
```sql
SELECT id, name, email, password, follower_count, `time` FROM member;
```
![task3-1-2](task3-1-2.png)

### Task 3.3
```sql
SELECT id, name, email, follower_count, `time`
FROM member
ORDER BY `time` DESC;
```
![task3-3](task3-3.png)

### Task 3.4
```sql
SELECT id, name, email, `time`
FROM member
ORDER BY `time` DESC
LIMIT 3 OFFSET 1;
```
![task3-4](task3-4.png)

### Task 3.5
```sql
SELECT id, name, email FROM member
WHERE email = 'test@test.com';
```
![task3-5](task3-5.png)

### Task 3.6
```sql
SELECT id, name, email FROM member
WHERE name LIKE '%es%';
```
![task3-6](task3-6.png)

### Task 3.7
```sql
SELECT id, name, email FROM member
WHERE email = 'test@test.com' AND password = 'test';
```
![task3-8-7](task3-8-7.png)

### Task 3.8
```sql
UPDATE member
SET name = 'test2'
WHERE email = 'test@test.com';
```
![task3-8-7](task3-8-7.png)

## Task 4: SQL Aggregation Functions

### Task 4.1
```sql
SELECT COUNT(*) FROM member;
```
![task4-1](task4-1.png)

### Task 4.2
```sql
SELECT SUM(follower_count) FROM member;
```
![task4-2](task4-2.png)

### Task 4.3
```sql
SELECT AVG(follower_count) FROM member;
```
![task4-3](task4-3.png)

### Task 4.4
```sql
SELECT AVG(follower_count) FROM (
    SELECT follower_count FROM member
    ORDER BY follower_count DESC
    LIMIT 2
) AS top2;
```
![task4-4](task4-4.png)

## Task 5: SQU JOIN

### Task 5.1
```sql
CREATE TABLE message (
id INT UNSIGNED  NOT NULL AUTO_INCREMENT,
member_id  INT UNSIGNED  NOT NULL,
content TEXT NOT NULL,
like_count INT UNSIGNED  NOT NULL DEFAULT 0,
`time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (id),
FOREIGN KEY (member_id) REFERENCES member(id)
);
```
![task5-1](task5-1.png)

```sql
INSERT INTO message (member_id, content, like_count) VALUES
(1, 'Hello, this is test.', 10),
(1, 'Second post from test.', 20),
(2, 'Charlene says hi.', 5),
(4, 'Alfie posting here.', 8);
```

### Task 5.2
```sql
SELECT message.id, member.name, message.content, message.like_count
FROM message
JOIN member ON message.member_id = member.id;
```
![task5-2](task5-2.png)

### Task 5.3
```sql
SELECT message.id, member.name, message.content, message.like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.email = 'test@test.com';
```
![task5-3](task5-3.png)

### Task 5.4
```sql
SELECT AVG(message.like_count)
FROM message
JOIN member ON message.member_id = member.id
WHERE member.email = 'test@test.com';
```
![task5-4](task5-4.png)

### Task 5.5
```sql
SELECT member.email, AVG(message.like_count)
FROM message
JOIN member ON message.member_id = member.id
GROUP BY member.email;
```
![task5-5](task5-5.png)
