-- Script to display the average temparature ordered bt temparature
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM temperatures
GROUP BY `city`
ORDER BY `avg_temp` DESC;
