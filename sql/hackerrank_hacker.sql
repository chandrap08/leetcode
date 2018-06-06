select
   s.hacker_id as hacker_id,
   h.name as name
    from submissions s
    inner join challenges c
          on s.challenge_id = c.challenge_id
    inner join difficulty d
          on d.difficulty_level = c.difficulty_level
    inner join hackers h
          on h.hacker_id = s.hacker_id
    where s.score = d.score
group by s.hacker_id, name
  having count(s.hacker_id) > 1
order by count(s.hacker_id) desc, s.hacker_id