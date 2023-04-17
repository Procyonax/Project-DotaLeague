DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
  id SERIAL PRIMARY KEY,
  team_name VARCHAR(255)
);

CREATE TABLE matches (
  id SERIAL PRIMARY KEY,
  home_team_id VARCHAR(255) NOT NULL,
  away_team_id VARCHAR(255) NOT NULL,
  -- home_team_id INT NOT NULL REFERENCES teams(id),
  -- away_team_id INT NOT NULL REFERENCES teams(id),
  result VARCHAR(255)
);
