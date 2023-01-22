DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS class;

CREATE TABLE class
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR                           NOT NULL
);

INSERT INTO class(name) VALUES ('10био');
INSERT INTO class(name) VALUES ('10геохим');
INSERT INTO class(name) VALUES ('10исс1');
INSERT INTO class(name) VALUES ('10исс2');
INSERT INTO class(name) VALUES ('10линг1');
INSERT INTO class(name) VALUES ('10линг2');
INSERT INTO class(name) VALUES ('10мат');
INSERT INTO class(name) VALUES ('10матэк');
INSERT INTO class(name) VALUES ('10мед');
INSERT INTO class(name) VALUES ('10фил');
INSERT INTO class(name) VALUES ('10фм');
INSERT INTO class(name) VALUES ('10эк');

INSERT INTO class(name) VALUES ('11био');
INSERT INTO class(name) VALUES ('11биохим');
INSERT INTO class(name) VALUES ('11гео');
INSERT INTO class(name) VALUES ('11исс');
INSERT INTO class(name) VALUES ('11линг1');
INSERT INTO class(name) VALUES ('11линг2');
INSERT INTO class(name) VALUES ('11мат1');
INSERT INTO class(name) VALUES ('11мат2');
INSERT INTO class(name) VALUES ('11мед');
INSERT INTO class(name) VALUES ('11фил');
INSERT INTO class(name) VALUES ('11фм');
INSERT INTO class(name) VALUES ('11эк');

INSERT INTO class(name) VALUES ('none');

CREATE TABLE user
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    telegram_id  INTEGER UNIQUE                    NOT NULL,
    username     VARCHAR,
    name         VARCHAR                           NOT NULL,
    clas_id      INTEGER,
    "group"      INTEGER,
    state        INTEGER                           NOT NULL DEFAULT 0,
    last_message VARCHAR                                    DEFAULT '2000-01-01 00:00:00.000000',
    FOREIGN KEY (clas_id) REFERENCES class (id)
);

CREATE TABLE schedule
(
    id        INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    date      VARCHAR                           NOT NULL,
    number    INTEGER                           NOT NULL,
    name      VARCHAR,
    clas_id   INTEGER                           NOT NULL,
    "group"   INTEGER                           NOT NULL,
    classroom VARCHAR,
    FOREIGN KEY (clas_id) REFERENCES class (id)
);