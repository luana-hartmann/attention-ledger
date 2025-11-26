# app_streamlit.py

import streamlit as st
import matplotlib.pyplot as plt
from attention_core import compute_day_distribution, extrapolate_time

PRIMARY_COLOR = "#F50000"  
SECONDARY_COLOR = "#356BFF"  
TERTIARY_COLOR = "#8900C0" 
QUATERNARY_COLOR = "#00C106"  

def render_stacked_bar(label: str, distribution: dict, social_days_text: str | None = None):
    """
    Renders a horizontal stacked bar using simple HTML/CSS.
    `distribution` should have keys: sleep, social, work, free.
    """
    sleep_h = distribution["sleep"]
    social_h = distribution["social"]
    work_h = distribution["work"]
    free_h = distribution["free"]

    # Avoid division by zero
    total = sleep_h + social_h + work_h + free_h
    if total <= 0:
        return

    sleep_pct = sleep_h / 24 * 100
    social_pct = social_h / 24 * 100
    work_pct = work_h / 24 * 100
    free_pct = free_h / 24 * 100

    bar_html = f"""
    <div style="margin-bottom: 12px;">
      <div style="font-weight: 600; margin-bottom: 4px;">{label}</div>
      <div style="
          width: 100%;
          height: 29px;
          border-radius: 999px;
          overflow: hidden;
          border: 1px solid #cccccc;
          display: flex;
      ">
        <div title="Social media: {social_h:.2f} h ({social_pct:.1f}%)"
             style="width: {social_pct}%; background-color: #{PRIMARY_COLOR[1:]};"></div>
        <div title="Sleep: {sleep_h:.2f} h ({sleep_pct:.1f}%)"
             style="width: {sleep_pct}%; background-color: #{SECONDARY_COLOR[1:]};"></div>
        <div title="Work/study: {work_h:.2f} h ({work_pct:.1f}%)"
             style="width: {work_pct}%; background-color: #{TERTIARY_COLOR[1:]};"></div>
        <div title="Remaining free time: {free_h:.2f} h ({free_pct:.1f}%)"
             style="width: {free_pct}%; background-color: #{QUATERNARY_COLOR[1:]};"></div>
      </div>
      <div style="font-size: 0.8rem; margin-top: 4px;">
        Social media: {social_pct:.1f}% &nbsp;|&nbsp;
        Sleep: {sleep_pct:.1f}% &nbsp;|&nbsp;
        Work/study: {work_pct:.1f}% &nbsp;|&nbsp;
        Free: {free_pct:.1f}%
      </div>
    """
    if social_days_text:
        bar_html += f"""
      <div style="font-size: 0.8rem; margin-top: 2px; color: #555;">
        {social_days_text}
      </div>
    """
    bar_html += "</div>"

    st.markdown(bar_html, unsafe_allow_html=True)

def plot_pie_chart(data, labels, title):
    fig, ax = plt.subplots(figsize=(6, 6))  # Tamanho fixo para ambos os gráficos
    colors = ["#356BFF","#F50000", ]  # Vermelho e Azul para os dois segmentos
    
    # Gerando o gráfico de pizza sem os textos dentro
    wedges, texts, autotexts = ax.pie(data, labels=None, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Alterando o fundo para roxo escuro
    fig.patch.set_facecolor('#1D0238')  # Cor roxa escura

    # Ajustando o título
    ax.set_title(title, color="white", fontsize=16)

    # Ajustando o texto para ser branco
    for autotext in autotexts:
        autotext.set(color='white', fontsize=14)  # Aumenta o tamanho do texto e deixa branco

    st.pyplot(fig)

def main():
    # -------------------- page config
    st.set_page_config(page_title="Attention Ledger", page_icon="🧠", layout="centered")

    # title and description
    st.title("Attention Ledger")
    st.markdown(
        "Visualize how your daily habits with **sleep**, **study/work** and **social media** "
        "add up over a day, a year, and even a decade."
    )

    # -------------------- sidebar inputs
    st.sidebar.image("logo.png", width=500)

    st.sidebar.header("Daily routine")
    hours_social = st.sidebar.slider(
        "Hours on social media per day",
        min_value=0.0,
        max_value=20.0,
        value=3.0,
        step=0.5,
    )
    hours_sleep = st.sidebar.slider(
        "Hours of sleep per day",
        min_value=0.0,
        max_value=20.0,
        value=7.0,
        step=0.5,
    )
    hours_work = st.sidebar.slider(
        "Hours of work/study per day",
        min_value=0.0,
        max_value=20.0,
        value=8.0,
        step=0.5,
    )

    # -------------------- compute distributions
    dist = compute_day_distribution(hours_social, hours_sleep, hours_work)

    if dist["total_used"] > 24:
        st.warning(
            "You are reporting more than 24 hours of activities in a single day. "
            "Some estimates might be inconsistent."
        )

    extra = extrapolate_time(hours_social)

    # -------------------- daily bar
    st.subheader("Daily distribution")
    render_stacked_bar(
        "One day (24 hours)",
        dist,
        social_days_text=(
            f"If every day looks like this, you spend about "
            f"{extra['year_days']:.1f} full days per year just on social media."
        ),
    )

    # -------------------- long-term extrapolations
    st.markdown("---")
    st.subheader("Long-term view")

    cols = st.columns(3)

    with cols[0]:
        st.markdown("### 1 month")
        hours_in_month = extra['month_hours']
        videos_in_month = hours_in_month * 60 / 1  # 60 seconds per video
        books_in_month = hours_in_month * 30 / 300  # 30 pages per hour, 300 pages per book
        movies_in_month = hours_in_month / 90  # 90 minutes per movie

        st.markdown(f"In one month, this adds up to about **{extra['month_days']:.2f} full days** on social media.")
        st.markdown(f"This is equivalent to **{hours_in_month:.2f} hours**.")
        
        st.markdown(f"And **{videos_in_month:.0f} videos** of 60 seconds.")
        st.markdown(f"📚 Or you could read **{books_in_month:.0f} books** (300 pages each).")
        st.markdown(f"🎬 Or watch **{movies_in_month:.0f} movies** (90 minutes each).")

    with cols[1]:
        st.markdown("### 1 year")
        hours_in_year = extra['year_hours']
        videos_in_year = hours_in_year * 60 / 1
        books_in_year = hours_in_year * 30 / 300
        movies_in_year = hours_in_year / 90

        st.markdown(f"In one year, this adds up to about **{extra['year_days']:.1f} full days** on social media.")
        st.markdown(f"This is equivalent to **{hours_in_year:.2f} hours**.")
        
        st.markdown(f"And **{videos_in_year:.0f} videos** of 60 seconds.")
        st.markdown(f"📚 Or you could read **{books_in_year:.0f} books** (300 pages each).")
        st.markdown(f"🎬 Or watch **{movies_in_year:.0f} movies** (90 minutes each).")

    with cols[2]:
        st.markdown("### 10 years")
        hours_in_10years = extra['ten_year_hours']
        videos_in_10years = hours_in_10years * 60 / 1
        books_in_10years = hours_in_10years * 30 / 300
        movies_in_10years = hours_in_10years / 90

        st.markdown(f"In ten years, this adds up to about **{extra['ten_year_days']:.1f} full days** on social media.")
        st.markdown(f"This is equivalent to **{hours_in_10years:.2f} hours**.")
        
        st.markdown(f"And **{videos_in_10years:.0f} videos** of 60 seconds.")
        st.markdown(f"📚 Or you could read **{books_in_10years:.0f} books** (300 pages each).")
        st.markdown(f"🎬 Or watch **{movies_in_10years:.0f} movies** (90 minutes each).")


    # -------------------- exercise time
    exercise_per_week_minutes = 150  # 150 min/week recommended by WHO
    exercise_per_week_hours = 150 / 60 # 2.5 hour/week recommended by WHO
    exercise_time_per_week = (extra['month_hours'] * 60) / 30 * 7 / 60

    trainings_possible = min(7, exercise_time_per_week // 1)  

    st.markdown("---")
    st.markdown("### Recommended Exercise Time vs Your Time")
    st.markdown(f"**Recommended by WHO**: {exercise_per_week_hours} hours per week ({exercise_per_week_minutes} minutes).\n")

    st.markdown(f"📊 **With your current social media time**, you could have done **{trainings_possible} one-hour workout sessions per week**.")
    #st.markdown(f"That's a total of {trainings_possible} hours of exercise per week.")
    st.markdown(f"And you would still have {extra['month_hours'] - (trainings_possible * 1):.2f} hours left for other activities in you month!")
    st.markdown(f"With just a little adjustment, you can easily hit the **{exercise_per_week_minutes} minutes** recommended by the WHO!")

    st.markdown("""
    *The exercise time is based on the WHO's recommendation of 150 minutes per week of moderate-intensity physical activity.*
    For more information, you can visit the official [WHO website](https://www.who.int/news-room/fact-sheets/detail/physical-activity).
    """)

    st.markdown("---")
    st.subheader("Knowledge Retention vs Wasted Information")

    # -------------------- short vs long videos
    col1, col2 = st.columns(2)

    short_video_data = [10, 90]  
    short_video_labels = ['Knowledge Retained', 'Wasted Information']
    
    long_video_data = [30, 70] 
    long_video_labels = ['Knowledge Retained', 'Wasted Information']
    
    with col1:
        st.markdown("**Short Videos**")
        plot_pie_chart(short_video_data, short_video_labels, "Short Video Retention vs Wasted Information")
    
    with col2:
        st.markdown("**Long Videos/Movies**")
        plot_pie_chart(long_video_data, long_video_labels, "Long Video Retention vs Wasted Information")

    st.markdown("#### Legend")
    st.markdown("🔵 **Knowledge Retained**: Blue represents the knowledge retained during video consumption.")
    st.markdown("🔴 **Wasted Information**: Red represents the wasted information.")

    st.markdown("""
    **Text from the research study:**

    Studies show that **short videos**, such as those on TikTok, degrade our ability to retain information. 
    With short 60-second videos, only 10% of the content is retained, while 90% is wasted. 
    On the other hand, with longer videos, such as films, knowledge retention can reach 30%, with only 70% of the time being wasted.
    """)

    st.markdown("""
    **Source:**
    Chiossi, F., Haliburton, L., Ou, C., Butz, A., & Schmidt, A. (2023). 
    *Short-Form Videos Degrade Our Capacity to Retain Intentions: Effect of Context Switching On Prospective Memory*. 
    Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI ’23), April 23–28, 2023, Hamburg, Germany. 
    [https://doi.org/10.1145/3544548.3580778](https://doi.org/10.1145/3544548.3580778)
    """)

    # -------------------- closing remarks
    st.markdown("---")
    st.markdown(
        "This is not about guilt. The goal is to make the impact of your daily habits visible. "

        "By understanding how your time is spent, small adjustments in your routine can help you regain focus and improve how you use your attention over time."
    )

    # -------------------- footer
    st.markdown("""
    <style>
        .footer {
            font-size: 0.8rem;
            text-align: center;
            color: #888;
            margin-top: 20px;
        }
    </style>
    <div class="footer">
        Developed by Luana Hartmann F. Cruz | 
        <a href="https://github.com/luana-hartmann" target="_blank" style="color: #356BFF;">GitHub</a> | 
        <a href="https://www.linkedin.com/in/luana-hartmann-f-cruz/" target="_blank" style="color: #356BFF;">LinkedIn</a>
    </div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
