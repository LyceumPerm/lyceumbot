DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS schedule;
DROP TABLE IF EXISTS profile;
DROP TABLE IF EXISTS teacher;



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


CREATE TABLE teacher
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name VARCHAR                           NOT NULL
);

INSERT INTO teacher(name) VALUES ('Альянаки С.И.');
INSERT INTO teacher(name) VALUES ('Басманова А.С.');
INSERT INTO teacher(name) VALUES ('Баталова Л.Г.');
INSERT INTO teacher(name) VALUES ('Бежина И.Н.');
INSERT INTO teacher(name) VALUES ('Бушин В.Н.');
INSERT INTO teacher(name) VALUES ('Быстрова Н.Я.');
INSERT INTO teacher(name) VALUES ('Вавилин А.С.');
INSERT INTO teacher(name) VALUES ('Веревкина И.Н.');
INSERT INTO teacher(name) VALUES ('Гачегова Л.В.');
INSERT INTO teacher(name) VALUES ('Гашева Л.И.');
INSERT INTO teacher(name) VALUES ('Демидова М.И.');
INSERT INTO teacher(name) VALUES ('Жувак И.В.');
INSERT INTO teacher(name) VALUES ('Журавлева Л.С.');
INSERT INTO teacher(name) VALUES ('Загребина Г.Е.');
INSERT INTO teacher(name) VALUES ('Зотина И.М.');
INSERT INTO teacher(name) VALUES ('Иванов С.В.');
INSERT INTO teacher(name) VALUES ('Ильина Н.С.');
INSERT INTO teacher(name) VALUES ('Каменских О.В.');
INSERT INTO teacher(name) VALUES ('Комаров В.А.');
INSERT INTO teacher(name) VALUES ('Конев А.И.');
INSERT INTO teacher(name) VALUES ('Коровина К.С.');
INSERT INTO teacher(name) VALUES ('Кощеева А.Н.');
INSERT INTO teacher(name) VALUES ('Князева Е.А.');
INSERT INTO teacher(name) VALUES ('Мартилова Н.Л.');
INSERT INTO teacher(name) VALUES ('Мартынова М.Н.');
INSERT INTO teacher(name) VALUES ('Микрюков Д.А.');
INSERT INTO teacher(name) VALUES ('Нагорнюк О.И.');
INSERT INTO teacher(name) VALUES ('Некрасов О.О.');
INSERT INTO teacher(name) VALUES ('Осташова Е.В.');
INSERT INTO teacher(name) VALUES ('Панова Е.А.');
INSERT INTO teacher(name) VALUES ('Поварницына Е.С.');
INSERT INTO teacher(name) VALUES ('Полушкина М.А.');
INSERT INTO teacher(name) VALUES ('Радаева О.С.');
INSERT INTO teacher(name) VALUES ('Ракина Е.А.');
INSERT INTO teacher(name) VALUES ('Ромодина Т.П.');
INSERT INTO teacher(name) VALUES ('Соболева Т.И.');
INSERT INTO teacher(name) VALUES ('Сонинский П.Г.');
INSERT INTO teacher(name) VALUES ('Сорокина А.В.');
INSERT INTO teacher(name) VALUES ('Сутоцкая М.Ю.');
INSERT INTO teacher(name) VALUES ('Филенко А.Е.');
INSERT INTO teacher(name) VALUES ('Филенко Д.А.');
INSERT INTO teacher(name) VALUES ('Фомичева Н.В.');
INSERT INTO teacher(name) VALUES ('Чепурин А.В.');
INSERT INTO teacher(name) VALUES ('Чернышев А.Ю.');
INSERT INTO teacher(name) VALUES ('Чигодайкина Е.В.');
INSERT INTO teacher(name) VALUES ('Чугунова О.О.');




CREATE TABLE user
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    telegram_id  INTEGER UNIQUE                    NOT NULL,
    username     VARCHAR,
    name         VARCHAR                           NOT NULL,
    clas_number  INTEGER,
    profile_id   INTEGER,
    "group"      INTEGER,
    teacher_id   INTEGER,
    state        INTEGER                           NOT NULL DEFAULT 0,
    last_message VARCHAR                                    DEFAULT '2000-01-01 00:00:00.000000',
    FOREIGN KEY (profile_id) REFERENCES profile (id),
    FOREIGN KEY (teacher_id) REFERENCES teacher (id)
);



CREATE TABLE schedule
(
    id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    date        VARCHAR                           NOT NULL,
    number      INTEGER                           NOT NULL,
    name        VARCHAR,
    teacher_id  INTEGER,
    clas_number INTEGER                           NOT NULL,
    profile_id  INTEGER                           NOT NULL,
    "group"     INTEGER                           NOT NULL,
    classroom   VARCHAR,
    FOREIGN KEY (profile_id) REFERENCES profile (id),
    FOREIGN KEY (teacher_id) REFERENCES teacher (id)
);