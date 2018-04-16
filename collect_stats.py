import sqlite3

open_hand_db_conn = sqlite3.connect('Open_hands.db')


def initialize_open_hand():
    open_hand_db_conn.execute("DROP TABLE IF EXISTS Open_hands")
    open_hand_db_conn.commit()
    try:
        open_hand_db_conn.execute(
            "CREATE TABLE Open_hands(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Player TEXT NOT NULL, Hand INTEGER NOT NULL);")
        open_hand_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_open_hand_db(mana, game, player, hand):
    open_hand_db_conn.execute("INSERT INTO Open_hands (Mana, Game, Player, Hand) VALUES ('" + str(mana) + "', '"
                              + str(game) + "', '" + str(player) + "', '" + str(hand) + "')")


def get_open_hand_stats():
    open_hand_cursor = open_hand_db_conn.cursor()
    try:
        result = open_hand_cursor.execute("SELECT Mana, Game, Player, Hand FROM Open_hands")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


first_blood_db_conn = sqlite3.connect('First_blood.db')


def initialize_first_blood():
    first_blood_db_conn.execute("DROP TABLE IF EXISTS First_blood")
    first_blood_db_conn.commit()
    try:
        first_blood_db_conn.execute(
            "CREATE TABLE First_blood(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Round INTEGER NOT NULL, Player TEXT NOT NULL, Method TEXT NOT NULL, "
            "GoesFirst INTEGER NOT NULL);")
        first_blood_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_first_blood_db(mana, game, round, player, method, goesfirst):
    first_blood_db_conn.execute("INSERT INTO First_blood (Mana, Game, Round, Player, Method, GoesFirst) VALUES ('"
                                  + str(mana) + "', '" + str(game) + "', '" + str(round) + "', '" + str(player)
                                  + "', '" + str(method) + "', '" + str(goesfirst) + "')")


def get_first_blood_stats():
    cursor = first_blood_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Round, Player, Method, GoesFirst FROM First_blood")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


mana_starved_db_conn = sqlite3.connect('Mana_starved.db')


def initialize_mana_starved():
    mana_starved_db_conn.execute("DROP TABLE IF EXISTS Mana_starved")
    mana_starved_db_conn.commit()
    try:
        mana_starved_db_conn.execute(
            "CREATE TABLE Mana_starved(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Round INTEGER NOT NULL, Player TEXT NOT NULL, GoesFirst TEXT NOT NULL);")
        mana_starved_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_mana_starved_db(mana, game, round, player, goesfirst):
    mana_starved_db_conn.execute("INSERT INTO Mana_starved (Mana, Game, Round, Player, GoesFirst) VALUES ('"
                                 + str(mana) + "', '" + str(game) + "', '" + str(round)
                                 + "', '" + str(player) + "', '" + str(goesfirst) + "')")


def get_mana_starved_stats():
    cursor = mana_starved_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Round, Player, GoesFirst FROM Mana_starved")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


who_wins_db_conn = sqlite3.connect('Who_wins.db')

def initialize_who_wins():
    who_wins_db_conn.execute("DROP TABLE IF EXISTS Who_wins")
    who_wins_db_conn.commit()
    try:
        who_wins_db_conn.execute(
            "CREATE TABLE Who_wins(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Round INTEGER NOT NULL, Player TEXT NOT NULL, Method TEXT NOT NULL, "
            "GoesFirst TEXT NOT NULL);")
        who_wins_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_who_wins_db(mana, game, rounds, player, method, goes_first):
    who_wins_db_conn.execute("INSERT INTO Who_wins (Mana, Game, Round, Player, Method, GoesFirst) VALUES ('"
                             + str(mana) + "', '" + str(game) + "', '" + str(rounds)
                             + "', '" + str(player) + "', '" + str(method) + "', '" + str(goes_first) + "')")


def get_who_wins_stats():
    cursor = who_wins_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Round, Player, Method, GoesFirst FROM Who_wins")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


draw_into_win_db_conn = sqlite3.connect('DrawCon.db')


def initialize_draw_into_win():
    draw_into_win_db_conn.execute("DROP TABLE IF EXISTS DrawCon")
    draw_into_win_db_conn.commit()
    try:
        draw_into_win_db_conn.execute(
            "CREATE TABLE DrawCon(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, EvoDraw INTEGER NOT NULL, "
            "NonEvo INTEGER NOT NULL);")
        draw_into_win_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_draw_into_win_db(evo_draw, non_evo_draw):
    draw_into_win_db_conn.execute("INSERT INTO DrawCon (EvoDraw, NonEvo) VALUES ('"
                             + str(evo_draw) + "', '" + str(non_evo_draw) + "')")


def get_draw_into_win_stats():
    cursor = draw_into_win_db_conn.cursor()
    try:
        result = cursor.execute("SELECT EvoDraw, NonEvo FROM DrawCon")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


initialize_open_hand()
initialize_first_blood()
initialize_mana_starved()
initialize_who_wins()
initialize_draw_into_win()


def game_stats(rounds, player, mana, game, hand=None, method=None, winner=None, goes_first=None):
    if hand is not None and method is None:
        insert_into_open_hand_db(mana, game, player, hand)
    if method and winner is None:
        insert_into_first_blood_db(mana, game, rounds, player, method, goes_first)
    # if winner and method is "NoManaHand":
    #     no_mana_hand.append([mana, game, rounds, player, goes_first])
    if winner and method is "ManaStarved":
        insert_into_mana_starved_db(mana, game, rounds, player, goes_first)
    # if winner and method is "Milled":
    #     milled_stats.append([mana, game, rounds, player, goes_first])
    # if winner and method is "Combat":
    #     death_by_combat.append([mana, game, rounds, player, goes_first])
    if method and winner:
        insert_into_who_wins_db(mana, game, rounds, player, method, goes_first)
