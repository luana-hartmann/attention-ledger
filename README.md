# Attention Ledger

**Attention Ledger** is a tool designed to visualize how much time of your life is spent on social media, sleep, and work/study. It provides both a **command-line interface (CLI)** and a **Streamlit web interface** to help users track and reflect on their daily routines over the short term (a day) and long term (months, years, or even a decade).

The purpose is not to judge but to make the impact of your daily habits visible. By visualizing how much attention you spend on various activities, you can take more control over how your time is distributed.

---

## Features

- **Daily Input**:
  - Hours spent on social media per day.
  - Hours of sleep per day.
  - Hours of work/study per day.
  
- **Distribute the 24-hour day**:
  - Shows the breakdown of time between **sleep**, **social media**, **work/study**, and **remaining free time**.
  
- **Long-term View**:
  - Extrapolates social media usage to longer periods:
    - 1 month (30 days),
    - 1 year (365 days),
    - 10 years.
  - Expresses long-term usage in both **hours** and **equivalent full days**.
  
- **Visualization**:
  - Displays the daily distribution as a **stacked horizontal bar**.
  - Visualizes **Knowledge Retention vs Wasted Information** with **Pie Charts** comparing the effectiveness of short vs long videos.

- **Exercise Time**:
  - Calculates how much time spent on social media could have been used for exercise, showing potential workout sessions that could be completed to meet the WHO recommendation.

---

## Project Structure

    .
    ├── app_streamlit.py      # Streamlit web app (interactive interface)
    ├── attention_cli.py      # Command-line prototype
    ├── attention_core.py     # Core logic: calculations and helper functions
    └── requirements.txt      # Python dependencies for the project

---

## Requirements

- Python 3.9+ (3.11/3.12 also work)
- Virtual environment tool (`venv`, `virtualenv`, or similar)
- For the web interface:
  - `streamlit`
  
All Python dependencies are listed in `requirements.txt`.

---

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/attention-ledger.git
    cd attention-ledger
    ```

2. **Create and activate a virtual environment**

   - **Linux/macOS**:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

   - **Windows (PowerShell)**:

    ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

If you only want to use the CLI version, `streamlit` is not required, but installing from `requirements.txt` ensures both versions will work.

---

## Command-line Interface (CLI)

The CLI prototype is implemented in `attention_cli.py` and uses the core functions defined in `attention_core.py`.

### Running the CLI version

With the virtual environment activated and dependencies installed:

    ```bash
    python attention_cli.py
    ```

You will be prompted to enter the following values:

- How many hours per day you spend on social media.
- How many hours per day you sleep.
- How many hours per day you work/study.

The script will then:

1. Print the **distribution of a 24-hour day** among sleep, social media, work/study, and remaining free time (in hours and percentages).
2. Extrapolate social media time to **week, month, year, and 10 years**, showing both hours and equivalent full days.
3. Provide a brief comment on sleep if the reported value is below 7 hours per day.

---

## Streamlit Web Interface

The Streamlit app is implemented in `app_streamlit.py`.

### Running the Streamlit app locally

From the project root, with the virtual environment activated:

    ```bash
    streamlit run app_streamlit.py
    ```

Streamlit will start a local web server and open the app in your browser (or provide a local URL such as `http://localhost:8501`).

### How the Web Interface Works

- The **sidebar** contains sliders for:
  - Hours on social media per day.
  - Hours of sleep per day.
  - Hours of work/study per day.

- The **main area** shows:
  - A **"Daily Distribution"** section with a 24-hour stacked bar:
    - **Red**: Social media
    - **Blue**: Sleep
    - **Purple**: Work/study
    - **Green**: Remaining free time
  - A short text summarizing how many full days per year are spent on social media.
  - A **"Long-Term View"** section with three panels showing:
    - 1 month (30 days),
    - 1 year (365 days),
    - 10 years (3650 days).
    
Each panel repeats the same daily pattern as a stacked bar and includes text indicating how many full days are spent on social media over that period.

---

## Access the Online App

To experience the Attention Ledger app without setting up the environment, simply access the online version deployed on Streamlit.

[StreamLit App](https://attention-ledger-o8oxrfjd8atxj3af23nsmb.streamlit.app/)

---

## Customization and Extension Ideas

- Allow users to specify additional categories of time use (e.g., commute, chores).
- Add more detailed textual insights based on thresholds (e.g., messages depending on social media usage).
- Enable exporting results or screenshots for use in reports or presentations.
- Integrate real usage statistics (e.g., importing screen-time data) while keeping a critical perspective on attention and focus.

---

## References

- Chiossi, F., Haliburton, L., Ou, C., Butz, A., & Schmidt, A. (2023). Short-Form Videos Degrade Our Capacity to Retain Intentions: Effect of Context Switching On Prospective Memory. *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23)*. https://doi.org/10.1145/3544548.3580778
