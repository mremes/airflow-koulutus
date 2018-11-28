SELECT IF(a.c = b.c, true, false) sums_match
FROM
(
SELECT _PARTITIONDATE pt, SUM(num_commits) c
FROM `github.commits`
WHERE _PARTITIONTIME = "{{ ds }}"
group by pt
) a
LEFT JOIN
(
SELECT CAST(author.date AS DATE) pt, COUNT(1) c
FROM `bigquery-public-data.github_repos.commits`
WHERE CAST(author.date AS DATE) = "{{ ds }}"
GROUP BY pt
) b
ON a.pt = b.pt