# Attention Ledger

Attention Ledger is a small exploratory tool that makes visible how much of a person’s life is spent on social media.  
It provides two simple interfaces:

1. A **command-line prototype** (CLI), focused on quick interaction and text output.  
2. A **Streamlit web interface**, which visualizes a 24-hour day as a stacked bar chart and extrapolates social media time to longer periods (month, year, decade).

The goal is not to moralize, but to offer a clear, data-based view of how everyday habits with social media, sleep and work/study accumulate over time and affect our available attention.

---

## Features

- Input daily:
  - hours spent on social media;
  - hours of sleep;
  - hours of work/study.
- Compute a **24-hour distribution** into:
  - sleep,
  - social media,
  - work/study,
  - remaining free time.
- Extrapolate social media usage to:
  - 1 week,
  - 1 month (30 days),
  - 1 year (365 days),
  - 10 years.
- Express long-term social media usage both in **hours** and in **equivalent full days**.
- Visualize the daily distribution as a **stacked horizontal bar** in the Streamlit UI.

---

## Project structure

    .
    ├── app_streamlit.py      # Streamlit web app (interactive interface)
    ├── attention_cli.py      # Command-line prototype
    ├── attention_core.py     # Core logic: calculations and helper functions
    └── requirements.txt      # Python dependencies for the project

---

## Requirements

- Python 3.9+ (3.11/3.12 also work)  
- Virtual environment tool (`venv`, `virtualenv` or similar)  
- For the web interface:
  - `streamlit`

All Python dependencies are listed in `requirements.txt`.

---

## Installation

1. **Clone the repository**

    git clone https://github.com/<your-username>/attention-ledger.git
    cd attention-ledger

2. **Create and activate a virtual environment**

   Linux/macOS:

    python3 -m venv .venv
    source .venv/bin/activate

   Windows (PowerShell):

    python -m venv .venv
    .\.venv\Scripts\Activate

3. **Install dependencies**

    pip install -r requirements.txt

If you only want to use the CLI version, `streamlit` is technically not required, but installing from `requirements.txt` is the simplest way to keep both versions working.

---

## Command-line interface (CLI)

The CLI prototype is implemented in `attention_cli.py` and uses the core functions defined in `attention_core.py`.

### Running the CLI version

With the virtual environment activated and dependencies installed:

    python attention_cli.py

You will be prompted for three values:

- How many hours per day you spend on social media.  
- How many hours per day you sleep.  
- How many hours per day you work or study.  

The script will then:

1. Print the **distribution of a 24-hour day** among sleep, social media, work/study and remaining free time (in hours and percentages).  
2. Extrapolate social media time to **week, month, year and 10 years**, showing both hours and equivalent full days.  
3. Provide a brief comment on sleep if the reported value is below 7 hours per day.

This version is useful for quick experiments, debugging and testing the underlying logic without any graphical interface.

---

## Streamlit web interface

The Streamlit application is implemented in `app_streamlit.py`.  
It uses the same core logic from `attention_core.py`, but presents the results in a more visual and accessible way.

### Running the Streamlit app locally

From the project root, with the virtual environment activated:

    streamlit run app_streamlit.py

Streamlit will start a local web server and open the app in your browser (or provide a local URL such as `http://localhost:8501`).

### How the web interface works

- The **sidebar** contains three sliders:
  - Hours on social media per day.
  - Hours of sleep per day.
  - Hours of work/study per day.

- The **main area** shows:
  - A **“Daily distribution”** section, with a 24-hour stacked bar:
    - blue: sleep,  
    - orange: social media,  
    - green: work/study,  
    - light gray: remaining free time.
  - A short text summarizing how many full days per year are effectively spent on social media, if every day looks like the chosen routine.
  - A **“Long-term view”** section with three panels:
    - 1 month (30 days),  
    - 1 year (365 days),  
    - 10 years.  

    Each panel repeats the same daily pattern as a stacked bar and includes a text indicating how many full days in that period are spent on social media.

- At the bottom, a brief conclusion remarks that the aim is to make invisible patterns visible and to encourage reflection on how attention is distributed over time.

---

## Access the Online App

To experience the Attention Ledger app without setting up the environment, simply access the online version deployed on Streamlit. Click the link below: 

[StreamLit App](https://attention-ledger-o8oxrfjd8atxj3af23nsmb.streamlit.app/)
---

## Customization and extension ideas

Some straightforward extensions that can be implemented on top of the current structure:

- Allow users to specify additional categories of time use (commute, chores, household care).  
- Add more detailed textual insights based on thresholds (for example, different messages depending on whether social media usage is above or below a certain number of hours per day).  
- Export results or screenshots for use in reports and presentations.  
- Integrate real usage statistics in the future (for example, importing screen-time data), while still keeping a clear, critical perspective on attention and focus.

---
