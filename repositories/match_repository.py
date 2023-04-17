from db.run_sql import run_sql

from models.match import Match
from models.team import Team
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team_id, away_team_id, result) VALUES (%s, %s, %s) RETURNING *"
    values = [match.home_team_id, match.away_team_id, match.result]
    results = run_sql(sql, values)
    # print(results)
    id = results[0]['id']   
    print(id)
    match.id = id
    return match

# Function to select all match results in league
def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        # team1 = team_repository.select(row['home_team_id'])
        # team2 = team_repository.select(row['away_team_id'])
        match = Match(row['home_team_id'], row['away_team_id'], row['result'], row['id'] )
        matches.append(match)
    return matches


# Function to select all matches for a specific team
def select(id):
    # matches = []
    # match = None
    # sql = "SELECT * FROM matches WHERE home_team_id = %s OR away_team_id = %s"
    # values = [id, id]
    # result = run_sql(sql, values)

    # for row in results:
    #     match = Match(row['home_team_id'], row['away_team_id'], row['result'], row['id'] )
    #     matches.append(match)
    # return matches

    # if result is not None:
    #     # team1 = team_repository.select(result['home_team_id'])
    #     # team2 = team_repository.select(result['away_team_id'])
    #     match = Match(result['home_team_id'], result['away_team_id'], result['result'], result['id'] )
    # return match

    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        match = Match(result['home_team_id'], result['away_team_id'], result['result'], result['id'] )
    return match


def delete_all():
    sql = "DELETE  FROM matches"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(match):
    sql = "UPDATE matches SET (home_team_id, away_team_id, result) = (%s, %s, %s) WHERE id = %s"
    values = [match.home_team_id, match.away_team_id, match.result, match.id]
    run_sql(sql, values)


