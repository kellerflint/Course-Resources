# M2 - Applications of AI
## Learning Objectives
*These topics will be covered in this module's knowledge check and entry ticket.*
- Understand the types of common tasks in AI (no need to memorize the techniques, just make sure to understand the task categories and kinds of data / scenarios they deal with).
- Understand the differences in approach between Supervised Learning, Unsupervised Learning, Reinforcement Learning, and Evolutionary Learning.
- Understand traditional machine learning models and explain the advantages that traditional models can have over neural networks.
- Understand the difference between simple and multiple linear regression.
- Explain how simple and multiple linear regression models make predictions and why they are generally considered to be explainable / interpretable models.
- Explain the steps required to implement a linear regression model in Python using scikit-learn to predict a continuous output variable from input variable(s).
- Interpret the coefficients and intercept of a fitted linear regression model to understand the learned relationship between input and output variables.
- Use Python and Pandas to train models and manipulate data frames (you will not have to write code during quizzes but you may have to explain or interpret what some Python / Pandas code does).


## Exploring Machine Learning

<div style="position:relative;height:0;padding-bottom:56.25%"><iframe width="640" height="360" src="https://www.linkedin.com/learning/embed/artificial-intelligence-foundations-machine-learning-22345868/exploring-machine-learning?autoplay=false&claim=AQGVTyuTZYVRhQAAAZIu5B5euNVEdSXaIJwGQzUrycJtDofbshEKHDxIEjYr-ERvYMNS9z3i51GmmSPsmcB_-Hp3qgo82JYiLOIunmVPI0TMt52faodpIv5wkRHqukdJ-n2Ywn5JuCAw3OQU-JoWi43LMecv2PD6fxVCaDthZ-Cf6zyFm8PNqm3Zg6jawt9JfKtKLxu5UpEmeJwzgzWHuMuK0KEqh1eN7B7sfFywRXz-DegLY3rSdXrYW5UDwlt63GUHPWuNCGzplF_WUzBEo-PvSSA7j5Wv7Wo8s_Ulf9RohFEmoR5gM6zRWNEXuLFqgdxDR7y1qqSYj-Rk0gkoL3H9y4OHyg6sL7Rm5Jcz0HWd-4BJlc6q2nd-HJKaxFZBsPYc_HRSAeAoiulfNJvZzvmHJ8lvT2is311uUMVgrk4jcLyrTbbedyH5OHR61ME411SKG1PldWW7YTx05GomBvp8pydcMm8BJ95DX74ZjqHssHApgfYrm90dHSqiWPhHcbbdcBEIoZfZZRzNUeMOMz8uz-8wKnO37bydjKxBFWJ8faLIEZsDJMQ4MRGad9lQiOZ6SOOtEFWMHHNMTK2j3k0dSNHf0d-JbYRoFPi53C5h1AN6g51eKSIi7SuuAjMe3eDXG9wq4K7OPjE3jFlBTGMDKU_yvYa5YzeZPtiCqi6ipk9BRe7f9AcunXlv_sXPX9mRaOjjDGl-AMKNm_WBh-CWUBapsvY-lKPoX6T4_9ixW2lb6lPOCmcbxlG5UHckC9fSTIukzeW3624bkCF7-w0tGtNOBAVMupv8nVBEgUlwsDkKZavAKHq-zqWLTTwITfUk8E4qmObxPIciGk6uDjzZQ1ZDyHPYbdspO1nrRV__dOhDdJ-o_1f7ethUR1cywLCQ0nrhDGSnEt_iF34QC4J_ybCFWMWObAmf6Hs48zp8iTQbgz79vEFV3wSZF0mHA6DHy7dyPtnNgG15RGx5uWBZB5uWDFq1qZ9hooIi7_UL_aXBimrkVFRHjsRxzQY-uill0iBMYdcWBHC3fZGBW09DupCsjAHDo5doTXo5y1NpmczM1B4ijmVYA40gtwjr9xdf_C7_sZNQp_jhijPdXhEExXnVTNFfKJtdo53btOjde2-Kq7Km4L9yedbhN8xCAKOYVkC-kEiZ9pH7Pmil97BsPMtUHrfZk8N4kOS9vubsoz0mEX5NVPoo3u_85S_RjFGS9ZAh7eWj-GM4PmJZh89SQq4y" mozallowfullscreen="true" webkitallowfullscreen="true" allowfullscreen="true" frameborder="0" style="position:absolute;width:100%;height:100%;left:0"></iframe></div><p><strong><a href="https://www.linkedin.com/learning/artificial-intelligence-foundations-machine-learning-22345868/exploring-machine-learning?trk=embed_lil">Exploring machine learning</a></strong> from <strong><a href="https://www.linkedin.com/learning/artificial-intelligence-foundations-machine-learning-22345868?trk=embed_lil">Artificial Intelligence Foundations: Machine Learning</a></strong> by <strong><a href="https://www.linkedin.com/learning/instructors/kesha-williams?trk=embed_lil">Kesha Williams</a></strong></p>

## How Machines Learn

<div style="position:relative;height:0;padding-bottom:56.25%"><iframe width="640" height="360" src="https://www.linkedin.com/learning/embed/artificial-intelligence-foundations-machine-learning-22345868/examining-how-machines-learn?autoplay=false&claim=AQGq8rZZLdKr2AAAAZIu5MdKoBTFR8i2Luys8U7ldfvKt6wIvP0KjQAjPaB7Z5l4lzH-iSEZot0HHraxuIQIETEB3KL0HLw5qEKptOU6mSxDZ-2nQQzkqWuoGBww3tWwyJf0OeBOnBspnobFmRke-KOzVJd5KOUwj9U6MjMc7aUOLZcLSS8y_xqOcRbp43iF4avSBW0e_sb2jqqF8O6hk3qSGV5GJufiKT7ThnpLFEeTWIsrFuDyNNPJIP7MRMggiLzr9WvaCmEItoOICWsmp1XMiWzV_scnFSOtL93AdKGY2UZWK-4dVCXOLY_73I2apxbg1rIJsDhjEPOP2Ws_yJnwzdSoYOgWkk0tqIDDKl5FNCnL4f2a1Z0Rl_RAK982Y46NvHXDlQggmsvVMdy3VacC7OdUVJ8De79mzB79CO3yntsa62ycDIgZRAG3a_l1R-7JdH0fun48_8op_GlcLi5dyTsXRnfuBfpIMkwrFIojp0rISSTp-AEHWO__4iqCZc8hrhdskHs9hJ6Ft0Wsiei1hnCVqQsx7p7l7DeSGudbqATxtQ61Z371YuRo6F2rnivK-BJS8Z63WvZ0vbdLs-YEZuQOyLZoYgLN96U5VtkdC0ab3MTFWOx7AwCBt9gRt9dpYC8YL_rfu2XxEVvAedSEdlqOOeEZmbbVjjvHjEM_9V9e-conLlLzF-EJTIq6-u9YSGB-8yw3L9xSRSIKq58Tjv2YKJ_rq7lGqVC_v7M7Veq8IuqWfYHPmJGMZzI5dDeDxPRpEEwywvMEaAmor9z7o6fgKtmHHl8L1lmCiGh1DKUkk-QuKfU6LhWQ3eLxqEDIVt7LI5IFr9RKKjpeCCxJtACXbz3l9bE6-zJfzpvgnq34zlOO6WCJMd-fw3GDauHM283ewCGPxhN2r7IcU3-nHxVAlysdHBQSS8IMoXRd0fElQyv7AP8evglTxRxieviA8GLRQsbVEn8nlidMueJ8MOiouh4mQWQF0FItFOs9p7h2KmvrPKdinUbOoy_xpdSIoBxDn2akOBsLg1VaubI0OTMRyZY26SX1-_a6xUTxBatnqnebCXOLrbsRRtjKYqagns5k4-s8vu56-i_BkDfCHtsMk6d9HUJdKt6yguQnVkmsN8hkoYjewzlJp5oweU1sxb_9FEJ911BbjOOm6H9iQbqNKKCIt9xtD4-U0BiWCOetM1ddjTU5gLMkZ69ERtnyJuhhHTga2hlaMd_VNWC4Ny6d" mozallowfullscreen="true" webkitallowfullscreen="true" allowfullscreen="true" frameborder="0" style="position:absolute;width:100%;height:100%;left:0"></iframe></div><p><strong><a href="https://www.linkedin.com/learning/artificial-intelligence-foundations-machine-learning-22345868/examining-how-machines-learn?trk=embed_lil">Examining how machines learn</a></strong> from <strong><a href="https://www.linkedin.com/learning/artificial-intelligence-foundations-machine-learning-22345868?trk=embed_lil">Artificial Intelligence Foundations: Machine Learning</a></strong> by <strong><a href="https://www.linkedin.com/learning/instructors/kesha-williams?trk=embed_lil">Kesha Williams</a></strong></p>

## AI Tasks and Types of Machine Learning
<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=6f841154-530c-499c-ae9f-b145010e5e6e&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player"></iframe>

## Quick Intro to Simple Linear Regression

<iframe width="720" height="405" src="https://www.youtube.com/embed/qxo8p8PtFeA?si=0ovg0oldgqj-FDK4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Traditional Models and Linear Regression
<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=9c4076e5-f9a2-4979-b054-b14a0052d8cd&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player" aria-description="Linear Regression" ></iframe>

### Links
- Study Hours Dataset: [Student Study Hours (kaggle.com)](https://www.kaggle.com/datasets/himanshunakrani/student-study-hours/data?select=score.csv)
- Admissions Dataset: [Data for Admission in the University (kaggle.com)](https://www.kaggle.com/datasets/akshaydattatraykhare/data-for-admission-in-the-university)
- My Notebook: https://colab.research.google.com/drive/1h3-bCRU2JQ5VqFLbshVIK84HlITYwV6Q?usp=sharing

## Assignment: Multiple Linear Regression

<iframe src="https://egator.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=1eb1e8a7-d650-4e3a-8eb8-b14a005b8b26&autoplay=false&offerviewer=true&showtitle=true&showbrand=true&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay" aria-label="Panopto Embedded Video Player" aria-description="Multiple Linear Regression Assignment" ></iframe>

#### Instructions
1. Find a dataset suitable for multiple linear regression analysis. [Find Open Datasets and Machine Learning Projects | Kaggle](https://www.kaggle.com/datasets?sort=votes&tags=13405-Linear+Regression)
2. Select the columns (features) you want to use as predictor variables and the column you want to predict (target variable).
3. Create a multiple linear regression model using the selected columns.
4. Use the model to predict the target variable.
5. Make your Colab notebook accessible to anyone with the link (Share -> General Access -> Change from "Restricted" to "Anyone with the Link" can view)
#### Evaluation
- Appropriate selection of dataset and columns for multiple linear regression
- Correct implementation of the multiple linear regression model
- Successful prediction of the target variable using the model
- Clear and well-documented code


#### Submission
Submit your assignment by providing a link to your Colab notebook to the assignment in Canvas. If you worked locally, export your document as an HTML or PDF file and upload that file to the assignment Canvas.


