# FLUX: YouTube Sentiment Analysis Engine

**FLUX** is a streamlined Python-based tool designed to scrape YouTube comments and perform deep sentiment analysis using a hybrid approach. It combines the speed of VADER (Valence Aware Dictionary and sEntiment Reasoner) with the contextual intelligence of Local LLMs (via Ollama) to categorize audience reactions into Positive, Negative, or Neutral sentiments.

---

## 🚀 Features

* **Automated Scraping:** Extract comments directly from any YouTube URL using `youtube-comment-downloader`.
* **Hybrid Sentiment Analysis:** * **VADER:** Provides instant polarity scoring for clear-cut comments.
    * **Ollama (Gemma 3:1b):** Automatically handles ambiguous or "neutral" VADER scores by leveraging a local LLM for better nuance detection.
* **Real-time Progress:** Visual feedback in the terminal using the `rich` library.
* **Data Visualization:** Generates a comprehensive pie chart of the overall sentiment distribution using `matplotlib`.
* **Exportable Data:** Cleans and saves processed data into CSV format for further research.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Analysis:** `vaderSentiment`, `ollama`
* **Data Handling:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `rich`
* **Scraping:** `youtube-comment-downloader`

---

## 📋 Prerequisites

Before running FLUX, ensure you have the following installed:

1.  **Python 3.8+**
2.  **Ollama:** Download and install from [ollama.com](https://ollama.com).
3.  **Local Model:** Pull the required model for the LLM fallback:
    ```bash
    ollama pull gemma3:1b
    ```

---

## 🔧 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/flux.git](https://github.com/yourusername/flux.git)
    cd flux
    ```

2.  **Install dependencies:**
    ```bash
    pip install pandas numpy matplotlib rich vaderSentiment youtube-comment-downloader ollama
    ```

3.  **Project Structure:** Ensure your directory includes the following modules:
    * `main.py`: The entry point and logic controller.
    * `scraper.py`: Handles the YouTube data extraction.
    * `sentiment.py`: Contains the `ai_detect` logic and VADER integration.

---

## 🖥️ Usage

1.  **Run the application:**
    ```bash
    python main.py
    ```
2.  **Input:** When prompted, paste the URL of the YouTube video you wish to analyze.
3.  **Processing:** The script will scrape up to 100 comments (or 500 seconds worth of data) and begin the sentiment classification.
4.  **Results:** * View real-time sentiment tags in your terminal.
    * Review the final **Average Sentiment Score**.
    * Analyze the generated **Pie Chart** for a visual breakdown of the data.

---

## 🧠 Logic Workflow

FLUX utilizes a "Failover Analysis" logic to ensure accuracy:
1.  **Stage 1:** VADER calculates a compound score.
2.  **Stage 2:** If the score is between $-0.05$ and $0.05$ (the "Grey Zone"), the comment is passed to **Gemma 3:1b** via Ollama.
3.  **Stage 3:** The LLM interprets sarcasm or context to return a definitive `-1`, `0`, or `1`.

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.
