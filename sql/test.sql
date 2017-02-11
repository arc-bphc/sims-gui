PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME            TEXT       NOT NULL,
    EMAIL ID        TEXT       NOT NULL,
    PIN             INT        NOT NULL,
    PHONE_CALL      CHAR(10)   NOT NULL,
    PHONE_WHATSAPP  CHAR(10)   NOT NULL,
    ROOM_NO  TEXT              NOT NULL
    );
INSERT INTO "users" VALUES(1,'yashdeep','yashdeep97@gmail.com',1234,'9010712068','9665333384','BM036');
CREATE TABLE transactions(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME               TEXT    NOT NULL,
    ITEM               TEXT    NOT NULL,
    ISSUE_DATETIME     TEXT    NOT NULL,
    WITHDRAW_DATETIME  TEXT    NOT NULL,
    RETURN_DATETIME    TEXT    NULL
    );
CREATE TABLE history(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME               TEXT    NOT NULL,
    ITEM               TEXT    NOT NULL,
    ISSUE_DATETIME     TEXT    NOT NULL,
    WITHDRAW_DATETIME  TEXT    NOT NULL,
    RETURN_DATETIME    TEXT    NOT NULL
    );
INSERT INTO "history" VALUES(1,'yashdeep','RASPI','2017-02-21 12:30:12','2017-02-21 12:33:13','2017-02-21 14:50:13');
COMMIT;
