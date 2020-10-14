'''
Get the list of integers for Codewars Leaderboard score (aka Honor) in descending order

Note:
if it was the bad timing, the data could be updated during your test cases.
Try several times if you had such experience.
'''


import requests
from bs4 import BeautifulSoup

URL = "https://www.codewars.com/users/leaderboard"

def get_leaderboard_honor():
    scores = []
    soup = BeautifulSoup(requests.get(URL).text, "html.parser")
    users = soup.find_all("tr", {"data-username": True})
    for user in users:
        tds = user.find_all("td")
        scores.append(int(tds[-1].get_text(strip=True).replace(",", "")))
    return scores
