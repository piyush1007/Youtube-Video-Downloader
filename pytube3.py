from pytube import YouTube
video_list=open("videolinks.txt","r")
for i in video_list:
    yt=YouTube(i)
    #print(yt.streams.all())
    down=yt.streams.first()
    print(down)
    down.download("C:/Users/aditya.kumar.sinha/Desktop/Monu")
    print("Downloaded",i)