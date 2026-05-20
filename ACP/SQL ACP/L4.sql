CREATE TABLE hacker_news (
    news_id INT PRIMARY KEY,
    user_name VARCHAR(50),
    title VARCHAR(255),
    read_count INT
);

INSERT INTO hacker_news (news_id, user_name, title, read_count)
VALUES
(1, 'Karan', 'AI is the Future', 120),
(2, 'Karan', 'Top Programming Languages', 95),
(3, 'Karan', 'Cybersecurity Trends', 150),
(4, 'Rahul', 'SpaceX Launch Update', 80);

SELECT 
    COUNT(*) AS total_news,
    MAX(read_count) AS highest_reads,
    MIN(read_count) AS lowest_reads,
    AVG(read_count) AS average_reads,
    SUM(read_count) AS total_reads
FROM hacker_news
WHERE user_name = 'Karan';