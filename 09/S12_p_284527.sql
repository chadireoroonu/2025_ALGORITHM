-- 조건에 맞는 사원 정보 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/284527

SELECT SUM(g.SCORE) AS SCORE, g.EMP_NO, e.EMP_NAME, e.POSITION, e.EMAIL
FROM HR_GRADE g
LEFT JOIN HR_EMPLOYEES e ON g.EMP_NO = e.EMP_NO
GROUP BY EMP_NO
ORDER BY SCORE DESC
LIMIT 1