# Vancouver DataJam Workshop: Create your first dashboard using Dash and Plotly

### Workshop level: intermediate

### Background knowledge

Knowledge of working with pandas needed to engage with the material in this workshop. Familiarity with Git and Github required (knowing how to clone a repository, create a repository, as well as add, commit and push changes to a repository). Knowledge of function definition assumed. Recommended to be familiar with at least one visualizing library in Python. Working knowledge of plotly is a plus, but not necessary. Knowledge of HTML is not necessary. 

### Workshop description

In this workshop we will use pandas, plotly and Dash to create a dashboard that explores changes in the average housing price in various provinces in Canada for the last 5 years. We will start by generating interactive visualizations using plotly and turn exploratory code into reusable functions. We will then work together to bring our functions into a script. Participants will be introduced into dashboarding, layout options, and will work together to generate and test a local dashboard. Participants will learn how to deploy their dashboard to production. 

### Workshop schedule

1. Data exploration and visualization using Jupyter notebooks
2. Turning code into functions, and scripting
3. Introduction to Dash and layouts 
4. Designing our layout
5. Implement dashboard and test locally
6. Engineering check: files necessary to successfully deploy. Hint: you can find them [here](https://github.com/Vancouver-Datajam/dashboard-prep)
7. Hosting the dashboard

### Setup prep

Prior to joining this workshop, participants will need a GitHub account, as well as a Heroku account. 

* See how to create a GitHub account https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account 

* To create a Heroku account visit https://signup.heroku.com/

* Install Heroku https://devcenter.heroku.com/articles/heroku-cli

* Please have Anaconda installed along with Python 3.6 or higher:
  1. Anaconda on Windows https://docs.anaconda.com/anaconda/install/windows/
  2. Anaconda on Mac https://docs.anaconda.com/anaconda/install/mac-os/
  3. Anaconda on Linux https://docs.anaconda.com/anaconda/install/linux/

From your local computer, open your terminal and enter

    git clone https://github.com/Vancouver-Datajam/dashboard-workshop-dash.git
    cd dashboard-workshop-dash/

Please ensure you create a virtual environment prior to engaging with the workshop material. 

For MacOS and Linux, use your terminal and enter the following two commands:

    python3 -m venv env
    source env/bin/activate
  
For Windows, use the Anaconda Prompt and enter the following two commands. 

    py -m venv env
    .\env\Scripts\activate

Once created, you will need to install required dependencies:
  
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
  
You can then navigate to the notebooks/ directory 
  
    cd notebooks/

We will use Jupyter notebook for this workshop. From this location, type on your terminal

    jupyter notebook

Once you are done with the notebook, you can shutdown your local instance by entering `CTRL + C`. 

Remember to deactivate your virtual environment:
  
    deactivate

Read more https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ 

### Workshop Instructors

Laura Gutierrez Funderburk (she/her)

Laura works as a data scientist at Cybera. Laura has a B.Sc. in Mathematics from Simon Fraser University, and was awarded a Terry Fox Gold medal for overcoming severe childhood trauma and helping the communities she forms part of. In her spare time, she is a co-organizer for PyLadies Vancouver, and is enthusiastic about cycling by the seaside and trail running. 

Hanh Tong (she/her)

Hanh works as a data scientist at Theory+Practice - a data science consulting company. She has a PhD in Economics from Simon Fraser University. She is interested in using experiments and data science to understand how people make decisions and why they behave the way they do. In her spare time, she enjoys dancing (West Coast Swing) with her two left feet.
