import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort scores in descending order
    sorted_scores = scores.sort_values(by='score', ascending=False).reset_index(drop=True)

    # Initialize rank and previous score
    rank = 0
    prev_score = None

    # Calculate rank for each score
    ranks = []
    for score in sorted_scores['score']:
        if score != prev_score:
            prev_score = score
            rank += 1
        ranks.append(rank)

    # Add rank to DataFrame
    sorted_scores['rank'] = ranks

    return sorted_scores[["score","rank"]]