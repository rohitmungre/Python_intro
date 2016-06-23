import webbrowser
import time 

num_breaks = 3
break_count = 0

print("Our program started on "+time.ctime())
while break_count < num_breaks:
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=b8I-7Wk_Vbc")
    break_count = break_count +1

print("Our program ended on "+time.ctime())
