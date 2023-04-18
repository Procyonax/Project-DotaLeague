from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.team import Team
import repositories.team_repository as team_repository
import repositories.match_repository as match_repository

teams_blueprint = Blueprint("teams", __name__)

# INDEX
# GET /teams
@teams_blueprint.route('/teams')
def teams():
    teams = team_repository.select_all()

    return render_template('/teams/index.html', all_teams = teams)

# NEW
# GET /teams/new/
@teams_blueprint.route('/teams/new')
def new_team():
    teams = team_repository.select_all()
    return render_template("/teams/new.html", teams = teams)

# CREATE
# POST /teams/
@teams_blueprint.route('/teams', methods=['POST'])
def create_team():
    team_name = request.form['team_name']
    team = Team(team_name)
    team_repository.save(team)

    return redirect('/teams')

# SHOW
# GET /teams/<id>/
@teams_blueprint.route('/teams/<id>/show')
def show_team(id):
    team = team_repository.select(id)
    return render_template('teams/show.html', team=team)

# EDIT
# GET /teams/<id>/edit/
@teams_blueprint.route('/teams/<id>/edit')
def edit_team(id):
    team = team_repository.select(id)
    # teams = team_repository.select_all()
    return render_template('teams/edit.html', team=team)

# UPDATE
# PUT (POST) /teams/<id>/
@teams_blueprint.route('/teams/<id>', methods=['POST'])
def update_team(id):
    team_name = request.form['team_name']
    team = team_repository.select(id)
    # home_team_id = team_repository.select(home_team)
    # away_team_id = team_repository.select(away_team)
    team = Team(team_name, id)
    team_repository.update(team)
    
    return redirect('/teams')

# DELETE
# DELETE (POST) /teams/<id>/delete/
@teams_blueprint.route('/teams/<id>/delete', methods=['POST'])
def delete_team(id):
    team_repository.delete(id)
    return redirect('/teams')