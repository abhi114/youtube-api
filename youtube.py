#AIzaSyC-qhIU91gzfBEHQPeo9Lkes19CRFFy1A8
from tkinter import *
import urllib.request
import json

key = "AIzaSyC-qhIU91gzfBEHQPeo9Lkes19CRFFy1A8"

def channel_data():
    name = e1.get()
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()

    sub = json.loads(data)['items'][0]["statistics"]["subscriberCount"]
    total_view = json.loads(data)['items'][0]["statistics"]["viewCount"]
    tota_videos = json.loads(data)['items'][0]["statistics"]["videoCount"]
    l2.config(text = sub)
    l4.config(text = total_view)
    l6.config(text = tota_videos)







root = Tk()
root.geometry("500x200")
channel_name = StringVar()
e1 = Entry(root,textvariable =  channel_name)
e1.grid(row=1,column=2)
b1 = Button(root,text="Get",command=channel_data)
b1.grid(row=2,column=2)


#display label

l1 = Label(root,text="total numbers of subscribers :",font = "times 15 bold")
l1.grid(row=4,column=1)
l2 = Label(root,font = "times 15 bold")
l2.grid(row=4,column=3)

l3 = Label(root,text="total numbers of views :",font = "times 15 bold")
l3.grid(row=6,column=1)
l4 = Label(root,font = "times 15 bold")
l4.grid(row=6,column=3)


l5 = Label(root,text="total numbers of videos :",font = "times 15 bold")
l5.grid(row=8,column=1)
l6 = Label(root,font = "times 15 bold")
l6.grid(row=8,column=3)

root.mainloop()

