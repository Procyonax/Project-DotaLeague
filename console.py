import pdb
from models.match import Match
from models.team import Team

import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

team_repository.delete_all()
match_repository.delete_all()

team1 = Team("Evil Genuises")
team_repository.save(team1)
team2 = Team("TSM")
team_repository.save(team2)
team3 = Team("Beastcoast")
team_repository.save(team3)
team4 = Team("Team Secret")
team_repository.save(team4)
team5 = Team("OG")
team_repository.save(team5)
team6 = Team("Gaiman Gladiators")
team_repository.save(team6)
team7 = Team("Shopify Rebellion")
team_repository.save(team7)
team8 = Team("Team Liquid")
team_repository.save(team8)
team9 = Team("Tundra Esports")
team_repository.save(team9)

team_repository.select_all()

# match1 = Match(team1, team2, "1-0")

match1 = Match(team1.id, team2.id, "1-0")
match_repository.save(match1)

match2 = Match(team1.id, team2.id, "1-1") 
match_repository.save(match2)

match3 = Match(team9.id, team7.id, "1-0")
match_repository.save(match3)

match4 = Match(team5.id, team8.id, "0-1") 
match_repository.save(match4)

match5 = Match(team7.id, team6.id, "0-1")
match_repository.save(match5)

# match1 = Match("Evil Genuises", "TSM", "1-1")
# match_repository.save(match1)

# match2 = Match("Beastcoast", "OG", "2-0")
# match_repository.save(match2)

# match3 = Match("TSM", "Team Secret", "0-2")
# match_repository.save(match3)

# match2 = Match(team3.team_name, team2.team_name, "0-1")
# match_repository.save(match2)

# match3 = Match(team1.team_name, team3.team_name, "1-1")
# match_repository.save(match3)

results = match_repository.select_all()
for match in results:
    print(match.__dict__)

# results = match_repository.select(12)
# for match in results:
#     print(match.__dict__)

# results = team_repository.select('Wildcats')
# print(results)

# print(results)

# print(match1.__dict__)