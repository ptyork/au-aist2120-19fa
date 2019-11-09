import requests, bs4

team = input("Enter team: ")
team = team.strip()
team = team.lower()
team = team.replace(' ', '-')

years = input("Enter years: ")
years = int(years)

resp = requests.get(f"https://www.sports-reference.com/cfb/schools/{team}/")

if not resp.ok:
    print('NOT FOUND')
    exit(1)

soup = bs4.BeautifulSoup(resp.text, features="html.parser")

win_elems = soup.select(f"#{team} td[data-stat=wins]")
total_wins = 0
for elem in win_elems[:years]:
    winstr = elem.get_text()
    wins = int(winstr)
    total_wins += wins

print(f"{team.title()} has {total_wins} wins over the past {years} years!")
