import requests, bs4

resp = requests.get("https://www.augusta.edu/ccs/faculty.php")

if not resp.ok:
    print('NOT FOUND')
    exit(1)

soup = bs4.BeautifulSoup(resp.text, features="html.parser")

title_elems = soup.select("title")
#print(title_elems)

if len(title_elems) > 0:
    elem = title_elems[0]
    print(elem.get_text())

profs = soup.select(".profile-contact")
for prof in profs:
    #print(prof)
    #print(prof.get_text())
    n = prof.select_one(".pname")
    if n == None:
        name = "NO NAME"
    else:
        name = n.get_text()
        name = name.strip()
        if len(name) > 35:
            name = name[:32] + '...'

    e = prof.select_one(".mail")
    if e == None:
        email = "NO EMAIL"
    else:
        email = e.get_text()
        email = email.strip()

    p = prof.select_one(".phone")
    if p == None:
        phone = "NO PHONE"
    else:
        phone = p.get_text()
        phone = phone.strip()

    print(f"{name:35}{email:30}{phone}")
