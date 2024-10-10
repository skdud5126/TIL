
CREATE TABLE articles(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content TEXT NOT NULL,
  created_at DATE NOT NULL
);


-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table
INSERT INTO articles (title, content, created_at) 
VALUES('제목1', '내용1', '2000-01-01');

INSERT INTO articles (title, content, created_at)
VALUES
  ('제목2', '내용2', '2001-01-01'),
  ('제목3', '내용3',' 2002-01-01'),
  ('제목4', '내용4', '2003-01-01');

INSERT INTO articles VALUES (5, '제목5', '내용5', '2004-01-01');
-- 2. Update data in table
-- django에서 어떤 데이터를 수정하려고 한다면?
-- 기본 준비단계 : 수정 대상을 찾아내기.

UPDATE
  articles
-- 어떤 컬럼에 어떤 DATA를 SET 할 거야
SET 
  title = 'update title'
WHERE
  id = 1;

UPDATE articles
SET
  title = 'UPDATE TITLE',
  content = 'UPDATE CONTENT'
WHERE
  id= 2;

-- 3. Delete data from table

DELETE FROM articles
WHERE id = 1;

DELETE FROM articles
WHERE
  id IN(
    SELECT id FROM articles
    ORDER BY created_at
    LIMIT 2
  );

