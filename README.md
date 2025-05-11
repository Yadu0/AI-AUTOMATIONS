# YouTube Video Finder with Analysis

## Overview

This project automates the process of finding relevant YouTube videos based on a user’s voice or text query. It filters videos based on duration, recency, and relevance, and analyzes the video titles to recommend the best match using a Large Language Model (LLM) such as **ChatGPT 4o Mini** or **Gemini 2.0 Flash**.

### Features:
- Accepts **voice or text input** (supports **Hindi/English**).
- **Searches YouTube** for relevant videos based on the user query.
- Filters the search results:
  - **4-20 minutes** video duration.
  - Posted within the **last 14 days**.
  - Retrieves **top 20 results**.
- Analyzes **video titles** using a **Large Language Model (LLM)**.
- Outputs the **best video** based on title quality and relevance.

## Tech Stack

- **n8n** / **Make.com** / **Python**: For building the automation.
- **YouTube API**: To retrieve video data.
- **ChatGPT 4o Mini** / **Gemini 2.0 Flash**: For analyzing video titles.
- **SpeechRecognition**: For handling voice input.
- **Flask** or **Streamlit**: (Optional) For creating a simple UI (if needed).

## Installation

### Prerequisites

Before you start, make sure you have:
- **Python 3.7+** installed.
- A **Google Cloud** account and access to the **YouTube Data API**.
- An API key from **OpenAI** or **Google Gemini** (depending on which LLM you use).

### 1. Clone the Repository
```bash
git clone https://github.com/Yadu0/AI-AUTOMATIONS.git
cd youtube-finder
2. Install Dependencies
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Set Up API Keys
Create a .env file in the root directory.

Add the following environment variables:

YOUTUBE_API_KEY=<your_youtube_api_key>

OPENAI_API_KEY=<your_openai_api_key> (If using ChatGPT 4o Mini or Gemini)

4. Run the Automation
Run the Python script to start the video finder:

bash
Copy
Edit
python finder.py
5. (Optional) Running the Web Interface
If you want a simple web interface to interact with the automation, you can use Flask or Streamlit. Instructions will vary depending on which framework you choose, but you can easily build a front-end where users can input their queries.

Usage
Voice Input: Use speech recognition to speak your query (e.g., "Best productivity tips for students").

Text Input: Type your query directly into the program.

The automation will:

Search YouTube based on the query.

Filter videos based on the defined parameters.

Analyze video titles with an LLM.

Return the best video based on title relevance and quality.

Example Output
bash
Copy
Edit
Best video based on the query "How to boost productivity":
- Title: "Top 5 Productivity Hacks You Should Try Today!"
- Channel: "Productivity Mastery"
- Duration: 12 minutes
- Published: 3 days ago
- Link: https://www.youtube.com/watch?v=XXXXXX
Troubleshooting
API Rate Limits: If you receive rate limit errors, make sure to check the usage quota on your YouTube API and OpenAI keys.

No Results Found: If no videos meet the criteria, try broadening the search terms or adjusting the filters.

Blocked Push: If you're working with GitHub and you see a blocked push error due to sensitive data (e.g., API keys), make sure you add .env to the .gitignore file to prevent accidental commits of secrets.

Contributing
Feel free to fork the repository, open issues, and submit pull requests for bug fixes or feature enhancements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Future Improvements
Voice Integration: Add more accurate voice input handling and output feedback.

Custom Filters: Allow more filters (e.g., by view count, video quality).

Multilingual Support: Expand the input to support more languages for a broader audience.

Web Interface: Improve the UI and offer a more user-friendly web interface.

Acknowledgments
YouTube Data API: For providing access to YouTube videos and metadata.

OpenAI: For providing the GPT-3.5 and ChatGPT models for analyzing video titles.

n8n / Make.com: For automation and workflow integration.

vbnet
Copy
Edit

### Notes:
- **Setup**: The README provides instructions on setting up the API keys and running the script.
- **Usage**: It explains how to use the project with both voice and text inputs.
- **Future Improvements**: Mention of features you might want to consider implementing later.




