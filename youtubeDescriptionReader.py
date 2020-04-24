from config import youtube_api_key
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=youtube_api_key)

#res = youtube.channels().list(id='theneedledrop', part='contentDetails').execute()

#res = youtube.playlistItems().list(playlistId='UUt7fwAhXDy3oNFTAzF2o8Pw', part='snippet', maxResults=5).execute()

#print(res)

def get_channel_videos(channel_id):
    res = youtube.channels().list(id='theneedledrop', 
                                  part='contentDetails').execute()
    videos = []
    res = youtube.playlistItems().list(playlistId='UUt7fwAhXDy3oNFTAzF2o8Pw', 
                                           part='snippet', 
                                           maxResults=1,
                                           ).execute()
    videos += res['items']  
    return videos

videos = get_channel_videos('theneedledrop')

# for video in videos:
#     reversed_score = []
#     score = ''
#     if('ALBUM REVIEW' in video['snippet']['title']):
#         title = video['snippet']['title']
#         #print(video['snippet']['description'].find('/10'))
#         index = video['snippet']['description'].find('/10')
#         while video['snippet']['description'][index] != '\n':
#             reversed_score.append(video['snippet']['description'][index])
#             index -= 1
#         for i in reversed(reversed_score):
#             score += i
#         score += '10'
#         print(title)
#         print(score)