-- 물고기 종류 별 잡은 수 구하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/293257

SELECT COUNT(*) AS FISH_COUNT, N.FISH_NAME
FROM FISH_INFO I
JOIN FISH_NAME_INFO N
    ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY N.FISH_NAME
ORDER BY 1 DESC