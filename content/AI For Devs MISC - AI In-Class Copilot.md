# Serving ML Models

## Learning Objectives
- Get comfortable using resources and AI tools to quickly jump into new technologies
- See how the machine learning models you develop can be used in applications

## Goal
Convert your existing linear regression model into an API-accessible service using Flask. The API should accept input data and use the regression model (either by returning the result directly or using it to make a decision). Create a simple user interface in React that calls the API.

Try to **ONLY** use AI to write code! Talking to LLMs and getting them to do exactly what you want is a bit of an art and takes time to get used to. Practice communicating and instructing it clearly to get the results you want.

## Setup
- Get GitHub Copilot. 
- Prepare your development environment with necessary libraries.

## Flask Application Development
Create a basic Flask application and implement a prediction endpoint that accepts POST requests. Ensure your endpoint can process input data and return predictions.

## React Application Development
Create a basic React application (I'd suggest using create-react-app) that collects the necessary model inputs from the user and displays the prediction.
- *If you're getting errors connecting to the API it might be CORS.*

## Enhancements
Add error handling / input validation.

## Optional Extension
If you finish this early, try adding another endpoint that hosts a pre-trained GPT-2 model and predicts words.
