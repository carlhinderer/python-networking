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
        team_details = self.parse_team(division_name, team)
        self.teams.append(team_details)

    def parse_team(self, division_name, team):
        anchor_tags = team.find_all(class_='AnchorLink')
        team_link = anchor_tags[1]['href']
        team_name = anchor_tags[1].text
        stats_link = anchor_tags[2]['href']
        schedule_link = anchor_tags[3]['href']
        roster_link = anchor_tags[4]['href']
        depth_chart_link = anchor_tags[5]['href']
        
        return {
            'division': division_name,
            'team_link': team_link,
            'team_name': team_name,
            'stats_link': stats_link,
            'schedule_link': schedule_link,
            'roster_link': roster_link,
            'depth_chart_link': depth_chart_link
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
        print(t['team_name'], '-', t['division'])