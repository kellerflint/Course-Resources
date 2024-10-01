# EDA and Notebook Practice

## Introduction

AI is fundamentally about data. Why? 

Because at its core, that's what AI systems learn from and operate on.

Today, we'll look into understanding data through a process called Exploratory Data Analysis (EDA).

I also want you to get comfortable using AI effectively as a learning tool. Leverage the AI tools to get customized examples that relate directly to your specific tasks. This approach can help you ramp up quickly in new areas without spending hours googling and sifting through generic tutorials.

Think of it as having a friend that you can bounce questions off of. Their knowledge isn't always up to date, and they can make mistakes, but they have a passing familiarity with the subject area and can often point you in the right direction.

## Technical Work
- Create an account on Kaggle and download the following dataset: [Indicators of Heart Disease (2022 UPDATE) (kaggle.com)](https://www.kaggle.com/datasets/kamilpytlak/personal-key-indicators-of-heart-disease)
- Extract the data and find the heart_2022_with_nans.csv file. This is the data we will be working with
- You can work locally in VS Code or in Google Collab
- Import pandas and matplotlib
```python
import pandas as pd
import matplotlib.pyplot as plt
# and others if you'd like
```
- Load and display the first few rows of the dataset
- List all of the features (columns) in the dataset and total number or records
- Check for missing values. Show how many missing values are in each column
- There's more than one way to deal with missing values. Briefly investigate a few of these options. Which do you believe is most appropriate?
- Apply one of the methods of missing values
- Pick a few numerical columns and a few categorical columns. For categorical variables, create bar plots showing frequency distributions. For continuous numerical variables, create histograms. For binary variables (yes/no), create pie charts.

## Questions and Discussion
- What are the limitations of this data? What concerns might we have with it? How might these impact and AI model?
- What might be the down stream consequences of relying on an AI model trained with this data?

## Submit

At the end of class, submit your notebook (shared link if Collab, file if VS Code) to the assignment on Canvas. Your notebook should contain:
- The technical work you completed
- A markdown cell at the end with brief answers to the questions