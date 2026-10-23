-- 코드를 입력하세요
# 같은 아이스크림에 대하여 서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우가 있습니다.
# 같은 맛의 아이스크림이라도 다른 출하 번호를 가짐  
# 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛 limit3  F.FLAVOR
# 7월 주문을 맛별로 합친 후에 join
SELECT F.FLAVOR
FROM FIRST_HALF F
INNER JOIN (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS JULY_ORDER
    FROM JULY
    GROUP BY FLAVOR  
) J
ON F.FLAVOR = J.FLAVOR
GROUP BY F.FLAVOR
ORDER BY F.TOTAL_ORDER + J.JULY_ORDER DESC
LIMIT 3


