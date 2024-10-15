import argparse
import os
from dotenv import load_dotenv
from src.transcriber import YouTubeTranscriber

def main():
    load_dotenv('.env.local')
    api_key = os.getenv('YOUTUBE_API_KEY')

    if not api_key:
        raise ValueError("YouTube API key not found. Please set it in the .env.local file.")

    parser = argparse.ArgumentParser(description='Transcribe YouTube videos.')
    parser.add_argument('url', help='The YouTube video URL to transcribe')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    args = parser.parse_args()

    transcriber = YouTubeTranscriber(api_key)
    result = transcriber.transcribe_video(args.url)

    if result:
        print(f"Title: {result['title']}")
        print(f"Description: {result['description'][:100]}...")

        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result['transcript'])
            print(f"Transcript saved to: {args.output}")
        else:
            print(f"Transcript: {result['transcript'][:500]}...")
    else:
        print("Failed to transcribe the video.")

if __name__ == '__main__':
    main()
