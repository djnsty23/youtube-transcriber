from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

class YouTubeAPI:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_details(self, video_id):
        request = self.youtube.videos().list(
            part="snippet",
            id=video_id
        )
        response = request.execute()
        return response['items'][0]['snippet']
