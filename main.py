from services.analyzer import analyze_flares, flare_tracker
from api.nasa import get_solar
from data.report_screen import show_flare_report


def main():

    flare_tracker(get_solar())
    
    choice = input("Would you like the Solar Flare Report for the past 30 days? (y/n): ")
    if choice.lower() == "y":
        flares = get_solar()
        report = analyze_flares(flares)
        show_flare_report(report)
    else:
        print("Thank you for tracking!")
        

if __name__ == "__main__":
    main()


