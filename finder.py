import os
import openai
import isodate
from dotenv import load_dotenv
from datetime import datetime, timedelta
from googleapiclient.discovery import build
import time
import openai

def analyze_with_openai(videos, query):
    titles = [v['title'] for v in videos]
    prompt = f"""You are a YouTube recommendation engine.

Given the user's query: "{query}", choose the most relevant and engaging title from this list:
{chr(10).join(f"- {title}" for title in titles)}

Return only the best matching title."""

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Changed model to gpt-3.5-turbo
            prompt=prompt,
            temperature=0.5,
            max_tokens=100  # Adjust as needed
        )
        return response['choices'][0]['text'].strip()
    except openai.error.RateLimitError:
        print("❌ Rate limit exceeded. Retrying after a brief pause...")
        time.sleep(60)  # Wait for 60 seconds before retrying
        return analyze_with_openai(videos, query)  # Retry the request


# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

openai.api_key = OPENAI_API_KEY

def get_user_input():
    return input("🔍 Enter your video search query: ")

def search_youtube(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    published_after = "2000-01-01T00:00:00Z"  

    search_response = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=25,
        publishedAfter=published_after
    ).execute()

    video_ids = [item['id']['videoId'] for item in search_response['items']]
    return youtube, video_ids

def get_filtered_videos(youtube, video_ids):
    details = youtube.videos().list(
        part="contentDetails,snippet",
        id=",".join(video_ids)
    ).execute()

    videos = []
    for item in details['items']:
        duration = isodate.parse_duration(item['contentDetails']['duration']).total_seconds() / 60
        if 4 <= duration <= 20:
            videos.append({
                'title': item['snippet']['title'],
                'url': f"https://www.youtube.com/watch?v={item['id']}",
                'duration': round(duration, 1)
            })
    return videos

def analyze_with_openai(videos, query):
    titles = [v['title'] for v in videos]
    prompt = f"""You are a YouTube recommendation engine.

Given the user's query: "{query}", choose the most relevant and engaging title from this list:
{chr(10).join(f"- {title}" for title in titles)}

Return only the best matching title."""

    # Using gpt-3.5-turbo instead of gpt-4
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  # Changed model to gpt-3.5-turbo
        prompt=prompt,
        temperature=0.5,
        max_tokens=100  # Adjust as needed
    )

    return response['choices'][0]['text'].strip()


    response = openai.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5
)

    return response['choices'][0]['message']['content'].strip()

def main():
    query = get_user_input()
    youtube, video_ids = search_youtube(query)
    videos = get_filtered_videos(youtube, video_ids)

    if not videos:
        print("❌ No videos found matching your criteria.")
        return

    best_title = analyze_with_openai(videos, query)
    matched_video = next((v for v in videos if best_title in v['title']), None)

    if matched_video:
        print("\n✅ Best Video Recommendation:")
        print(f"Title: {matched_video['title']}")
        print(f"Duration: {matched_video['duration']} minutes")
        print(f"URL: {matched_video['url']}")
    else:
        print("\n🔎 Suggested Title:", best_title)
        print("Couldn't match it to a specific video URL.")

if __name__ == "__main__":
    main()
