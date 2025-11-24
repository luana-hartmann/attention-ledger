# attention_cli.py

from attention_core import compute_day_distribution, extrapolate_time


def main():
    print("=== Attention Ledger (CLI prototype) ===\n")

    # Input collection
    hours_social = float(input("How many hours per day do you spend on social media? "))
    hours_sleep = float(input("How many hours per day do you sleep? "))
    hours_work = float(input("How many hours per day do you work/study? (e.g., 8) "))

    # 1) Day distribution
    distribution = compute_day_distribution(hours_social, hours_sleep, hours_work)

    print("\n--- Distribution of a 24-hour day ---")
    for label, key in [
        ("Sleep", "sleep"),
        ("Social media", "social"),
        ("Work/study", "work"),
        ("Remaining free time", "free"),
    ]:
        h = distribution[key]
        perc = (h / 24) * 100
        print(f"{label}: {h:.2f} h ({perc:.1f}%)")

    if distribution["total_used"] > 24:
        print("\n⚠️  Warning: you are reporting more than 24 hours of activities in a single day.")
        print("   This suggests some of your estimates are inconsistent.\n")

    # 2) Social media extrapolation
    extra = extrapolate_time(hours_social)

    print("\n--- Time spent on social media ---")
    print(f"Per day:    {extra['day_hours']:.2f} h")
    print(
        f"Per week:   {extra['week_hours']:.2f} h  "
        f"(~{extra['week_days']:.2f} full days)"
    )
    print(
        f"Per month:  {extra['month_hours']:.2f} h  "
        f"(~{extra['month_days']:.2f} full days)"
    )
    print(
        f"Per year:   {extra['year_hours']:.2f} h  "
        f"(~{extra['year_days']:.2f} full days)"
    )

    # 3) Extra insight with sleep
    if hours_sleep < 7:
        print("\n💤 You sleep less than 7 hours per day.")
        print("   Lack of sleep erodes focus as well, together with social media overload.")
    else:
        print("\n✅ Your reported sleep time is within a commonly recommended range (>= 7 hours).")

    print("\nThanks for trying the CLI prototype of Attention Ledger :)")

if __name__ == "__main__":
    main()
