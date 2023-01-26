DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS class;

CREATE TABLE class
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR                           NOT NULL
);

INSERT INTO class(name)
VALUES ('био');
INSERT INTO class(name)
VALUES ('геохим');
INSERT INTO class(name)
VALUES ('исс1');
INSERT INTO class(name)
VALUES ('исс2');
INSERT INTO class(name)
VALUES ('линг1');
INSERT INTO class(name)
VALUES ('линг2');
INSERT INTO class(name)
VALUES ('мат');
INSERT INTO class(name)
VALUES ('матэк');
INSERT INTO class(name)
VALUES ('мед');
INSERT INTO class(name)
VALUES ('фил');
INSERT INTO class(name)
VALUES ('фм');
INSERT INTO class(name)
VALUES ('эк');

INSERT INTO class(name)
VALUES ('био');
INSERT INTO class(name)
VALUES ('биохим');
INSERT INTO class(name)
VALUES ('гео');
INSERT INTO class(name)
VALUES ('исс');
INSERT INTO class(name)
VALUES ('линг1');
INSERT INTO class(name)
VALUES ('линг2');
INSERT INTO class(name)
VALUES ('мат1');
INSERT INTO class(name)
VALUES ('мат2');
INSERT INTO class(name)
VALUES ('мед');
INSERT INTO class(name)
VALUES ('фил');
INSERT INTO class(name)
VALUES ('фм');
INSERT INTO class(name)
VALUES ('эк');

INSERT INTO class(name)
VALUES ('none');

CREATE TABLE user
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    telegram_id  INTEGER UNIQUE                    NOT NULL,
    username     VARCHAR,
    name         VARCHAR                           NOT NULL,
    clas_number  INTEGER,
    clas_id      INTEGER,
    "group"      INTEGER,
    state        INTEGER                           NOT NULL DEFAULT 0,
    last_message VARCHAR                                    DEFAULT '2000-01-01 00:00:00.000000',
    FOREIGN KEY (clas_id) REFERENCES class (id)
);

CREATE TABLE schedule
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    date        VARCHAR                           NOT NULL,
    number      INTEGER                           NOT NULL,
    name        VARCHAR,
    teacher     VARCHAR,
    clas_number INTEGER                           NOT NULL,
    clas_id     INTEGER                           NOT NULL,
    "group"     INTEGER                           NOT NULL,
    classroom   VARCHAR,
    FOREIGN KEY (clas_id) REFERENCES class (id)
);