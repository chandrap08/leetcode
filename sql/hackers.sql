select t.hacker_id, t.name, sum(t.max_score) as total_score
from(
    select h.hacker_id as hacker_id, h.name as name, s.challenge_id, max(s.score) as max_score
    from hackers as h
        inner join submissions as s
        on h.hacker_id = s.hacker_id
        group by h.hacker_id, h.name, s.challenge_id
    )t
group by t.hacker_id, t.name
having total_score > 0
order by total_score desc, t.hacker_id asc

####################
select h.hacker_id, name, sum(score) as total_score
from
hackers as h inner join
/* find max_score*/
(select hacker_id,  max(score) as score from submissions group by challenge_id, hacker_id) max_score

on h.hacker_id=max_score.hacker_id
group by h.hacker_id, name

/* don't accept hackers with total_score=0 */
having total_score > 0

/* finally order as required */
order by total_score desc, h.hacker_id
;