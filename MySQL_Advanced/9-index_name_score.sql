-- Smae as 8 but with scores added
CREATE INDEX idx_name_first_score ON names(name(1), score);