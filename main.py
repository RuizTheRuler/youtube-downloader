from pytube import YouTube
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

  link = input('Enter the YouTube link: ')
  path = input('Enter the path to save the video: ')
  yt = YouTube(link)

  print(yt.title)
  print(yt.description)
  print()
  choice = yt.streams.filter(progressive = True).get_highest_resolution()
  print(choice)

  print('Downloading...')
  ys.download()
  print('Download Completed')
