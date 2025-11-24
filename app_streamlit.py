# app_streamlit.py

import streamlit as st
from attention_core import compute_day_distribution, extrapolate_time


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
          height: 26px;
          border-radius: 999px;
          overflow: hidden;
          border: 1px solid #cccccc;
          display: flex;
      ">
        <div title="Sleep: {sleep_h:.2f} h ({sleep_pct:.1f}%)"
             style="width: {sleep_pct}%; background-color: #4e79a7;"></div>
        <div title="Social media: {social_h:.2f} h ({social_pct:.1f}%)"
             style="width: {social_pct}%; background-color: #f28e2b;"></div>
        <div title="Work/study: {work_h:.2f} h ({work_pct:.1f}%)"
             style="width: {work_pct}%; background-color: #59a14f;"></div>
        <div title="Remaining free time: {free_h:.2f} h ({free_pct:.1f}%)"
             style="width: {free_pct}%; background-color: #e0e0e0;"></div>
      </div>
      <div style="font-size: 0.8rem; margin-top: 4px;">
        Sleep: {sleep_pct:.1f}% &nbsp;|&nbsp;
        Social: {social_pct:.1f}% &nbsp;|&nbsp;
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


def main():
    st.set_page_config(page_title="Attention Ledger", page_icon="🧠", layout="centered")

    st.title("Attention Ledger")
    st.markdown(
        "Visualize how your daily habits with **sleep**, **work**, and **social media** "
        "add up over a day, a year, and even a decade."
    )

    # Sidebar inputs
    st.sidebar.header("Daily routine")
    hours_social = st.sidebar.slider(
        "Hours on social media per day",
        min_value=0.0,
        max_value=12.0,
        value=3.0,
        step=0.5,
    )
    hours_sleep = st.sidebar.slider(
        "Hours of sleep per day",
        min_value=0.0,
        max_value=12.0,
        value=7.0,
        step=0.5,
    )
    hours_work = st.sidebar.slider(
        "Hours of work/study per day",
        min_value=0.0,
        max_value=16.0,
        value=8.0,
        step=0.5,
    )

    # Compute distributions
    dist = compute_day_distribution(hours_social, hours_sleep, hours_work)

    if dist["total_used"] > 24:
        st.warning(
            "You are reporting more than 24 hours of activities in a single day. "
            "Some estimates might be inconsistent."
        )

    extra = extrapolate_time(hours_social)

    # Daily bar
    st.subheader("Daily distribution")
    render_stacked_bar(
        "One day (24 hours)",
        dist,
        social_days_text=(
            f"If every day looks like this, you spend about "
            f"{extra['year_days']:.1f} full days per year just on social media."
        ),
    )

    # Bars + days for month, year, 10 years
    st.subheader("Long-term view")

    cols = st.columns(3)

    with cols[0]:
        st.markdown("**1 month** (30 days)")
        render_stacked_bar(
            "Same daily pattern",
            dist,
            social_days_text=(
                f"In one month, this adds up to about "
                f"{extra['month_days']:.2f} full days on social media."
            ),
        )

    with cols[1]:
        st.markdown("**1 year** (365 days)")
        render_stacked_bar(
            "Same daily pattern",
            dist,
            social_days_text=(
                f"In one year, this adds up to about "
                f"{extra['year_days']:.1f} full days on social media."
            ),
        )

    with cols[2]:
        st.markdown("**10 years**")
        render_stacked_bar(
            "Same daily pattern",
            dist,
            social_days_text=(
                f"In ten years, this adds up to about "
                f"{extra['ten_year_days']:.1f} full days on social media."
            ),
        )

    st.markdown("---")
    st.markdown(
        "This is not about guilt. The goal is to make the impact of your daily habits visible."
        "By understanding how your time is spent, small adjustments in your routine can help you regain focus and improve how you use your attention over time."
    )

if __name__ == "__main__":
    main()
