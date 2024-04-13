select aaa.user_id , CASE 
                     when nombre_of_confirmation is null then 0
                     else round(nombre_of_confirmation/nombre_of_confirmati ,2)
                      END as confirmation_rate
from 
(select s.user_id,count(*) nombre_of_confirmation
from Confirmations c  
Right join Signups s 
on s.user_id = c.user_id  
where c.action = "confirmed"
group by s.user_id ,c.action ) aa

RIGHT join (select ss.user_id,count(*) nombre_of_confirmati
from Confirmations cc  
Right join Signups ss 
on ss.user_id = cc.user_id  
group by ss.user_id  ) aaa

on aaa.user_id = aa.user_id  


