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
    id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    telegram_id   INTEGER UNIQUE                    NOT NULL,
    username      VARCHAR,
    name          VARCHAR                           NOT NULL,
    class_number  INTEGER,
    class_profile INTEGER,
    class_group   INTEGER,
    state         INTEGER                           NOT NULL DEFAULT 0,
    prev_msg_time VARCHAR                                    DEFAULT '2000-01-01 00:00:00.000000',
    FOREIGN KEY (class_profile) REFERENCES profile (id)
);

CREATE TABLE schedule
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    date          VARCHAR                           NOT NULL,
    number        INTEGER                           NOT NULL,
    name          VARCHAR,
    teacher       VARCHAR,
    class_number  INTEGER                           NOT NULL,
    class_profile INTEGER                           NOT NULL,
    class_group   INTEGER                           NOT NULL,
    classroom     VARCHAR,
    FOREIGN KEY (class_profile) REFERENCES profile (id)
);