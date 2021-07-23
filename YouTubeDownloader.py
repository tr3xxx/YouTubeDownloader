import getpass
import os.path
from pytube import YouTube

username = getpass.getuser()
print("Hallo",username,"\nWillkommen beim tr3xGaming YouTube Downloader.\n")

while True:
    
        Format = input("\nSchreiben sie mp4 um ein YouTube Video herunterzuladen.\nSchreiben sie mp3 um nur die Audio eines YouTube Videos herunterzuladen.\n")

        if Format!="mp3" and Format!="mp4":
            print("Falsche Eingabe")
            break
        
        VideoLink = input("Geben sie nun die URL des Videos ein\n")
        if VideoLink.startswith("https://www.youtube.com/watch?v="):
            yt = YouTube(VideoLink)
            if Format == "mp4":
                ys = yt.streams.get_highest_resolution()
            if Format == "mp3":
                ys = yt.streams.get_audio_only()
                
            print("\nDer Download von: ",yt.title," wurde gestartet...")

            if not os.path.exists("${HOMEDRIVE}${HOMEPATH}\\Desktop\YouTubeDownlaods"):
             os.makedirs("${HOMEDRIVE}${HOMEPATH}\\Desktop\YouTubeDownlaods")
            
            Dpath = os.path.expandvars("${HOMEDRIVE}${HOMEPATH}\\Desktop\YouTubeDownlaods")
            ys.download(Dpath)
            print("\nDer Download ist abgeschlossen, sie finden die Datei unter:",Dpath,"\n")

        else:
            print(VideoLink + " ist KEIN gültiger YouTube Link, bitte versuchen sie es erneut.")

        
        restart = input("Wollen sie ein weiteres Video herunterladen (y/n)\n")
        
        if restart == "n":
            SystemExit
            break
          
        

