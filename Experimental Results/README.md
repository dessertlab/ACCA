# Automating the Correctness Assessment of AI-generated Code for Security Contexts

This folder contains the results we obtained during our empirical analysis. 
To reduce the possibility of errors in the manual analysis, multiple authors discussed cases of discrepancy, obtaining a consensus for all the evaluation results. 

For each of the five AI models encompassed in our analysis, i.e., Seq2Seq, CodeBERT, CodeT5+, PLBart and ChatGPT-3.5, we report:

- The set of natural language (NL) intents used as inputs for the AI code generation models;
- The set of ground truth code snippets, i.e., a reference implementation used for comparison;
- The set of code snippets predicted by the AI code generation models;
- The *human evaluation* score for each prediction;
- The *compilation accuracy* score for each prediction;
- The *BLEU-4* score for each prediction;
- The *SacreBLEU* score for each prediction;
- The *Edit Distance* score for each prediction;
- The *Exact Match* score for each prediction;
- The *ChatGPT-NL* score for each prediction, i.e., when ChatGPT evaluates if the generated code is the correct translation in assembly code of the NL intent;
- The *ChatGPT-GT* score for each prediction, i.e., when ChatGPT evaluates if the generated code is semantically equivalent to the ground truth code;
- The *ACCA* score for each prediction.