import random
from time import sleep

def tally_marks(number):
    return '|' * number

def toss():
    print("\n🏏 Toss Time!")
    choice = input("Choose Odd or Even: ").strip().lower()
    player_roll = int(input("🎲 Roll a number (1-10): "))
    comp_roll = random.randint(1, 10)
    print(f"🤖 Computer rolled: {comp_roll}")
    result = (player_roll + comp_roll) % 2
    
    if (result == 0 and choice == "even") or (result != 0 and choice == "odd"):
        print("✅ You won the toss!")
        return True
    else:
        print("❌ Computer won the toss!")
        return False

def play_innings(player_batting):
    print("\n" + "=" * 40)
    print("🏏 Innings Begins!")
    print("=" * 40)
    strikes = 0
    score = 0
    
    while strikes < 3:
        player_roll = int(input("\n🎲 Roll your fingers (1-10): "))
        comp_roll = random.randint(1, 10)
        print(f"🤖 Computer rolled: {comp_roll} ({tally_marks(comp_roll)})")
        sleep(1)
        
        if abs(player_roll - comp_roll) == 1:
            strikes += 1
            print(f"⚠️ Strike {strikes}/3! Be careful!")
        elif player_roll == comp_roll:
            score += 2 * player_roll
            print(f"🎯 Same roll! Score doubled! Total: {score}")
        else:
            runs = player_roll if player_batting else comp_roll
            score += runs
            print(f"🏏 Runs added! Current {'your' if player_batting else 'computer'} score: {score}")
    
    print("❌ Out! Innings over.")
    return score

def hand_cricket():
    player_won_toss = toss()
    
    if player_won_toss:
        choice = input("Do you want to Bat or Bowl? ").strip().lower()
        player_bats = choice == "bat"
    else:
        player_bats = random.choice([True, False])
        print("🤖 Computer chose to", "Bat" if player_bats else "Bowl")
    
    print("\n🏏 First Innings")
    first_score = play_innings(player_bats)
    print(f"\n🔹 First innings total: {first_score}")
    
    print("\n🏏 Second Innings")
    second_score = play_innings(not player_bats)
    print(f"\n🔹 Second innings total: {second_score}")
    
    print("\n🏆 Match Result")
    print("=" * 40)
    if first_score > second_score:
        winner = "You" if player_bats else "Computer"
        print(f"🎉 {winner} won the match!")
    elif second_score > first_score:
        winner = "Computer" if player_bats else "You"
        print(f"🎉 {winner} won the match!")
    else:
        print("🤝 It's a tie!")
    print("=" * 40)

hand_cricket()
