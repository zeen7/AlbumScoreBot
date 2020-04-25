from youtubeDescriptionReader import get_channel_videos
from reddit_bot import bot_post, r, get_completed

while True:
    videos = get_channel_videos('theneedledrop')

    for video in videos:
        reversed_score = []
        score = ''
        if('ALBUM REVIEW' in video['snippet']['title']):
            title = video['snippet']['title']
            #print(video['snippet']['description'].find('/10'))
            index = video['snippet']['description'].find('/10')
            while video['snippet']['description'][index] != '\n':
                reversed_score.append(video['snippet']['description'][index])
                index -= 1
            for i in reversed(reversed_score):
                score += i
            score += '10'
            content = score
    get_completed()
    bot_post(r, title, content)
