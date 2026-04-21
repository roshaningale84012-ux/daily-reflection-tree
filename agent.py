##Python


def daily_reflection():
    task_done = input("Did you complete your main task? (yes/no): ").lower()

    if task_done == "yes":
        feeling = input("How do you feel? (good/tired): ").lower()

        if feeling == "good":
            return "Maintain current strategy and continue momentum."
        elif feeling == "tired":
            return "Take rest and plan lighter tasks tomorrow."
        else:
            return "Invalid input."

    elif task_done == "no":
        reason = input("Reason? (time/motivation/distraction/difficult): ").lower()

        if reason == "time":
            return "Improve scheduling and prioritize key tasks."
        elif reason == "motivation":
            return "Break tasks into smaller parts."
        elif reason == "distraction":
            return "Identify and eliminate distractions."
        elif reason == "difficult":
            return "Seek help or simplify the task."
        else:
            return "Invalid input."

    else:
        return "Invalid input."


if __name__ == "__main__":
    result = daily_reflection()
    print("\n💡 Suggestion:", result)
