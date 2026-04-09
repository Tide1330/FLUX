import csv 
import numpy as np
import pandas as pd
import ollama as ollama
import re
import time


dataraw = pd.read_csv('youtube_comments.csv', on_bad_lines = 'warn', header = None)
mask = dataraw.apply(lambda row: len(''.join(row.fillna('').astype(str))), axis=1) > 2
datacleaned = dataraw.to_numpy(dtype=object)
datacleaned = dataraw[mask].drop(dataraw.columns[0], axis=1)
datacleaned = datacleaned.to_numpy(dtype = object)


def ai_detect(comment):
    response = ollama.chat(model='gemma3:1b', messages=[
        {
            'role': 'system',
            'content': 'You are a sentiment analyzer trying to figure out the audiences responses for the movie based on this trailer. Respond with only one of these NUMBERS: Positive: 1, Negative: -1, or Neutral: 0.'
        },
        {
            'role': 'user',
            'content': f"Analyze this Comment: {comment}",
        },
    ])
    ai_text = str(response['message']['content'])
    match = re.search(r'(-1|0|1)', ai_text)
    if match:
        return match.group(0)
    else:
        return 0

start_time = time.time()

spef_movie = datacleaned[:, 0] == 'Avengers Endgame Trailer'
indices = np.where(spef_movie)[0]
total_sentiment = 0

for idx in indices:
    try:
        comment = str(datacleaned[idx, 1])
        sentiment = ai_detect(comment)
        datacleaned[idx, 1] = sentiment
        
        total_sentiment += float(sentiment)
        
        print(f"Processed index {idx} | Sentiment: {sentiment}")
        
    except Exception as e:
        print(f"Error processing index {idx}: {e}")
        datacleaned[idx, 1] = 0
        continue

end_time = time.time()
average = total_sentiment / len(indices)

print(f"---")
print(f"Processing completed in {(end_time - start_time)/60:.2f} minutes")
print(f"Average score: {average:.4f}")









