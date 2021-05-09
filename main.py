import functions
import time

f = functions
player_input = 0
ending_number = 0

f.banner_text("*")
f.banner_text("Reach for the Stars")
f.banner_text("")
f.banner_text("<Press Enter to Begin>")
f.banner_text("*")

start_pause = input()

f.banner_text("*")
f.banner_text("Basic Instructions")
f.banner_text("")
f.banner_text("You will pick the paths you want to follow in the story")
f.banner_text("You answers to the questions presented will determine the ending")
f.banner_text("Enter all answers in the chat box below")
f.banner_text("*")

time.sleep(2)

player_choices = []

f.banner_text("*", 95)
f.banner_text(" It is a warm summer day. ", 95)
f.banner_text("You are a finance major that has just graduated college and are looking for a job.", 95)
f.banner_text("You have not had much luck.", 95)
f.banner_text("Do you:", 95)
f.banner_text("", 95)
f.banner_text("1. Continue to work on your cover letter and look on an online job website afterwards.", 95)
f.banner_text("2. Go outside and meet up with some friends.", 95)
f.banner_text("*", 95)

time.sleep(1)

while (player_input != "q") and (1 not in player_choices) and (2 not in player_choices):
    print("")
    print("<Please Pick 1 or 2>")
    player_input = input()
    if player_input == "1" or player_input == "2":
        player_choices.append(int(player_input))

if 1 in player_choices:
    f.banner_text("*", 95)
    f.banner_text("You continue to work on your cover letter and notice some improvements. ", 95)
    f.banner_text("When you look at the website you see two financial advisor jobs.", 95)
    f.banner_text("One job pays higher, but seems more competitive than the lower paying job.", 95)
    f.banner_text("You see that both jobs are conducting interviews for the position on the same day. ", 95)
    f.banner_text("Do you:", 95)
    f.banner_text("", 95)
    f.banner_text("3. Apply to the higher paying job", 95)
    f.banner_text("4. Apply to the lower paying job", 95)
    f.banner_text("*", 95)
    while (player_input != "q") and (3 not in player_choices) and (4 not in player_choices):
        print("")
        print("<Pick 3 or 4>")
        player_input = input()
        if player_input == "3" or player_input == "4":
            player_choices.append(int(player_input))

if 2 in player_choices:
    f.banner_text("*", 95)
    f.banner_text("You go outside and meet up with your friend Alex.", 95)
    f.banner_text("You decided to go get ice cream at a local store.", 95)
    f.banner_text("When there you see a help wanted sign on the front door.", 95)
    f.banner_text("Do you:", 95)
    f.banner_text("", 95)
    f.banner_text("5. Ask the store owner about the sign", 95)
    f.banner_text("6. Ignore the sign and order your ice cream", 95)
    f.banner_text("*", 95)
    while (player_input != "q") and (5 not in player_choices) and (6 not in player_choices):
        print("")
        print("<Please Pick 5 or 6>")
        player_input = input()
        if player_input == "5" or player_input == "6":
            player_choices.append(int(player_input))

if 3 in player_choices:
    f.banner_text("*", 95)
    f.banner_text("As you prepare for your interview you get a call from your friend Alex.", 95)
    f.banner_text("He asks you if you want to hang out.", 95)
    f.banner_text("You are kind of nervous about your interview and don’t think that you will get the job.", 95)
    f.banner_text("Do you:", 95)
    f.banner_text("", 95)
    f.banner_text("7. Back out of the interview and hangout with Alex", 95)
    f.banner_text("8. Say no to Alex and continue to prepare for your interview", 95)
    f.banner_text("*", 95)
    while (player_input != "q") and (7 not in player_choices) and (8 not in player_choices):
        print("")
        print("<Please Pick 7 or 8>")
        player_input = input()
        if player_input == "7" or player_input == "8":
            player_choices.append(int(player_input))

if 4 in player_choices:
    f.banner_text("*", 95)
    f.banner_text("As you prepare for your interview you get a call from your friend Alex.", 95)
    f.banner_text("He asks you if you want to hang out. ", 95)
    f.banner_text("You don’t think your interview will be too hard.", 95)
    f.banner_text("Do you:", 95)
    f.banner_text("", 95)
    f.banner_text("9. Hang out with Alex", 95)
    f.banner_text("10. Say no to Alex and continue to prepare for your interview", 95)
    f.banner_text("*", 95)
    while (player_input != "q") and (9 not in player_choices) and (10 not in player_choices):
        print("")
        print("<Please Pick 9 or 10>")
        player_input = input()
        if player_input == "9" or player_input == "10":
            player_choices.append(int(player_input))

if 5 in player_choices:
    f.banner_text("*", 95)
    f.banner_text("You ask the store owner about the sign ", 95)
    f.banner_text("and he says that he is looking for someone to help manage the finance of his store.", 95)
    f.banner_text("Do you:", 95)
    f.banner_text("", 95)
    f.banner_text("11. Mention some of your qualifications and express your interest in the position", 95)
    f.banner_text("12. Nod and then go back to ordering your ice cream", 95)
    f.banner_text("*", 95)
    while (player_input != "q") and (11 not in player_choices) and (12 not in player_choices):
        print("")
        print("<Please Pick 11 or 12>")
        player_input = input()
        if player_input == "11" or player_input == "12":
            player_choices.append(int(player_input))

if 6 in player_choices:
    f.banner_text("*", 95)
    f.banner_text("You go to order ice cream and you notice a new flavor that looks good.", 95)
    f.banner_text("Do you:", 95)
    f.banner_text("", 95)
    f.banner_text("13. Try the new flavor", 95)
    f.banner_text("14. Order your regular ice cream choice", 95)
    f.banner_text("*", 95)
    while (player_input != "q") and (13 not in player_choices) and (14 not in player_choices):
        print("")
        print("<Please Pick 13 or 14>")
        player_input = input()
        if player_input == "13" or player_input == "14":
            player_choices.append(int(player_input))

print("")
if 7 in player_choices:
    f.color_print("You have fun hanging out with Alex, but afterwards the stress of finding a job returns. "
        "You start to regret not doing the interview.", f.RED)

elif 8 in player_choices:
    f.color_print("You do your interview and everything goes well. "
          "You later get an email saying you got the job. You are ecstatic.", f.GREEN)

elif 9 in player_choices:
    f.color_print("You do your interview and do relatively well, but mess up a bit. "
          "You later get an saying that you did not get the position, however, they are willing "
          "to offer you a lower paying job because they believe you have potential.", f.YELLOW)

elif 10 in player_choices:
    f.color_print("You do your interview and everything goes well. You later get an email saying you got "
          "the job.\n This success makes you wonder if you could have secured the higher paying job.", f.YELLOW)

elif 11 in player_choices:
    f.color_print("After hearing your qualification the store owner offers to interview later. "
          "Based on his expression you prospects of getting the job are high.", f.YELLOW)

elif 12 in player_choices:
    f.color_print("You continue to hangout with Alex. While you had fun you are still stressed about getting a job.",
                  f.RED)

elif 13 in player_choices:
    f.color_print("The new flavor tastes better than what you normally order. You are glad you ordered it. "
          "You enjoy the rest of the day, but when you get back home you are still stressed about securing a job.",
                  f.RED)

elif 14 in player_choices:
    f.color_print("You enjoy your ice cream and continue to hangout with Alex. "
          "While you had fun you are still stressed about getting a job.", f.RED)
elif player_input == "q":
    print("Game Ended")
