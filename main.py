import argparse
from weather import get_weather

def main():
    parser = argparse.ArgumentParser(description="Get weather details for a city")
    parser.add_argument("city", type=str, help="City name")
    args = parser.parse_args()
    get_weather(args.city)

if __name__ == "__main__":
    main()
