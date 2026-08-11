def analyze_flares(data):
    print("\n" + "=" * 70)
    print("           *Solar Flare Tracker")
    print("=" * 70)

    for flare in data:
        print(f"Flare ID:      {flare['flrID']}\n")
        print(f"Class:         {flare['classType']}\n")
        print(f"Started at     {flare['beginTime']}\n")
        print(f"Peaked at      {flare['peakTime']}\n")
        print(f"Ended at       {flare['endTime']}\n")
        print(f"Location:      {flare['sourceLocation']}")
        print(f"Active Region: {flare['activeRegionNum']}\n")
        print(f"Notes:         {flare['note']}\n")
        print(f"Submitted on:  {flare['submissionTime']}")

        if flare["linkedEvents"]:
            print("(CME):         Yes")
        else:
            print("(CME):         No")

        print("-" * 70)

