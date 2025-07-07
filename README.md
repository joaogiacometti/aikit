# AIKit

A command-line toolkit for generating AI-powered study tools using Google Gemini.

## Features

- Generate simple flashcards for any topic
- Output formatted for direct import into Anki
- Save generated flashcards to a file
- **More tools coming soon!**

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/joaogiacometti/aikit.git
   cd aikit
   ```

2. Install dependencies:

   ```sh
   uv sync
   ```

3. Copy `.env.example` to `.env` and add your Google AI API key:
   ```sh
   cp .env.example .env
   # Edit .env and set AI_API_KEY
   ```

## Usage

Run a tool (e.g., flashcards):

```sh
python main.py --tool flashcards --prompt "Photosynthesis" --save-output
```

- `--tool` or `-t`: Tool to use (e.g., `flashcards`, more coming soon)
- `--prompt` or `-p`: Topic or question for the tool
- `--save-output` or `-s`: (Optional) Save output to `out/flashcards.txt`

## Configuration

- Set your model in [`config.py`](config.py)
- API key is loaded from `.env` (`AI_API_KEY`)

## Dependencies

- google-genai >= 1.24.0
- python-dotenv >= 1.1.1
