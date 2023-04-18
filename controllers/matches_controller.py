from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.match import Match
import repositories.match_repository as match_repository
import repositories.team_repository as team_repository

matches_blueprint = Blueprint("matches", __name__)

# INDEX
# GET /matches
@matches_blueprint.route('/matches')
def matches():
    matches = match_repository.select_all()

    return render_template('/matches/index.html', all_matches = matches)

# NEW
# GET /matches/new/
@matches_blueprint.route('/matches/new')
def new_match():
    teams = team_repository.select_all()
    return render_template("/matches/new.html", teams = teams)

# CREATE
# POST /matches/
@matches_blueprint.route('/matches', methods=['POST'])
def create_match():
    result = request.form['result']
    home_team_id = request.form['home_team']
    away_team_id = request.form['away_team']
    match = Match(home_team_id, away_team_id, result)
    match_repository.save(match)

    return redirect('/matches')

# SHOW
# GET /matches/<id>/
@matches_blueprint.route('/matches/<id>')
def show_match(id):
    match = match_repository.select(id)
    return render_template('matches/show.html', match=match)

# EDIT
# GET /matches/<id>/edit/
@matches_blueprint.route('/matches/<id>/edit')
def edit_match(id):
    match = match_repository.select(id)
    teams = team_repository.select_all()
    return render_template('matches/edit.html', match=match, teams=teams)

# UPDATE
# PUT (POST) /matches/<id>/
@matches_blueprint.route('/matches/<id>', methods=['POST'])
def update_match(id):
    home_team = request.form['home_team']
    away_team = request.form['away_team']
    result = request.form['result']
    match = match_repository.select(id)
    # home_team_id = team_repository.select(home_team)
    # away_team_id = team_repository.select(away_team)
    match = Match(home_team, away_team, result, id)
    match_repository.update(match)
    
    return redirect('/matches')

# DELETE
# DELETE (POST) /matches/<id>/delete/
@matches_blueprint.route('/matches/<id>/delete', methods=['POST'])
def delete_match(id):
    match_repository.delete(id)
    return redirect('/matches')