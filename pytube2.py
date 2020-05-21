from pytube import YouTube
video_list=["https://youtu.be/Ps4aVpIESkc","https://youtu.be/ZmcBC9-wAXM"]
for i in video_list:
    yt=YouTube(i)
    #print(yt.streams.all())
    down=yt.streams.get_by_itag(18)
    down.download("C:/Users/aditya.kumar.sinha/Desktop/Monu")
    print("Downloaded",i)