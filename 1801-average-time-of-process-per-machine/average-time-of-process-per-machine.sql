select a.machine_id, 
                   round (((select SUM(timestamp)
                       from Activity
                       where activity_type="end" and machine_id = a.machine_id )
                    - (select SUM(timestamp)
                       from Activity
                       where activity_type="start" and machine_id = a.machine_id )
                    )
                    /
                    (select count(timestamp)
                       from Activity
                       where activity_type="start" and machine_id = a.machine_id )
                 ,3  )
                as processing_time
from Activity a 
group by machine_id