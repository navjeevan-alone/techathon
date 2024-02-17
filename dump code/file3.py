from googleapiclient.discovery import build

# Your Google API Key
API_KEY = "AIzaSyCZ2Vn50GJKiaDsFOvL6LCgiY8jZTo4wwc"

# Prompt for video search
prompt = "internal structure of electron"

# Create a YouTube Data API client
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Make a search request to YouTube Data API
search_response = youtube.search().list(
    q=prompt,
    part='id,snippet',
    maxResults=3,  # Return up to 3 videos
    type='video',  # Only search for videos
    relevanceLanguage='en',  # Language preference
    safeSearch='strict',  # Exclude adult content
    videoDuration='any',  # Return videos of any duration
    order='relevance'  # Sort by relevance
).execute()

# Extract video information and print links
for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
        video_title = search_result['snippet']['title']
        video_id = search_result['id']['videoId']
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        print(f"{video_title}: {video_link}")
