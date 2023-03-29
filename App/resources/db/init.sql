DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS profile;

CREATE TABLE profile
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR                           NOT NULL
);

CREATE TABLE user
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    telegram_id  INTEGER UNIQUE                    NOT NULL,
    username     VARCHAR,
    name         VARCHAR                           NOT NULL,
    clas_number  INTEGER,
    profile_id   INTEGER,
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