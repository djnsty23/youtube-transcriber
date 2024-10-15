import os
import re
from dotenv import load_dotenv
from src.transcriber import YouTubeTranscriber  # Make sure this path is correct

# Load environment variables from .env.local file
load_dotenv('.env.local')

# Get the API key from the environment variable
api_key = os.getenv('YOUTUBE_API_KEY')

if not api_key:
    raise ValueError("YouTube API key not found. Please set it in the .env.local file.")

transcriber = YouTubeTranscriber(api_key)

# Create a folder for transcripts if it doesn't exist
transcripts_folder = 'transcripts'
os.makedirs(transcripts_folder, exist_ok=True)

def save_transcript(title, transcript):
    # Remove invalid characters from the title to use as a filename
    safe_title = re.sub(r'[^\w\-_\. ]', '_', title)
    filename = os.path.join(transcripts_folder, f"{safe_title}.txt")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(transcript)
    return filename

# Get the video URL from user input
video_url = input("Enter the full YouTube video URL: ")

result = transcriber.transcribe_video(video_url)

if result:
    print(f"Title: {result['title']}")
    print(f"Description: {result['description'][:100]}...")  # Print first 100 characters of description
    
    # Save the transcript to a file
    transcript_file = save_transcript(result['title'], result['transcript'])
    print(f"Transcript saved to: {transcript_file}")
    
    print(f"First 500 characters of transcript: {result['transcript'][:500]}...")
else:
    print("Failed to transcribe the video.")
