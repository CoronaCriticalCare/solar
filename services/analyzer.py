from datetime import datetime


def flare_strength(class_type):
    class_letter = class_type[0]
    magnitude = float(class_type[1:])

    multipliers = {
        "A": 0.0001,
        "B": 0.001,
        "C": 0.01,
        "M": 0.1,
        "X": 1.0
    }

    return multipliers[class_letter] * magnitude

def get_strongest(data):
    return max(
        data,
        key=lambda flare: flare_strength(flare["classType"])
    )

def count_classes(data):
    classes = {
        "A": 0,
        "B": 0,
        "C": 0,
        "M": 0,
        "X": 0
    }

    for flare in data:
        flare_class = flare["classType"][0]

        if flare_class in classes:
            classes[flare_class] += 1

    return classes

def count_cmes(data):
    cme_count = 0

    for flare in data:
        linked_events = flare["linkedEvents"] or []

        for event in linked_events:
            if "CME" in event["activityID"]:
                cme_count += 1

    return cme_count

def count_seps(data):
    sep_count = 0

    for flare in data:
        linked_events = flare ["linkedEvents"] or []

        for event in linked_events:
            if "SEP" in event["activityID"]:
                sep_count += 1

    return sep_count

def duration(data):
    for flare in data:
        start = datetime.fromisoformat(
            flare["beginTime"].replace("Z", "+00:00")
        )

        end = datetime.fromisoformat(
            flare["endTime"].replace("Z", "+00:00")
        )

        flare["duration"] = end - start

    longest = max(data, key=lambda flare: flare["duration"])
    shortest = min(data, key=lambda flare: flare["duration"])
    

    return longest, shortest

def average_duration(data):
    durations = []

    for flare in data:
        start = datetime.fromisoformat(
            flare["beginTime"].replace("Z", "+00:00")
        )

        end = datetime.fromisoformat(
            flare["endTime"].replace("Z", "+00:00")
        )

        durations.append((end - start).total_seconds())

    seconds = sum(durations) / len(durations)
    minutes = seconds / 60

    return minutes 

def flare_tracker(data):
    total_flares = len(data)
    strongest = get_strongest(data)
    cme_count = count_cmes(data)
    sep_count = count_seps(data)
    longest, shortest = duration(data)
    average = average_duration(data)
    classes = count_classes(data)

    print("\n" + "=" * 60)
    print("           Solar Flare Tracker")
    print("=" * 60 + "\n")
    print(f"Total Flares:               {total_flares}\n")
    print("~" * 25 + "\n")
    print(f"A-Class:    {classes['A']}\n")
    print(f"B-Class:    {classes['B']}\n")
    print(f"C-Class:    {classes['C']}\n")
    print(f"M-Class:    {classes['M']}\n")
    print(f"X-Class:    {classes['X']}\n")
    print("~" * 25 + "\n")
    print(f"Strongest Flare:            {strongest['classType']}\n")
    print(f"Longest Flare:              {longest['classType']} - {longest['duration']}\n")
    print(f"Shortest Flare:             {shortest['classType']} - {shortest['duration']}\n")
    print(f"Average duration:           {average:.2f} minutes\n")
    print(f"Total\nCoronal Mass Ejection:      {cme_count}\n")
    print(f"Total\nSolar Energy Particles:     {sep_count}\n")
    print("=" * 60 + "\n")

def analyze_flares(data):
    report = ""

    report += "\n" + "=" * 70 + "\n"
    report += "          Solar Flare Report\n"
    report += "=" * 70 + "\n"
    for flare in data:
        report += f"Flare ID:      {flare['flrID']}\n"
        report += f"Class:         {flare['classType']}\n"
        report += f"Started at     {flare['beginTime']}\n"
        report += f"Peaked at      {flare['peakTime']}\n"
        report += f"Ended at       {flare['endTime']}\n"
        report += f"Location:      {flare['sourceLocation']}\n"
        report += f"Active\nRegion:        {flare['activeRegionNum']}\n"
        report += f"Notes:         {flare['note']}\n"
        report += f"Submitted on:  {flare['submissionTime']}\n"

        if flare["linkedEvents"]:
            report += "(CME):         Yes\n"
            report += "(SEP):         Yes\n"
        else:
            report += "(CME):         No\n"
            report += "(SEP):         No\n"

        report += "-" * 70 + "\n"

    return report

    
