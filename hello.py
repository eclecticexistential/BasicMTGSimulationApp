import sqlite3
from flask import Flask, render_template, request, redirect, flash, url_for
from db_classes import Game, provide_winner_insight
from collect_stats import initialize_open_hand, initialize_mana_starved, initialize_who_wins, initialize_draw_into_win
from dv import make_visual

app = Flask(__name__)
app.secret_key = 'some_secret'

def get_stats(info):
    open_hand_db_conn = sqlite3.connect('Open_hands.db')
    mana_starved_db_conn = sqlite3.connect('Mana_starved.db')
    who_wins_db_conn = sqlite3.connect('Who_wins.db')
    draw_into_win_db_conn = sqlite3.connect('DrawCon.db')
    initialize_open_hand()
    initialize_mana_starved()
    initialize_who_wins()
    initialize_draw_into_win()
    copyit = info
    string = copyit.split(',')
    cc = int(string[0])
    mana = int(string[1])
    num_lands = int(string[2])
    removal = int(string[3])
    life_gain = int(string[4])
    tutor = int(string[5])
    draw_cards = int(string[6])
    combat_tricks = int(string[7])
    lil = int(string[8])
    bombs = int(string[9])
    evos = int(string[10])
    stats = provide_winner_insight(Game(cc, mana, num_lands, removal, life_gain, tutor, draw_cards, combat_tricks, lil, bombs, evos))
    # make_visual(stats)
    return stats

def make_string(cc, mana):
    stats = ''
    if cc == "40":
        stats += "Limited"
    elif cc == "60":
        stats += "Standard"
    if mana == "2":
        stats += " - 2 Mana"
    elif mana == "3":
        stats += " - 3 Mana"
    return stats

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    stats = request.form['data']
    info = get_stats(stats)
    unstr = stats.split(',')
    title = make_string(unstr[0], unstr[1])
    p1 = str(round(info[0] * 100)) + '%'
    p2 = str(round(info[1] * 100)) + '%'
    play1 = str(round(info[2] * 100)) + '%'
    play2 = str(round(info[3] * 100)) + '%'
    mill = str(round(info[6] * 100)) + '%'
    mana = str(round(info[5] * 100)) + '%'
    combat = str(round(info[4] * 100)) + '%'
    wr = round(info[7])
    return render_template('results.html', stats=title, p1=p1, p2=p2, play1=play1, play2=play2, mill=mill, mana=mana, combat=combat, wr=wr)

@app.errorhandler(500)
def internal_error(error):
    flash("Required Stats Are Not Met. Click Reset to Highlight Must Have Info.")
    return redirect(url_for('index'))
	
app.run(debug=True)