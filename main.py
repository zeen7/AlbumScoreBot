from youtubeDescriptionReader import get_channel_videos
from reddit_bot import bot_post, r, get_completed

# Infinite loop
while True:
    videos = get_channel_videos('theneedledrop', 'UUt7fwAhXDy3oNFTAzF2o8Pw')

    for video in videos:
        reversed_score = []
        score = ''
        # Gets title and description/score of the video if it is an album review
        if('ALBUM REVIEW' in video['snippet']['title']):
            title = video['snippet']['title']
            # Finds /10 in the description
            index = video['snippet']['description'].find('/10')
            # Finds everthing before /10 in the description to get the full score
            while video['snippet']['description'][index] != '\n':
                reversed_score.append(video['snippet']['description'][index])
                index -= 1
            # Reverses the backwords score
            for i in reversed(reversed_score):
                score += i
            score += '10'
            content = score
            # Posts on Reddit
            bot_post(r, title, content)
