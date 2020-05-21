from pytube import YouTube
yt=YouTube("https://youtu.be/OGGHKpV01cs")
#print(yt.streams.all())
down=yt.streams.get_by_itag(18)
down.download(r"C:\Users\aditya.kumar.sinha\Desktop\Monu")
print("Downloaded",yt)