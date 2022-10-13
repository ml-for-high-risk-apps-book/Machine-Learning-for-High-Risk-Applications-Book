# Code for Chapter 11 -  Red-teaming XGBoost

In this chapter, we’ll show you how to hack your own models so that you can add red-teaming into to your model debugging repertoire. The main idea of the chapter is when you know what
hackers will try to do to your model, then you can try it out first and devise effective defenses. We’ll start out with a concept refresher that reintroduces common ML
attacks and countermeasures, then we’ll dive into examples of attacking an XGBoost classifier trained on structured data. We’ll then introduce two XGBoost models, one trained with the
standard black-box approach, and one trained with constraints and a high degree of L2 regularization. We’ll use these two models to explain the attacks and to test
whether transparency and L2 regularization are adequate countermeasures. After that, we’ll jump into attacks that are likely to be performed by external adversaries
against a black-box ML API: model extraction and adversarial example attacks. From there, we’ll try out insider attacks that involve making deliberate changes to an ML
modeling pipeline: data poisoning and model backdoors.

# Code

1. Training an Overfit and a Constrained XGBoost model [![Open In Colab](https://colab.research.google.com/drive/1_76P6hvYY5tHdD8pPswMeNP_VrhAnh5y?usp=sharing)     [![Open In GitHub](https://img.shields.io/badge/Github-code-green)](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-6/GLM%2CGAM%20and%20EBM_code_example.ipynb)
