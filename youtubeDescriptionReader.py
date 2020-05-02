# Method that gets a list of Youtube videos on a specified channel and playlist through the Youtube API
from config import youtube_api_key
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

def get_channel_videos(channel_id, playlist_id):
    res = youtube.channels().list(id=channel_id, 
                                  part='contentDetails').execute()
    videos = []
    res = youtube.playlistItems().list(playlistId=playlist_id, 
                                           part='snippet', 
                                           maxResults=1,
                                           ).execute()
    videos += res['items']  
    return videos

