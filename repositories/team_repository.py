from db.run_sql import run_sql

from models.team import Team
from models.match import Match

def save(team):
    sql = "INSERT INTO teams (team_name) VALUES (%s) RETURNING *"
    values = [team.team_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        team = Team(row['team_name'], row['id'] )
        teams.append(team)
    return teams


def select(id):
    # print(id)
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    # print(results)

    if results:
        result = results[0]
        team = Team(result['team_name'], result['id'] )
        # print(team)
    return team


def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET team_name = %s WHERE id = %s"
    values = [team.team_name, team.id]
    run_sql(sql, values)

def matches(team):
    matches = []

    sql = "SELECT * FROM matches WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        match = Match(row['home_team'], row['away_team'], row['result'], row['id'] )
        matches.append(match)
    return matches
