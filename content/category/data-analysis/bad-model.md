title: When models are deceptively bad.
date: 2024-09-17

I was once tasked with fitting some machine learning models in R to a subset of the well-known [abalone dataset](https://archive.ics.uci.edu/dataset/1/abalone), then recommending the best one. The aim was to use non-invasive measurements (like dimensions and weight) to classify their sex. 

Ultimately, I recommended _none_ of the models. Their overall accuracy percentages gave the impression that they performed kind of okay. But really, the models were garbage, as they misclassified nearly _all_ of the female abalone. 

This happened because the dimensions of male and female abalone overlapped too much i.e. they weren't separable. So, unable to differentiate, the models just guessed they were male.

![Box plots of abalone variables]({static}/images/abalone-variables.png)

It really demonstrated to me that there is more to machine learning than knowing a bit of Python or R. The hard part is being able to see - and admit - that your model is rubbish.

Source code and report: [GitHub](https://github.com/amanjit-gill-data/ml-classify-abalone)
