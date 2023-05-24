test3_db.html  
展示ai识别的图片，已聚类的结果也展示，已标注的图片不展示  
包括聚类、标注、查询功能

test3_db_julei  
展示聚类结果，已标注的图片不展示  

mysql语句：  
查询日期最大最小值：
    select max(img_time),min(img_time),name_face from img_no_id 
    where substring(img_time,6,5)='04-01' and name_face='周富强';

