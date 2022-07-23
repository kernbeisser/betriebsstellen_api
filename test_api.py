import requests
import sys

base_url = "http://127.0.0.1:5000/"


def main():
    if len(sys.argv) < 2:
        print("booh!")
        sys.exit()
    else:
        abk = sys.argv[1]
        response = requests.get(base_url + 'betriebsstelle/' + abk)
        print(response.json())


if __name__ == '__main__':
    main()