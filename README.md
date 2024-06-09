# WhatsApp Chat Sentiment Analysis Using BERT

## Overview

This project aims to analyze sentiments in WhatsApp chat exports using BERT (Bidirectional Encoder Representations from Transformers). By uploading a chat file, the system preprocesses the messages, applies various visualization techniques, and performs sentiment analysis on each message, providing insightful results.

## Features

- **Chat File Upload**: Users can upload their WhatsApp chat exports for analysis.
- **Preprocessing**: Messages are cleaned and normalized for analysis.
- **Visualization**: Various techniques to visualize text data, including word clouds and bar charts.
- **Sentiment Analysis**: Uses BERT to perform sentiment analysis on each message and present the results.

## Modules

### Preprocessor

The `preprocessor.py` module is responsible for preparing the chat data for analysis. It includes functions for:

- **Data Cleaning**: Removing unnecessary characters and noise from the text.
- **Normalization**: Standardizing the text data for consistent analysis.
- **Message Segmentation**: Splitting the chat data into individual messages with timestamps and user information.

#### Key Functions

- `get_sentiment_score(message)`: Uses BERT to get the sentiment label and score for a given message.

### Helper

The `helper.py` module contains various functions for data analysis and visualization. It includes:

- **Statistical Analysis**: Functions to calculate total messages, total words, and other statistics.
- **Visualization**: Functions to create word clouds, bar charts, and other visualizations of the chat data.

#### Key Functions

- `fetch_stats(selected_user, df)`: Returns the total number of messages, words, media messages, and links.
- `most_busy_users(df)`: Identifies the most active users in the chat.
- `create_wordcloud(selected_user, df)`: Generates a word cloud for the most used words.
- `most_common_words(df, selected_user)`: Identifies the most common words used in the chat.
- `emoji_helper(selected_user, df)`: Analyzes the usage of emojis in the chat.
- `monthly_timeline(selected_user, df)`: Generates a monthly timeline of messages.
- `daily_timeline(selected_user, df)`: Generates a daily timeline of messages.
- `week_activity_map(selected_user, df)`: Analyzes weekly activity patterns.
- `month_activity_map(selected_user, df)`: Analyzes monthly activity patterns.
- `activity_heatmap(selected_user, df)`: Creates a heatmap of activity by day and hour.
- `sentiment_analysis(selected_user, df)`: Analyzes the sentiment distribution in the chat.
- `sentiment_analysis_by_user(selected_user, df)`: Analyzes sentiment by user.

### App

The `app.py` module is the main entry point for the Streamlit application. It provides the user interface for uploading chat files, displaying visualizations, and presenting sentiment analysis results.

#### Key Features

- **File Upload**: Allows users to upload WhatsApp chat exports.
- **Interactive Visualizations**: Displays various visualizations of the chat data.
- **Sentiment Analysis Results**: Presents sentiment analysis results using BERT.

### Running the Application

To run the application, follow these steps:

1. **Install Dependencies**: Make sure you have Python and the required packages installed.
   ```bash
   pip install -r requirements.txt
