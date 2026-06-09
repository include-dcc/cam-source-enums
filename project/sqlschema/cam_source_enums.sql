-- # Class: RequiredClass Description: Required description for classes.
--     * Slot: uid
--     * Slot: id Description: Unique identifier
--     * Slot: full_name Description: Full name
--     * Slot: aliases Description: Aliases
--     * Slot: phone Description: Phone number
--     * Slot: age Description: Age

CREATE TABLE "RequiredClass" (
	uid INTEGER NOT NULL,
	id TEXT,
	full_name TEXT,
	aliases TEXT,
	phone TEXT,
	age TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_RequiredClass_uid" ON "RequiredClass" (uid);
