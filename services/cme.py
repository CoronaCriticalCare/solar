import multiprocessing

from services.analyzer import *
from api.nasa import *
from data.report_screen import show_cme_report


def start_cme():
    data = get_cme()
    report = cme_report(data)
    process = multiprocessing.Process(
        target=show_cme_report,
        args=(report,)
    )
    process.start()

def cme_report(data):
    report = ""

    report += "\n" + "=" * 70 + "\n"
    report += "                       Coronal Mass Ejection Report\n"
    report += "=" * 70 + "\n"
    for cme in data:
        report += f"CME ID:               {cme['activityID']}\n"
        report += f"Catalog:              {cme['catalog']}\n"
        report += f"Start time:           {cme['startTime']}\n"
        report += f"Instruments used:     {cme['instruments']}\n"
        report += f"Active\nRegion:               {cme['activeRegionNum']}\n"
        report += f"Note:                 {cme['note']}\n"
        report += f"Submission Time:      {cme['submissionTime']}\n"
        
        report += f"Linked Events:        {cme['linkedEvents']}\n"
        report += f"Notifications:        {cme['sentNotifications']}\n"

        if cme["cmeAnalyses"]:
            report += "(Analysis):           Yes\n"
        else:
            report += "(Analysis):           No\n"

        report += "-" * 70 + "\n"

    return report