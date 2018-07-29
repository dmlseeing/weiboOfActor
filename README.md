# **weiboOfActor**  
Get basic information from actors' weibo  
  
## **Main codes**  
  * **actor_name.csv**  
    The list of actors' name  
  * **basic_url.txt**  
    The urls of users' information page
  * **elements_withoutFindingOut.txt**  
    The list of actors' name without weibo  
  * **data1~data5**  
    Datas of actors' weibo which contain three files, _time_weibo.txt, three_types_num.json, basic_infomation.txt_
  * **get_actorWeiboInfo.py**  
    * **get_actorurl()**  
      Get homepage urls of actors' weibo and generate a file named _actor_url.txt_  
    * **get_num_of_follow_fan_weibo()**  
      Get numbers of follows, weibo and fans and generate files named _three_types_num.json_  
    * **slowdown()**  
      Glide function, to achieve dynamic glide and get data  
    * **get_totalinfo_of_firstpage()**    
      Get total original weibo and time of firstpage and generate files named _time_weibo.txt_  
    * **get_basicinfo()**  
      Get relevant information from users' information page and generate files named _basic_infomation.txt_  
    * **get_totalnumof_forward_like()**  
      Get total numbers of forwards and likes of firstpage and generate a file named _totalNumOfForward_Like.txt_  
## **Operating environment**  
Based on **python3.5** and **selenium**, first need to install：  
  1.  selenium  
  2.  webdriver  
  3.  
