import pdb
from models.match import Match
from models.team import Team

import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

match_repository.delete_all()
team_repository.delete_all()

team1 = Team("Wildcats")
team_repository.save(team1)
team2 = Team("Bing Chilling")
team_repository.save(team2)
team3 = Team("Purdue")
team_repository.save(team3)

team_repository.select_all()

match1 = Match(team1.team_name, team2.team_name, "1-0")
match_repository.save(match1)

match2 = Match(team3.team_name, team2.team_name, "0-1")
match_repository.save(match2)

match3 = Match(team1.team_name, team3.team_name, "1-1")
match_repository.save(match3)

results = match_repository.select_all()
for match in results:
    print(match.__dict__)

# print(results)

# print(match1.__dict__)