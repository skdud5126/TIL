-- 데이터 조회 : 테이블 "songs"에서 모든 음악 데이터를 조회하는 SQL 문장을 작성하시오.

SELECT
  *
FROM
  songs;

-- 데이터 정렬 : 테이블 "songs"에서 음악의 제목(title)을 기준으로 내림차순으로 정렬하는 SQL문장을 작성하시오.

SELECT
  *
FROM
  songs
ORDER BY
  title DESC;

-- 데이터 필터링 : 테이블 "Songs"에서 특정 장르(genre)의 음악만 조회하는 SQL문장을 작성하시오.

SELECT 
  *
FROM
  songs
WHERE
  genre = 'Pop';

-- 조건부 조회: 테이블 "Songs"에서 플레이 시간이 3분 이상인 음악 데이터를 조회하는 SQL문장을 작성하시오.

SELECT
  *
FROM songs
WHERE
  duration >= 180;