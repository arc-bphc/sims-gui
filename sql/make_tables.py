#!/usr/bin/python

import sqlite3

connection = sqlite3.connect('test.db')

print "Opened database successfully"

connection.execute('''create table users(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME            TEXT       NOT NULL,
    EMAIL ID        TEXT       NOT NULL,
    PIN             INT        NOT NULL,
    PHONE_CALL      CHAR(10)   NOT NULL,
    PHONE_WHATSAPP  CHAR(10)   NOT NULL,
    ROOM_NO  TEXT              NOT NULL
    );''')

connection.execute('''create table transactions(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME               TEXT    NOT NULL,
    ITEM               TEXT    NOT NULL,
    ISSUE_DATETIME     TEXT    NOT NULL,
    WITHDRAW_DATETIME  TEXT    NOT NULL,
    RETURN_DATETIME    TEXT    NULL
    );''')

connection.execute('''create table history(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME               TEXT    NOT NULL,
    ITEM               TEXT    NOT NULL,
    ISSUE_DATETIME     TEXT    NOT NULL,
    WITHDRAW_DATETIME  TEXT    NOT NULL,
    RETURN_DATETIME    TEXT    NOT NULL
    );''')

print "tables created successfully"

connection.close()

