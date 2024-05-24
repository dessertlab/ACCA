# Automating the Correctness Assessment of AI-generated Code for Security Contexts

This repo contains **ACCA**, a fully automated method to evaluate the correctness of AI-generated code for security purposes. The method uses symbolic execution to assess whether the AI-generated assembly code behaves as a reference implementation.

To correctly perform the evaluation, make sure to follow these steps:

# Step 0: Ground Truth and Predictions Files Setup

* Put the file containing your ground truth code snippets in the ``Ground Truth and Predictions/Ground Truth`` folder
* Put the file containing your predicted code snippets in the ``Ground Truth and Predictions/Predictions`` folder

# Step 1: Syntactic Correctness Analysis
	
* To perform the syntactic evaluation, run the command ``python syntactic_analisys.py``. The script opens up a window that lets you select the file to evaluate. 
* The results of the syntactic analysis are both shown and stored in a .csv file in the ``Output/Output_Syntactic_Analysis`` folder. In the ``Filtered Snippets`` folder you can also find the results filtered by warnings, undefined symbol errors and other errors.

# Step 2: Semantic Correctness Analysis 

* To perform the syntactic evaluation, run the command ``python semantic_analisys.py``. The script opens up a window that lets you select the file to evaluate. Make sure to select the file containing the results of the previous syntactic analysis.
* The results of the semantic analysis are both shown and stored in a .csv file in the ``Output/Output_Semantic_Analysis`` folder.