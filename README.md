# Twitter following extractor

Small program that extracts the URLs of the account a given user is following
 
## Requirements

Install the requirements

    pip install -r requirements.txt
    
## Set up a Twitter app

Set up a twitter app and fill the `config_template.py`, 
then rename it to `config.py`

## Usage

Run: 

    python following.py twitter_user following.txt
            
to extract the URLs of the accounts `twitter_user` is following.

If you don't specify any output path then it will just print the URLs 
for instance you could run:

    python following.py clem_doum 

to print the accounts I follow to your console
        