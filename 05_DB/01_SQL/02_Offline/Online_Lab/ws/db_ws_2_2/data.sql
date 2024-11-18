SELECT
  *
FROM
  zoo;

-- 1. zoo테이블에 species열을 추가한다. 값은 Text를 받을 수 있어야 한다.
ALTER TABLE zoo
ADD COLUMN species TEXT NOT NULL DEFAULT 'DEFAULT';

UPDATE zoo
SET species = 'Panthera leo'
WHERE 
  name = 'Lion';

-- 2. zoo 테이블에 삽입되어 있는 모든 데이터에 species 값을 추가하여 수정한다.
UPDATE zoo
SET species = 'Loxodont africana'
WHERE 
  name = 'Elephant';

UPDATE zoo
SET species = 'Giraffa camelopardalis'
WHERE 
  name = 'Giraffe';

UPDATE zoo
SET species = 'Cebus capucinus'
WHERE 
  name = 'Monkey';

-- UPDATE zoo
-- SET species = 
--   CASE 
--     WHEN name = 'Elephant' THEN 'Loxodont africana'
--     WHEN name = 'Giraffe' THEN 'Giraffa camelopardalis'
--     WHEN name = 'Monkey' THEN 'Cebus capucinus'
--     -- 필요시 추가
--     ELSE species
--   END;


-- 3. 모든 데이터의 height값을 2.54가 곱해진 값으로 수정한다.

UPDATE zoo
SET height = height*2.54;


-- 4. zoo테이블의 모든 데이터를 조회하여 출력한다.
SELECT
  *
FROM
  zoo;