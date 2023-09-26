from Django_AutoReloader import Autoreload_Django   
# """
# Enter Reload Time and App url example: reload_time='03:00',app_url='127.0.0.1:8080'
# """
re_run=Autoreload_Django(reload_time="03:00",app_url="127.0.0.1:8080")   
#  """
#                         Once you have used  reload method avoid using keyboard short cut Ctl + s
#                         if you use ctrl + s after using this method your server will stop responding to requests because reload creates anew django main thread killing the 
#                         the previous thread that was running when you first started the djnago server.
# """
re_run.reload()   




