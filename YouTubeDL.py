from pytube import YouTube
import sys

def filter_name(name):
    name = ''.join(e for e in name if e.isalnum())
    return name + ".mp4"
    

def download_video(link):
    try:
        yt = YouTube(link)
    except:
        print("That is an invalid youtube link.")
        print("Usage: YouTubeDL.py [YouTube link]")
        exit(1)
    else:
        stream = yt.streams.filter(file_extension='mp4', type="video", adaptive="True")[0]
        # print(stream)
        title = filter_name(yt.title)
        stream.download(None, title)
        return title


def main():
    args = sys.argv[1:]
    if len(sys.argv) != 2:
        print("Usage: YouTube.py [YouTube link]")
        exit(1)
    title = download_video(sys.argv[1])
    print(f"Successfully downloaded {title} from YouTube.\n")

if __name__ == "__main__":
    main()
