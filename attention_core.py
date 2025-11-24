# attention_core.py

HOURS_PER_DAY = 24


def compute_day_distribution(hours_social, hours_sleep, hours_work=8):
    """
    Computes the distribution of a 24-hour day among:
    - sleep
    - social media
    - work/study (optional, default 8h)
    - remaining free time
    """
    # ensure everything is float
    h_social = float(hours_social)
    h_sleep = float(hours_sleep)
    h_work = float(hours_work)

    total_used = h_social + h_sleep + h_work
    remaining = max(0.0, HOURS_PER_DAY - total_used)

    return {
        "sleep": h_sleep,
        "social": h_social,
        "work": h_work,
        "free": remaining,
        "total_used": total_used,
    }


def extrapolate_time(hours_per_day):
    """
    Extrapolates social media time for a week, a month, a year and 10 years.
    Returns hours and equivalent full days.
    """
    h_day = float(hours_per_day)

    week_hours = h_day * 7
    month_hours = h_day * 30       # simple approximation
    year_hours = h_day * 365
    ten_year_hours = year_hours * 10

    def hours_to_days(hours):
        return hours / HOURS_PER_DAY

    return {
        "day_hours": h_day,
        "week_hours": week_hours,
        "week_days": hours_to_days(week_hours),
        "month_hours": month_hours,
        "month_days": hours_to_days(month_hours),
        "year_hours": year_hours,
        "year_days": hours_to_days(year_hours),
        "ten_year_hours": ten_year_hours,
        "ten_year_days": hours_to_days(ten_year_hours),
    }
