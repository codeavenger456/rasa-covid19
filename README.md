# COVID-19 Rasa Assistant
Demo bot built in Rasa to inform users about COVID-19 

## Installation

To run the content of the repo, first install the dependencies using Anaconda :

```
conda env create -f environment.yml
```

This will install all dependencies needed to run the rasa bot.

Once the installation is complete, activate the newly created environment by using

```
conda activate rasa-covid19
```

Unfortunately, not all dependencies can be installed that way. We need to run one additional line in order to make sure everything is installed in order to run `ConveRT` :

```
pip install rasa[convert]
```

## Train the Rasa Model

To train the bot, run the following line from within the newly created environment

```
rasa train
```

This will train the model using the data available in the `data` directory for both NLU and dialogue management, using the modeling pipeline you defined in the `config.yml` file.


## Other Interesting COVID-19 Bots

* Nora : https://rasa.com/showcase/norabot
* Vocinity : https://rasa.com/showcase/vocinity
* NuEcho : https://www.nuecho.com/news-events/chatbot-rasa-artificial-intelligence-covid-19/
