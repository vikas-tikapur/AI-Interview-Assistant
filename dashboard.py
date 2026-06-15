import pandas as pd

def get_dashboard_stats():

    csv_file = "results/interview_results.csv"

    try:

        df = pd.read_csv(csv_file)

        total_interviews = len(df)

        average_score = round(
            df["Score"].mean(),
            2
        )

        highest_score = df["Score"].max()

        lowest_score = df["Score"].min()

        return {
            "total": total_interviews,
            "average": average_score,
            "highest": highest_score,
            "lowest": lowest_score
        }

    except:

        return {
            "total": 0,
            "average": 0,
            "highest": 0,
            "lowest": 0
        }