DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS profile;

CREATE TABLE profile
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR                           NOT NULL
);

INSERT INTO profile(name)
VALUES ('био');
INSERT INTO profile(name)
VALUES ('геохим');
INSERT INTO profile(name)
VALUES ('исс1');
INSERT INTO profile(name)
VALUES ('исс2');
INSERT INTO profile(name)
VALUES ('линг1');
INSERT INTO profile(name)
VALUES ('линг2');
INSERT INTO profile(name)
VALUES ('мат');
INSERT INTO profile(name)
VALUES ('матэк');
INSERT INTO profile(name)
VALUES ('мед');
INSERT INTO profile(name)
VALUES ('фил');
INSERT INTO profile(name)
VALUES ('фм');
INSERT INTO profile(name)
VALUES ('эк');

INSERT INTO profile(name)
VALUES ('биохим');
INSERT INTO profile(name)
VALUES ('гео');
INSERT INTO profile(name)
VALUES ('исс');
INSERT INTO profile(name)
VALUES ('мат1');
INSERT INTO profile(name)
VALUES ('мат2');

CREATE TABLE user
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    telegram_id  INTEGER UNIQUE                    NOT NULL,
    username     VARCHAR,
    name         VARCHAR                           NOT NULL,
    clas_number  INTEGER,
    profile_id   INTEGER,
    teacher      VARCHAR,
    "group"      INTEGER,
    state        INTEGER                           NOT NULL DEFAULT 0,
    last_message VARCHAR                                    DEFAULT '2000-01-01 00:00:00.000000',
    FOREIGN KEY (profile_id) REFERENCES profile (id)
);

CREATE TABLE schedule
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    date        VARCHAR                           NOT NULL,
    number      INTEGER                           NOT NULL,
    name        VARCHAR,
    teacher     VARCHAR,
    clas_number INTEGER                           NOT NULL,
    profile_id  INTEGER                           NOT NULL,
    "group"     INTEGER                           NOT NULL,
    classroom   VARCHAR,
    FOREIGN KEY (profile_id) REFERENCES profile (id)
);