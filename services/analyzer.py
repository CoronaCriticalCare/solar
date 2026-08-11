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

def count_cmes(data):
    cme_count = 0

    for flare in data:
        linked_events = flare["linkedEvents"] or []

        for event in linked_events:
            if "CME" in event["activityID"]:
                cme_count += 1

    return cme_count

def analyze_flares(data):
    total_flares = len(data)
    strongest = get_strongest(data)
    cme_count = count_cmes(data)

    print("\n" + "=" * 70)
    print("           Solar Flare Tracker")
    print("=" * 70)
    print(f"Total flares:               {total_flares}\n")
    print(f"Strongest flare:            {strongest['classType']}\n")
    print(f"Total\nCoronal Mass Ejection:      {cme_count}\n")
    print("=" * 70)

    for flare in data:
        print(f"Flare ID:      {flare['flrID']}\n")
        print(f"Class:         {flare['classType']}\n")
        print(f"Started at     {flare['beginTime']}\n")
        print(f"Peaked at      {flare['peakTime']}\n")
        print(f"Ended at       {flare['endTime']}\n")
        print(f"Location:      {flare['sourceLocation']}\n")
        print(f"Active\nRegion:        {flare['activeRegionNum']}\n")
        print(f"Notes:         {flare['note']}\n")
        print(f"Submitted on:  {flare['submissionTime']}")

        if flare["linkedEvents"]:
            print("(CME):         Yes")
        else:
            print("(CME):         No")

        print("-" * 70)

