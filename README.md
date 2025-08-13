# OSINT Google Dorking Search Script

## Overview
This Python script automates Google searches for OSINT (Open Source Intelligence) and Google Dorking. It retrieves URLs matching a search term, fetches page content, analyzes sentiment, detects crime-related keywords, and classifies the source type. Results are saved in JSON format for further analysis.

## Features
- Accepts search term, number of results, pause between requests, output file name, and location filter.
- Uses Google Dorking syntax (`intext:`) for targeted searches.
- Fetches and parses web page content for each result.
- Performs sentiment analysis using TextBlob.
- User agent rotation and proxy support to prevent Google from blocking requests
- Flags pages mentioning crime-related keywords.
- Classifies sources (social, news, informational, government, education, forum, other).
- Outputs results to a JSON file.

## Requirements
- Python 3.7+
- Packages: `requests`, `colorama`, `googlesearch-python`, `textblob`, `beautifulsoup4`

## Installation
**Step 1**
```bash
git clone https://github.com/marsacom/OSINT_S3ARCH3R.git
```    
**Step 2**
```bash
pip3 install -r requirements.txt
```

## Usage
Run the script from the command line:
```bash
python osearcher.py
```
**OR (if on Windows, download from [releases](https://github.com/marsacom/OSINT_S3ARCH3R/releases/download/v1.1/osearcher.exe))**
```bash
osearcher.exe
```

You will be prompted for:
- Search term (e.g., "John Doe")
- Number of results to generate (e.g., 10)
- Location filter (optional, e.g, California)
- Output file name (optional, e.g., johndoe_results)
- Pause between requests (seconds, default 2)

Example:
```
Enter search term (e.g., "John Doe"): John Doe
Enter number of results to generate (e.g., 10): 10
Enter location filter (optional, press Enter to skip): New York
Enter output file name (optional, press Enter to skip): johndoe_results
Enter pause between requests (in seconds, default 2): 2
```

## Output
Results are saved in a JSON file with fields:
- `url`: The result URL
- `title`: Page title
- `snippet`: Text snippet from the page
- `source_type`: Classified source type(s)
- `mentions_crime`: True/False if crime keywords found
- `sentiment`: The sentiment value in your results is a score calculated by the TextBlob library, which analyzes the text content of each web page snippet. It ranges from -1.0 (very negative) to +1.0 (very positive). A value close to 0 means the text is neutral. Positive values (e.g., 0.16, 0.3) indicate the text is generally positive or optimistic. Negative values (e.g., -0.5) would indicate the text is negative or pessimistic. In your results, the sentiment helps you quickly see if the page content is positive, negative, or neutral.
- `confidence`: The confidence value in your results is a custom score you calculate for each URL. It is meant to estimate how relevant or significant the result is, based on crime mentions and sentiment. If the page mentions crime (crime_flag is True), confidence is set to 0.7. Otherwise, confidence is calculated as 0.5 + abs(sentiment)/2, so it increases with stronger positive or negative sentiment. This value helps you quickly gauge which results are more likely to be important or noteworthy for your search.

## Notes
- The script is for legal, ethical OSINT research only.
- Google may block requests if run too quickly or too often.
- For best results, use specific search terms and reasonable pause values.

## Author
Brayden Kukla, 2024
