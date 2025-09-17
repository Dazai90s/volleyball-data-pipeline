-- cleaning_queries.sql
-- Final table creation and sample data insert for Volleyball Data Pipeline project.
-- Extracted from pgAdmin Query History (final successful run).
-- Note: Sample data shown here for demonstration purposes. Real dataset loaded from Kaggle VNL via Python.

CREATE TABLE player_stats (
    player_name TEXT,
    team TEXT,
    skill TEXT,
    success INT,
    errors INT,
    attempts INT,
    efficiency_rating FLOAT
);

INSERT INTO player_stats (player_name, team, skill, success, errors, attempts, efficiency_rating)
VALUES
('Alex', 'Dragons', 'Serve', 15, 5, 20, 0.75),
('Jordan', 'Tigers', 'Spike', 22, 8, 30, 0.733),
('Casey', 'Dragons', 'Block', 10, 2, 12, 0.833);

-- Optional: view the table
SELECT * FROM player_stats;
