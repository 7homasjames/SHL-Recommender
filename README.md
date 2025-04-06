# 🧠 SHL Assessment Recommender

This project is an intelligent recommender system that extracts job descriptions from SHL product catalog pages and suggests relevant SHL assessments using a Large Language Model (LLM). It supports both full URLs and slugs as input and returns a structured markdown table with the most relevant SHL assessments.

---

## ✅ Solution Overview

### 1. Frontend Interface
- **Tool**: `Streamlit`
- Provides a simple UI for users to input:
  - A full SHL job description URL
  - A job slug (identifier string)

### 2. Web Scraping
- **Libraries**: `Selenium`, `BeautifulSoup`
- **Steps**:
  - Launch a Chrome browser using Selenium
  - Load and extract HTML from the given URL
  - Parse and clean the HTML body using BeautifulSoup (remove scripts/styles)

### 3. Text Chunking
- Cleaned HTML content is split into chunks (max 6000 characters) to respect LLM token limits.

### 4. Prompt Engineering + LLM Parsing
- **Libraries**: `LangChain`, `OpenAI GPT-3.5-turbo`
- Prompts the LLM to extract:
  - Most likely job title
  - Top 10 SHL assessments relevant to the job
  - A markdown table with: assessment name, URL, remote testing, adaptive/IRT support, duration, and type

### 5. Displaying Results
- **Streamlit UI** shows:
  - Cleaned job description (for transparency)
  - Markdown-formatted assessment table

---

## 🧰 Tools & Libraries Used

| Tool/Library        | Purpose                                      |
|---------------------|----------------------------------------------|
| `Streamlit`         | UI development                               |
| `Selenium`          | Dynamic web scraping                         |
| `BeautifulSoup`     | HTML parsing and cleanup                     |
| `LangChain`         | LLM prompt orchestration                     |
| `OpenAI GPT-3.5`    | Core LLM for extraction and recommendations  |
| `dotenv`            | API key management via `.env`                |

---
## User Interface
![image](https://github.com/user-attachments/assets/a8a2014f-0d76-472e-9b82-0bb7bdc99ee2)

---

## 🚀 How to Run

1. Clone the repo
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Sample Output

![image](https://github.com/user-attachments/assets/66850592-6296-4be2-915a-204c8786ea31)

  
