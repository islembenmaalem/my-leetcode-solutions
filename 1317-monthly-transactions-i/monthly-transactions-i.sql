select substring(trans_date,1,7)as month,
       country,
       count(*) as trans_count ,
       count(case when  state="approved" then "approved"  end )as approved_count,
       Sum(amount) as trans_total_amount ,
        SUM(case when state='approved' then  amount else 0 END ) as approved_total_amount 
from Transactions 
group by month ,country 