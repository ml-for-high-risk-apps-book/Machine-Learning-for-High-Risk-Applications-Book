# Code for Chapter 10 -  Testing and Remediating Bias with XGBoost

This chapter focuses on technical implementations of bias testing and remediation approaches. We’ll start off by training XGBoost on a variant of the credit card data. We’ll then test for bias by checking for differences in performance and outcomes across demographic groups. We’ll additionally try and identify any bias concerns at the individual observation level. Once we confirm the existence of measurable levels of bias in our model predictions, we’ll start trying to fix, or remediate, that bias. We employ pre-, in- and post-processing remediation methods that attempt to fix the training data, model, and outcomes, respectively. We’ll finish off the chapter by conducting bias-aware model selection that leaves us with a model that is both performant and minimally biased.

# Code

1. Testing and Remediating Bias in an XGBoost Credit Model [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1STUuI9pnzZ0XZbcBYKvk2l52L2904RYO?usp=sharing)   [![Open In GitHub](https://img.shields.io/badge/Github-code-green)](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-10/Testing_and_Remediating_Bias_constrained.ipynb)
