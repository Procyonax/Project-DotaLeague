DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(255)
);

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  result VARCHAR(255),
  home_team_id INT NOT NULL REFERENCES teams(id),
  away_team_id INT NOT NULL REFERENCES teams(id)
);
