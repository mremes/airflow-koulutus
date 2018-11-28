SELECT
  SHA256(CONCAT(author.name, author.email)) uid,
  author.name name,
  COUNT(1) num_commits
FROM
  `bigquery-public-data.github_repos.commits`
WHERE
  CAST(author.date AS DATE) = "{{ ds }}"
GROUP BY
  uid,
  name
ORDER BY
  num_commits DESC