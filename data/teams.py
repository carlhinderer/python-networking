import requests
from bs4 import BeautifulSoup

class EspnTeamScraper:
    TEAMS_PAGE = 'http://www.espn.com/nba/teams'

    def __init__(self):
        self.teams = []

    def load_teams(self):
        teams_page = self.load_espn_teams_page()
        self.load_divisions(teams_page)

    def load_divisions(self, teams_page):
        divisons = teams_page.find_all(class_='mt7')
        for d in divisons:
            self.load_division(d)

    def load_division(self, division):
        division_name = division.contents[0].text
        teams = division.contents[1]
        for t in teams.contents:
            team = t.find(class_='TeamLinks')
            self.load_team(division_name, team)

    def load_team(self, division_name, team):
        team_name_part = team.contents[0]
        rest = team.contents[1]
        return {
            'division': division_name,
            'team_name': team_name_part.contents[1],
            'team_link': team_name_part.contents[0],
            'stats_link': '',
            'schedule_link': '',
            'roster_link': '',
            'depth_chart_link': '',
            'tickets_link': ''
        }

    def load_espn_teams_page(self):
        teams_page = requests.get(self.TEAMS_PAGE)
        if not teams_page.ok:
            raise RuntimeError('Cant access teams page.')
        team_soup = BeautifulSoup(teams_page.text, 'lxml')
        return team_soup
        


if __name__ == '__main__':
    scraper = EspnTeamScraper()
    teams = scraper.load_teams()
    for t in scraper.teams:
        print(team['team_name'])