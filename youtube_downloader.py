from pytube import YouTube

def DownloadAudio(url_videos):
    #Download audio only
    print("Downloading........... (don't close this windows)")
    MyDownload = YouTube(url_videos).streams.get_audio_only().download()
    print('Finished!')
    return MyDownload

def DownloadVideos(url_videos, MyVideosResolution):
    print("Downloading........... (don't close this windows)")
    MyDownload = YouTube(url_videos).streams.get_by_resolution(MyVideosResolution).download()
    print('Finished')
    return MyDownload

def MainMenu():
    print('Welcome to My Youtube Downloader:')
    UrlVideos = input('Url Videos: ')

    print(f"""
    Download {YouTube(UrlVideos).title}
    [1]. Audio Only
    [2]. Videos
    """)

    MyChoice = int(input('your choice (1/2) ---> '))
    if MyChoice == 1:
        DownloadAudio(UrlVideos)
    elif MyChoice == 2:
        MyResoChoice = input('your resolution videos(720/480/360/240/120): ') + 'p'
        try:
            DownloadVideos(UrlVideos, MyResoChoice)
        except:
            print('ERROR! Change your videos resolution!')
    else:
        print('ERROR!!!')

#url_videos = 'https://www.youtube.com/watch?v=a3ICNMQW7Ok'

MainMenu()