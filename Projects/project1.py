import random
import sys

# Game State Variables
day = 1
max_days = 10
crew = 12
food = 120
water = 120
oxygen = 120
power = 120
health = 100
science = 0
credits = 0
AP = 3
mission_failed = False

# Main Menu Loop
while True:
    print("\n===================================")
    print("   🚀 MARS COLONY SURVIVAL 🚀     ")
    print("===================================")
    print("       Welcome Commander!          ")
    print("Humanity's future depends on you.")
    print("===================================")
    print("1. Start New Mission")
    print("2. Mission Briefing")
    print("3. How to Play")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("\nInitializing Colony...\nLoading Resources...\nCrew Arrived Successfully!")
            print("Mission Started.\n")
            break  # Break out of the menu loop to start the main game loop
        case 2:
            print("\nThe first permanent colony has been established on Mars.")
            print("You are the Mission Commander.")
            print(f"Your objective is to keep the crew alive for {max_days} Sols.")
            print("Manage resources carefully.\nGood luck, Commander\n")
        case 3:
            print("\n• You receive 3 Action Points each day.")
            print("• Food, water, and oxygen decrease daily.")
            print("• Random events happen at the end of each day.")
            print("• Keep all resources above zero.")
            print(f"• Survive until Day {max_days}.\n")
        case 4:
            print("Exiting...")
            sys.exit()
        case _:
            print("Invalid choice. Please try again.")

# Main Game Loop
while day <= max_days:
    AP = 3
    flag_AP_insufficient = False  # Flag to check if AP is insufficient for any action
    while AP > 0:
        if not flag_AP_insufficient:
            print("\n" + "="*40)
            print(f"               Day: {day}")
            print("="*40)
            print(f"Crew          : {crew}")
            print(f"Food          : {food}")
            print(f"Water         : {water}")
            print(f"Oxygen        : {oxygen}")
            print(f"Power         : {power}")
            print(f"Health        : {health}")
            print(f"Science       : {science}")
            print(f"Credits       : {credits}")
            print(f"Action Points : {AP}\n")

            print("Choose an action:")
            print("1. Explore Mars (2 AP)")
            print("2. Gather Resources (1 AP)")
            print("3. Build Colony (2 AP)")
            print("4. Repair Systems (1 AP)")
            print("5. Research (2 AP)")
            print("6. View Colony Status")
            print("7. End Day\n")
        
        choice = int(input("Enter choice: "))

        if choice < 1 or choice > 7:
            print("Invalid choice, try again.")
            continue

        # AP Validation
        if (choice == 1 or choice == 3 or choice == 5) and AP < 2:
            flag_AP_insufficient= True
            print("Not enough Action Points!")
            continue
        if (choice == 2 or choice == 4) and AP < 1:
            flag_AP_insufficient= True
            print("Not enough Action Points!")
            continue

        flag_AP_insufficient= False
        match choice:
            case 1:
                print("\n========= EXPLORE =========")
                print("1. Ice Cave")
                print("2. Crater Valley")
                print("3. Return")
                print("==========================")
                
                location = int(input("Enter location: "))

                match location:
                    case 1:
                        incident = random.randint(1, 100)
                        if 1 <= incident <= 30:
                            print("Your team drilled through a thick layer of ice.\nA hidden underground reservoir was discovered.")
                            water += 20
                        elif 31 <= incident <= 60:
                            print("Frozen Minerals found.")
                            science += 10
                        elif 61 <= incident <= 75:
                            print("Crew member slipped.")
                            health -= 10
                        elif 76 <= incident <= 90:
                            print("Ice Collapse! One crew member dies...")
                            health -= 20
                            crew -= 1
                        else:
                            print("Found Nothing..")
                            AP -= 2
                            power -= 2
                            continue # Skip the normal AP deduction below to prevent double deduction
                    case 2:
                        incident = random.randint(1, 30)
                        if incident <= 10:
                            print("Rare Crystals found.")
                            credits += 10
                            science += 10
                        elif 11 <= incident <= 20:
                            print("An unknown energy source is found.")
                            power += 10
                        else:
                            print("Evidence of ancient Martian life found.")
                            science += 20
                    case 3:
                        print("Continuing Exploration...")
                        continue
                    case _:
                        print("Invalid location.")
                        continue
                AP -= 2

            case 2:
                print("\n======= Gather Resources =======")
                print("1. Collect Ice")
                print("2. Mine Minerals")
                print("3. Harvest Solar Energy")
                print("================================")
                location = int(input("Enter Choice: "))

                if location == 1:
                    print("Large Ice Deposit found.\nWater increased by: 20")
                    water += 20
                elif location == 2:
                    print("Rare Metal Found.\nCredits increased by: 20, Science by: 10")
                    science += 10
                    credits += 20
                elif location == 3:
                    print("Harvested Solar Energy.\nPower increased by: 15")
                    power += 15
                else:
                    print("Invalid Choice.")
                    continue
                AP -= 1

            case 3:
                print("\n========= Build Colony ==========")
                print("1. Solar Power Station")
                print("2. Greenhouse")
                print("3. Water Purification Plant")
                print("=================================")
                location = int(input("Enter location: "))
                incident = random.randint(1, 100)

                match location:
                    case 1:
                        if 1 <= incident <= 60:
                            print("Construction Successful.")
                            power += 10
                        elif 61 <= incident <= 85:
                            print("Advanced Solar Panels Installed.")
                            power += 10
                            credits += 20
                        else:
                            print("Equipment Malfunction.")
                            credits -= 10
                    case 2:
                        if 1 <= incident <= 60:
                            print("Crops Growing Successfully.")
                            science += 10
                            food += 30
                        elif 61 <= incident <= 85:
                            print("High Yield Harvest.")
                            power += 10
                            credits += 10
                        else:
                            print("Plant Disease.")
                            credits -= 10
                    case 3:
                        if 1 <= incident <= 60:
                            print("Plant Operational.")
                            water += 10
                            credits += 10
                        elif 61 <= incident <= 85:
                            print("High Efficiency Filters Installed.")
                            water += 10
                            credits += 10
                        else:
                            print("Filter Blocked.\nWater Contamination!\nWater decreased by: 10")
                            water -= 10
                            credits -= 10
                            health -= 10
                    case _:
                        print("Invalid Choice.")
                        continue
                AP -= 2

            case 4:
                print("\n========= Repair Systems =========")
                print("1. Oxygen Generator")
                print("2. Solar Panel Array")
                print("3. Water Purification Plant")
                print("==================================")
                location = int(input("Enter location: "))
                incident = random.randint(1, 100)

                match location:
                    case 1:
                        if 1 <= incident <= 55:
                            print("Repair Successful.")
                            oxygen += 20
                            credits += 10
                        elif 56 <= incident <= 85:
                            print("Efficiency Upgrade Installed.")
                            oxygen += 10
                            credits += 20
                        else:
                            print("Pressure Valve Exploded.")
                            credits -= 10
                            oxygen -= 10
                            health -= 10
                    case 2:
                        if 1 <= incident <= 60:
                            print("Panels Repaired.")
                            power += 10
                            credits += 10
                        elif 61 <= incident <= 85:
                            print("High-Efficiency Cells Installed.")
                            power += 10
                            credits += 10
                        else:
                            print("Electrical Short Circuit.")
                            credits -= 10
                            power -= 15
                    case 3:
                        if 1 <= incident <= 60:
                            print("Water Purifier Repaired.")
                            water += 10
                        elif 61 <= incident <= 85:
                            print("Advanced Filters Installed.")
                            water += 10
                            credits += 10
                        else:
                            print("Contamination During Repair.\nWater decreased by: 10")
                            water -= 10
                            credits -= 10
                            health -= 10
                    case _:
                        print("Invalid Choice.")
                        continue
                AP -= 1

            case 5:
                print("\n========= Research =========")
                print("1. Analyze Strange Rock")
                print("2. Decode Alien Signal")
                print("3. Study Martian Organism")
                print("4. Investigate Energy Crystal")
                print("5. Scan Underground")
                print("============================")
                location = int(input("Enter location: "))
                incident = random.randint(1, 100)

                match location:
                    case 1:
                        if 1 <= incident <= 40:
                            print("Rare Martian Mineral Found.")
                            credits += 20
                            science += 10
                        elif 41 <= incident <= 60:
                            print("Ancient Fossil Discovered.")
                            science += 10
                            credits += 10
                        elif 61 <= incident <= 80:
                            print("Magnetic Anomaly Detected.")
                            power += 10
                        elif 81 <= incident <= 90:
                            print("Radioactive Rock.")
                            health -= 10
                        else:
                            print("Rock Explodes During Analysis.")
                            crew -= 1
                            health -= 20
                    case 2:
                        if 1 <= incident <= 40:
                            print("Signal Successfully Decoded.")
                            science += 10
                            credits += 10
                        elif 41 <= incident <= 60:
                            print("Hidden Coordinates Received.")
                            science += 10
                        elif 61 <= incident <= 80:
                            print("Signal Interference.")
                            power -= 15
                            science += 10
                        elif 81 <= incident <= 90:
                            print("Psychological Disturbance.")
                            health -= 10
                        else:
                            print("Alien Response Detected.")
                            credits += 10
                            science += 10
                    case 3:
                        if 1 <= incident <= 40:
                            print("Oxygen-Producing Organism Found.")
                            oxygen += 20
                            science += 20
                            credits += 10
                        elif 41 <= incident <= 60:
                            print("New Biological Discovery.")
                            science += 35
                            credits += 20
                        elif 61 <= incident <= 80:
                            print("Organism Communicates.")
                            science += 50
                            credits += 10
                        elif 81 <= incident <= 90:
                            print("Toxic Spores Released.")
                            health -= 15
                            science += 15
                        else:
                            print("Crew Member Infected.")
                            health -= 20
                            crew -= 1
                            science += 20
                    case 4:
                        if 1 <= incident <= 40:
                            print("Stable Energy Source.")
                            science += 10
                            power += 10
                        elif 41 <= incident <= 60:
                            print("Rare Crystal Cored.")
                            science += 10
                            credits += 20
                        elif 61 <= incident <= 80:
                            print("Unknown Energy Resonance.")
                            science += 20
                        elif 81 <= incident <= 90:
                            print("Crystal Radiation Leak.")
                            science += 10
                            health -= 10
                        else:
                            print("Energy Overload.")
                            health -= 10
                            science += 10
                    case 5:
                        if 1 <= incident <= 40:
                            print("Underground Ice Reservoir.")
                            science += 10
                            credits += 10
                            water += 10
                        elif 41 <= incident <= 60:
                            print("Underground Edible Fungi.")
                            science += 10
                            food += 20
                        elif 61 <= incident <= 80:
                            print("Massive Underground Cave.")
                            science += 10
                        elif 81 <= incident <= 90:
                            print("Seismic Activity Detected.")
                            science += 10
                            power -= 10
                        else:
                            print("Toxic Gas Pocket.")
                            health -= 10
                            oxygen -= 10
                    case _:
                        print("Invalid Choice.")
                        continue
                AP -= 2

            case 6:
                print("\n" + "="*40)
                print("           Colony Status   ")
                print("="*40)
                print(f"Day           : {day}")
                print(f"Crew          : {crew}")
                print(f"Food          : {food}")
                print(f"Water         : {water}")
                print(f"Oxygen        : {oxygen}")
                print(f"Health        : {health}")
                print(f"Power         : {power}")
                print(f"Science       : {science}")
                print(f"Credits       : {credits}\n")
                # Does not cost AP, let loop restart

            case 7:
                print("Ending the day...")
                AP = 0  # Forces the loop to break

    # End of Day Deductions
    food -= crew
    water -= crew
    oxygen -= crew
    power -= 10

    # Random Events
    event = random.randint(1, 100)
    print("\n--- Daily Report & Events ---")
    
    if 1 <= event <= 15:
        print("🤕 Crew Accident")
        print("A crew member was injured during a routine task.\nMedical supplies were used for treatment.")
        print("Health decreased by: 20\n")
        health -= 20
    elif 16 <= event <= 36:
        print("🌪️ Dust Storm")
        print("A Powerful Martian dust storm blocks sunlight.\nSolar panels are damaged.")
        print("Power decreased by: 10\n")
        power -= 10
    elif 37 <= event <= 57:
        print("☄️ Meteor Shower")
        print("Small meteor fragments struck the colony's solar panels.")
        print("Power decreased by: 10\n")
        power -= 10
    elif 58 <= event <= 68:
        print("📡 Strange Signal")
        print("Scientists detect a mysterious signal and collect valuable data.")
        print("Science increased by: 20\n")
        science += 20
    elif 69 <= event <= 80:
        print("📦 Supply Drop")
        print("A supply drop from Earth arrives with essential resources.\n")
        food += 20
        water += 10
        credits += 10
    else:
        print("☮️ Calm Sol")
        print("The colony experienced a peaceful day.\nNo unusual activity detected.\n")

    # Failure Conditions
    if food < 0 or water < 0 or oxygen < 0 or power < 0 or health < 0 or crew <= 5:
        print("\n❌ MISSION FAILED ❌")
        print("A critical resource dropped below zero, or too many crew members perished.")
        mission_failed = True
        break
        
    day += 1

# End of Game Evaluation
if not mission_failed:
    print("\n===================================")
    print("🎉 MISSION ACCOMPLISHED 🎉")
    print("===================================")
    if 100 <= credits <= 300:
        print("Result: Barely Survived.")
    elif 301 <= credits <= 500:
        print("Result: Mission Successful.")
    elif 501 <= credits <= 700:
        print("Result: Mission Successful with Good Resources.")
    elif 701 <= credits <= 850:
        print("Result: Excellent Mission!")
    else:
        print("Result: Successfully built a thriving colony on Mars!")
        
    print("\nFinal Stats:")
    print(f"Crew: {crew} | Food: {food} | Water: {water} | Oxygen: {oxygen}")
    print(f"Power: {power} | Health: {health} | Science: {science} | Credits: {credits}")