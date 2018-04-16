import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

def make_visual(nums):
    a, b, c, d, e, f, g, h = nums
    turn_labels = "Player 1 Evo", "Player 2 Non-Evo"
    turn_size = [a,b]
    goes_labels = "Wins Playing 1st", "Wins Playing 2nd"
    goes_size = [c,d]
    method_labels = "Mill Wins", "No Mana Wins", "Combat Wins"
    method_size = [g, f, e]
    fig1, ax1 = plt.subplots()
    ax1.pie(turn_size, labels=turn_labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.savefig("static/graph.png")
    fig2, ax2 = plt.subplots()
    ax2.pie(goes_size, labels=goes_labels, autopct='%1.1f%%', startangle=90)
    ax2.axis('equal')
    plt.savefig("static/goes.png")
    fig3, ax3 = plt.subplots()
    ax3.pie(method_size, labels=method_labels, autopct='%1.1f%%', startangle=90)
    ax3.axis('equal')
    plt.savefig("static/method.png")


# make_visual([0.50, 0.50, 0.4, 0.6, 0.43, 0.3, 0.27, 14.511904761904763])
