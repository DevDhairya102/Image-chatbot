# Image-chatbot
Image Chatbot – AI-Powered Image Analysis
Image Chatbot is a Streamlit-based web application that utilizes Google Gemini AI to analyze images and generate meaningful responses. Users can upload an image and provide an optional text prompt to get AI-generated insights.

 Features
✅ Upload and analyze images using AI
✅ Accepts optional text prompts for better context
✅ Built with Streamlit, Google Generative AI, and Pillow
✅ Simple and intuitive UI

Steps
Install Dependencies
Set Up API Key
Create a .env file in the project directory.
Add your Google AI API Key inside it:
GOOGLE_API_KEY=your_api_key_here

Steps to Get Your Google Gemini API Key
Go to Google AI Studio

Open Google AI Studio
Sign in with Google

Use your Google account to sign in.
Generate API Key

Click on "Get API Key" in the dashboard.
Copy the generated API key.
Store API Key in a .env File

In your project folder, create a file named .env
Your Python script should include-
from dotenv import load_dotenv
import os
load_dotenv()
genai_api_key = os.getenv("GOOGLE_API_KEY")
