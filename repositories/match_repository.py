from db.run_sql import run_sql

from models.match import Match
from models.team import Team
import repositories.team_repository as team_repository

def save(match):
    sql = "INSERT INTO matches (home_team, away_team, result) VALUES (%s, %s, %s) RETURNING *"
    values = [match.home_team, match.away_team, match.result]
    results = run_sql(sql, values)
    # print(results)
    id = results[0]['id']   
    # print(id)
    match.id = id
    return match

# Function to select all match results in league
def select_all():
    matches = []

    sql = "SELECT * FROM matches"
    results = run_sql(sql)

    for row in results:
        team1 = team_repository.select(row['home_team'])
        team2 = team_repository.select(row['away_team'])
        match = Match(team1, team2,  row['result'], row['id'] )
        matches.append(match)
    return matches


# Function to select all matches for a specific team
def select(id):
    # matches = []
    # match = None
    # sql = "SELECT * FROM matches WHERE home_team = %s OR away_team = %s"
    # values = [id, id]
    # result = run_sql(sql, values)

    # for row in results:
    #     match = Match(row['home_team'], row['away_team'], row['result'], row['id'] )
    #     matches.append(match)
    # return matches

    # if result is not None:
    #     # team1 = team_repository.select(result['home_team'])
    #     # team2 = team_repository.select(result['away_team'])
    #     match = Match(result['home_team'], result['away_team'], result['result'], result['id'] )
    # return match

    match = None
    sql = "SELECT * FROM matches WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results is not None:
        result= results[0]
        team1 = team_repository.select(result['home_team'])
        team2 = team_repository.select(result['away_team'])
        match = Match(team1, team2,  result['result'], result['id'] )
    return match


def delete_all():
    sql = "DELETE  FROM matches"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM matches WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(match):
    sql = "UPDATE matches SET (home_team, away_team, result) = (%s, %s, %s) WHERE id = %s"
    values = [match.home_team, match.away_team, match.result, match.id]
    run_sql(sql, values)



    # Name a function called 'select_all' which will first generate an empty list named 'matches'
    # Execute SQL query to select all matches from the database
    # Iterate over each row in the query results
        # Retrieve home team and away team objects from the 'team_repository'
            # Create a 'Match' object with the retrieved teams and match result data
        # Add the 'Match' object to the list of matches
    # Return the list of 'Match' objects

