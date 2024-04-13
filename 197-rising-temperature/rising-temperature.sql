SELECT w.id
FROM Weather w, Weather we
WHERE w.recordDate = we.recordDate + INTERVAL 1 DAY
AND w.temperature > we.temperature



