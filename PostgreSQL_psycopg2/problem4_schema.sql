-- -----------------------------------------------------
-- Schema catalog
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Table catalog
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS catalog (
  bib_utility_number TEXT NOT NULL,
  title TEXT NULL,
  material_type TEXT NULL,
  record_number TEXT NULL,
  year_to_date_circ INT NULL,
  last_year_to_date_circ INT NULL,
  total_checkouts INT NULL,
  total_renewals INT NULL,
  PRIMARY KEY (bib_utility_number));
