select c.contest_id cid, c.hacker_id hid, c.name name, sum(ss.ts) s1,sum(ss.tas) s2,sum(vv.tv) s3, sum(vv.tuv) s4
    from contests c
    inner join
        colleges co on c.contest_id = co.contest_id
    inner join
        challenges ch on co.college_id = ch.college_id
    left join
        (select v.challenge_id cid, sum(v.total_views)tv, sum(v.total_unique_views)tuv from view_stats v group by cid)vv
          on vv.cid = ch.challenge_id
    left join
        (select s.challenge_id cid,sum(s.total_submissions)ts, sum(s.total_accepted_submissions)tas from submission_stats s group by cid)ss
          on ch.challenge_id = ss.cid
    group by c.contest_id, c.hacker_id, c.name
    having s1 > 0 or s2 > 0 or s3 > 0 or s4 > 0
order by cid