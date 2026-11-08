# CodeAlpha Sentiment Analysis Project

## Project Overview
This project analyzes customer reviews using Natural Language Processing (NLP) techniques. It classifies customer opinions into three categories: Positive, Negative, and Neutral.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- NLTK
- VADER Sentiment Analyzer

## Dataset
The project uses `reviews.csv`, containing 24 sample customer reviews.

## Methodology
1. Load customer reviews from the CSV dataset.
2. Use NLTK VADER to calculate sentiment scores.
3. Classify reviews based on compound scores:
   - Positive: Score greater than or equal to 0.05
   - Negative: Score less than or equal to -0.05
   - Neutral: Score between -0.05 and 0.05
4. Save the classified results into a CSV file.
5. Generate charts to visualize customer opinions.

## Sentiment Analysis Results

| Sentiment | Number of Reviews |
|---|---:|
| Positive | 10 |
| Negative | 10 |
| Neutral | 4 |
| **Total** | **24** |

## Visualizations

### 1. Sentiment Distribution
Bar chart showing the number of Positive, Negative, and Neutral reviews.

### 2. Sentiment Percentage
Pie chart showing the percentage distribution of customer sentiments.

### 3. Sentiment Score Distribution
Histogram showing the distribution of sentiment scores.

## Project Files
- `reviews.csv` – Customer reviews dataset
- `sentiment_analysis.py` – Python source code
- `sentiment_results.csv` – Classified sentiment results
- `sentiment_distribution.png` – Sentiment bar chart
- `sentiment_percentage.png` – Sentiment pie chart
- `sentiment_score_distribution.png` – Sentiment score histogram
- `README.md` – Project documentation

## How to Run the Project

Install the required libraries:

```bash
pip install pandas matplotlib seaborn nltk
```

Run the Python script:

```bash
python sentiment_analysis.py
```

## Limitations
VADER is a lexicon-based sentiment analyzer. It may sometimes misclassify complex sentences, sarcasm, or phrases whose meaning depends on context.

## Conclusion
This project helps understand customer opinions through sentiment classification. The results can support businesses in identifying customer satisfaction and dissatisfaction.