import requests, bs4

team = input("Team?: ")
team = team.strip()
team = team.lower()
team = team.replace(' ', '-')

resp = requests.get(f"https://www.sports-reference.com/cfb/schools/{team}/")

if not resp.ok:
    print("NOT FOUND")
    exit(1)

soup = bs4.BeautifulSoup(resp.text, features="html.parser")

win_elems = soup.select(f"#{team} td[data-stat=wins]")
total_wins = 0
for win in win_elems[:40]:
    wins = win.get_text()
    wins = int(wins)
    total_wins += wins

print(f"{team} has {total_wins} wins")
