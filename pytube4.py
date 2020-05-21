from pytube import Playlist
yt=Playlist("https://www.youtube.com/playlist?list=PLsyeobzWxl7r2ukVgTqIQcl-1T0C2mzau")
#print(yt.streams.all())
#down=yt.streams.get_by_itag(18)
yt.download_all(r"C:\Users\aditya.kumar.sinha\Desktop\Monu")
print("Downloaded",yt)