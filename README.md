# Python Projects 🐍

A collection of Python projects exploring different areas of software development, including Voice Assistants, Automation, GUI Development, and Web Scraping.

The repository contains practical projects demonstrating Python programming, third-party library integration, automation techniques, and interaction with external services.

---

## 📂 Projects

### 1. Alexa.py — Voice Assistant ⭐

A Python-based voice assistant inspired by Amazon Alexa, designed to recognize voice commands and perform various tasks through speech interaction.

**Key Features:**
- **Speech Recognition:** Listens to and processes voice commands using a microphone.
- **Text-to-Speech:** Responds to users with synthesized speech.
- **Web Navigation:** Opens popular websites and platforms, including Google, YouTube, LinkedIn, WhatsApp, and ChatGPT.
- **Time & Weather:** Provides the current time and retrieves weather information for Cairo.
- **Wikipedia Search:** Searches Wikipedia and delivers summarized information through voice responses.

**Technologies & Libraries:**
- Python
- SpeechRecognition
- pyttsx3
- Wikipedia API
- Requests
- PyAutoGUI

**Installation:**
```bash
pip install SpeechRecognition pyttsx3 wikipedia requests pyautogui
```

**Requirements:**
- A working microphone.
- PyAudio may be required for microphone input.
- A valid weather API key for weather functionality.

---

### 2. AutoGUI.py — YouTube Shorts Automation

A desktop automation script that uses PyAutoGUI to interact with YouTube Shorts and automate repetitive actions.

**Key Features:**
- Automatically opens a specified YouTube link.
- Navigates through YouTube Shorts.
- Automates liking multiple Shorts.

**Technologies & Libraries:**
- Python
- PyAutoGUI

**Installation:**
```bash
pip install pyautogui
```

---

### 3. DriverGenerator.py — Embedded Systems File Generator

A GUI-based utility developed with Tkinter to simplify and automate the generation of standard driver files for Embedded Systems projects.

**Key Features:**
- Generates predefined driver file templates.
- Automatically adds header comments and file guards.
- Supports selecting the software layer and author information.
- Reduces repetitive manual work when creating driver structures.

**Generated Files:**
- `interface.h`
- `private.h`
- `config.h`
- `main.c`

**Technologies & Libraries:**
- Python
- Tkinter

---

### 4. Fantasy.py — Fantasy Premier League Auto Selector

An automation script designed to interact with the Fantasy Premier League website and automatically select players for different team positions.

**Key Features:**
- Automates browser interactions.
- Selects players across different positions:
  - Forwards
  - Midfielders
  - Defenders
  - Goalkeepers
- Uses screen recognition and image-based interaction to automate selection.

**Technologies & Libraries:**
- Python
- PyAutoGUI

**Note:** The script relies on screen coordinates and reference images (`Forward.png`, `Select.png`, and `SortBy.png`). Adjustments may be required depending on screen resolution and layout.

---

### 5. Project1.py — Web Scraping (Abjjad)

A web scraping project that extracts book-related information from [Abjjad](https://www.abjjad.com/) and exports the collected data into an Excel spreadsheet.

**Key Features:**
- Extracts book information from the website.
- Collects book titles and authors.
- Retrieves ratings and available book content.
- Exports the scraped data into Excel format.

**Technologies & Libraries:**
- Python
- Requests
- BeautifulSoup4
- Pandas
- lxml
- OpenPyXL

**Installation:**
```bash
pip install requests beautifulsoup4 pandas lxml openpyxl
```

---

## 🛠️ Technologies & Tools

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Voice Assistant | SpeechRecognition, pyttsx3 |
| Automation | PyAutoGUI |
| GUI Development | Tkinter |
| Web Scraping | Requests, BeautifulSoup4, lxml |
| Data Processing | Pandas, OpenPyXL |
| External APIs | Wikipedia, Weather API |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AboAlsho2/Python-Projects.git
```

### 2. Navigate to the Project Directory

```bash
cd Python-Projects
```

### 3. Install Dependencies

Install the required libraries for the specific project you want to run.

### 4. Run a Project

```bash
python Alexa.py
```

You can replace `Alexa.py` with any other Python script in the repository.

---

## ⚠️ Important Notes

- Each project has its own dependencies. Install only the libraries required for the project you intend to run.
- `Alexa.py` requires microphone access and may require a weather API key.
- Automation scripts (`AutoGUI.py` and `Fantasy.py`) depend on screen resolution, coordinates, and desktop layout.
- `Project1.py` may require updating the output Excel file path depending on your local environment.

---

## 📌 Repository

**GitHub:** [AboAlsho2/Python-Projects](https://github.com/AboAlsho2/Python-Projects)

