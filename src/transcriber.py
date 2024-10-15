import re
from youtube_transcript_api import YouTubeTranscriptApi
from .youtube_api import YouTubeAPI  # Changed back to relative import

class YouTubeTranscriber:
    def __init__(self, api_key):
        self.youtube_api = YouTubeAPI(api_key)

    def get_transcript(self, video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return ' '.join([entry['text'] for entry in transcript])
        except Exception as e:
            print(f"Error getting transcript: {str(e)}")
            return None

    def get_video_info(self, video_id):
        return self.youtube_api.get_video_details(video_id)

    def extract_video_id(self, url):
        # Extract the video ID from various forms of YouTube URLs
        patterns = [
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([^&]+)',
            r'(?:https?:\/\/)?(?:www\.)?youtu\.be\/([^?]+)',
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([^?]+)',
            r'(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([^?]+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    def transcribe_video(self, video_url):
        video_id = self.extract_video_id(video_url)
        if not video_id:
            print("Invalid YouTube URL")
            return None

        transcript = self.get_transcript(video_id)
        video_info = self.get_video_info(video_id)

        if transcript and video_info:
            return {
                'title': video_info['title'],
                'description': video_info['description'],
                'transcript': transcript
            }
        else:
            return None
