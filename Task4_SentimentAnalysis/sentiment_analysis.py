import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon
nltk.download("vader_lexicon")

# Load dataset
df = pd.read_csv("reviews.csv")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Calculate sentiment scores
df["Sentiment_Score"] = df["Review"].apply(
    lambda review: sia.polarity_scores(str(review))["compound"]
)

# Classify sentiments
def classify_sentiment(score):
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df["Sentiment"] = df["Sentiment_Score"].apply(classify_sentiment)

# Save analyzed results
df.to_csv("sentiment_results.csv", index=False)

# Display results
print("\n========== SENTIMENT ANALYSIS RESULTS ==========")
print(df[["Review", "Sentiment", "Sentiment_Score"]].to_string(index=False))

# Sentiment counts
sentiment_counts = df["Sentiment"].value_counts()

print("\n========== SENTIMENT SUMMARY ==========")
print(sentiment_counts)

# Set visualization style
sns.set_theme(style="whitegrid")

# 1. Sentiment Distribution Bar Chart
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Sentiment", order=["Positive", "Neutral", "Negative"])
plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("sentiment_distribution.png")
plt.close()

# 2. Sentiment Distribution Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    sentiment_counts.values,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Customer Sentiment Percentage")
plt.tight_layout()
plt.savefig("sentiment_percentage.png")
plt.close()

# 3. Sentiment Score Distribution
plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="Sentiment_Score", bins=10, kde=True)
plt.title("Distribution of Sentiment Scores")
plt.xlabel("Sentiment Score")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.savefig("sentiment_score_distribution.png")
plt.close()

print("\nAll sentiment charts generated successfully!")
print("Analyzed results saved in sentiment_results.csv")