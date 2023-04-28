# Code for Chapter 7 - Explaining a PyTorch Image Classifier


|                      Section                      | Notebook              |                                                                               
| :-----------------------------------------------: | ---------------------- | 
|                 Data Preparation                  | [1.Data Preparation.ipynb](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-7%20%26%209/1.Data%20Preparation.ipynb "1.Data Preparation.ipynb")                            |
|                  Model Training                   | [2.Transfer learning-Stage_1.ipynb](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-7%20%26%209/2.Transfer%20learning-Stage_1.ipynb "2.Transfer learning-Stage_1.ipynb") |
|                                                   | [3.Transfer learning-Stage_2.ipynb](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-7/3.Transfer%20learning-Stage_2.ipynb "3.Transfer learning-Stage_2.ipynb") |     |
|   Generating Post-Hoc Explanations Using Captum   | [4.Post-Hoc Explanations.ipynb](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-7/4.Post-Hoc%20Explanations.ipynb "4.Post-Hoc Explanations.ipynb")             |     |
| Assessing the Robustness of Post-Hoc Explanations | [5.Adding Noise to images](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-7/5.Adding%20Noise%20to%20images%20.ipynb)                                          |     |
|                                                   | [6.Label Randomization](https://github.com/ml-for-high-risk-apps-book/Machine-Learning-for-High-Risk-Applications-Book/blob/main/code/Chapter-7/6.Label_Randomization.ipynb)                                                         |
---

# Code for Chapter 9 - Debugging a PyTorch Image Classifier 

This chapter focuses on model debugging techniques for Deep Learning(DL) models using our example pneumonia classifier trained in Chapter 7. We’ll start by discussing data quality and leakage issues in DL systems and why it is important to address them in the very beginning of a project. We’ll then explore some software testing methods and why software quality assurance (QA) is an essential component of debugging DL pipelines. We’ll also perform DL sensitivity analysis approaches, including testing the model on different distributions of pneumonia images and applying adversarial attacks. We’ll close the chapter by addressing our own data quality and leakage issues, discussing interesting new debugging tools for DL, and addressing the results of our own adversarial testing. 


1. Domain and Subpopulation Shift Testing
2. Adversarial Example Attacks
