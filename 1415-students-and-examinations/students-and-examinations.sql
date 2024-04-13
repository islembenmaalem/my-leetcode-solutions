SELECT distinct st.student_id , student_name, sbj.subject_name,
                          (select count(*)
                                       FROM Examinations e1
                                       WHERE
                                        e.student_id = e1.student_id
                                       AND e.subject_name = e1.subject_name
                                        ) 
                                       as attended_exams         

FROM  Students st
CROSS JOIN  Subjects sbj
LEFT JOIN Examinations e 
ON e.student_id = st.student_id AND e.subject_name = sbj.subject_name
order by student_id ,sbj.subject_name 
