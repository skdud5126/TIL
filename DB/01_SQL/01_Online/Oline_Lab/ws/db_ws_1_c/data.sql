-- 데이터 그룹화 : 테이블 "songs"에서 음악의 장르(genre)를 기준으로 그룹화하는 SQL 문장을 작성하시오.

SELECT
  genre, COUNT(*) AS 'count'
FROM
  songs
GROUP BY
  genre;

-- 집계 함수 : 테이블 "songs"에서 각 그룹별로 음악의 수를 계산하여 출력하시오.
SELECT
  genre, COUNT(*) AS 'count', AVG(duration) AS 'avg_duration'
FROM
  songs
GROUP BY
  genre;