import threading

from services.analyzer import analyze_flares, flare_tracker
from services.apod import show_pic_day
from api.nasa import get_solar, get_apod
from data.report_screen import show_flare_report
from app import app


def run_dashboard():
    app.run(debug=True, use_reloader=False)
def main():

    flare_tracker(get_solar())

    dashboard_thread = threading.Thread(
            target=run_dashboard,
            daemon=True
        )

    dashboard_thread.start()

    while True:
        while True:
            choice = input("Would you like the Solar Flare Report for the past 30 days? (y/n): ").strip().lower()
            if choice == "y":
                flares = get_solar()
                report = analyze_flares(flares)
                show_flare_report(report)
                break
            if choice == "n":
                print("Skipping the report...")
                break
            print("Please enter 'y' or 'n'.")

        while True:
            choice = input("Would you like to see today's Picture of the day? (y/n): ").strip().lower()
            if choice == "y":
                show_pic_day(get_apod())
                break
            if choice == "n":
                print("Skipping the Picture of the Day...")
                return
            print("Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()