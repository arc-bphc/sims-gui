#!/usr/bin/python

import sqlite3

connection = sqlite3.connect('test.db')

print "Opened database successfully"

connection.execute('''create table users(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME            TEXT       NOT NULL,
    EMAIL_ID        TEXT       NOT NULL,
    PHONE_CALL      CHAR(10)   NOT NULL,
    PHONE_WHATSAPP  CHAR(10)   NOT NULL,
    ROOM_NO         TEXT       NOT NULL,
    SALT            CHAR(5)    NULL,
    HASHED_PASSWORD CHAR(64)   NULL,
    IMAGE           BLOB       NULL
    );''')

connection.execute('''create table transactions(
    ID                 INT     NOT NULL, 
    NAME               TEXT    NOT NULL,
    ITEM_ID            INT     NOT NULL,
    QUANTITY           INT     NOT NULL,
    ISSUE_DATETIME     TEXT    NOT NULL,
    WITHDRAW_DATETIME  TEXT    NULL,
    RETURN_DATETIME    TEXT    NULL
    );''')

connection.execute('''create table history(
    ID INT PRIMARY KEY         NOT NULL, 
    NAME               TEXT    NOT NULL,
    ITEM_ID            INT     NOT NULL,
    QUANTITY           INT     NOT NULL,
    ISSUE_DATETIME     TEXT    NOT NULL,
    WITHDRAW_DATETIME  TEXT    NOT NULL,
    RETURN_DATETIME    TEXT    NOT NULL
    );''')
    
connection.execute('''create table inventory(
    ITEM_ID 	INT PRIMARY KEY     NOT NULL, 
    NAME                 TEXT       NOT NULL,
    RFID	             CHAR(12)   NOT NULL,
    SHELF_NO	         INT        NOT NULL,
    BOX_NO	             INT        NOT NULL,
    CATAGORY		     TEXT	    NOT NULL,
    QUANTITY		     INT	    NOT NULL
    );''')


connection.execute('''create table purchase(
    ID  INT PRIMARY KEY         NOT NULL, 
    NAME                TEXT    NOT NULL,
    ITEM                TEXT    NOT NULL,
    DATE                TEXT    NOT NULL,
    );''')

print "tables created successfully"

connection.close()

