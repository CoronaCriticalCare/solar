from services.analyzer import analyze_flares
from api.nasa import get_solar


def main():
    flares = get_solar()
    analyze_flares(flares)

if __name__ == "__main__":
    main()


