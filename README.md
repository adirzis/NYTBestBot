# NYTBestBot
The goal of this project is to add together two different descriptions of NYT Bestsellers using the NYT API to create a “super description.” It will also tweet the output using the Twitter API.

This project was coded in Python 3 and needs Python 3 or later to run. In addition, the pip and Tweepy libraries need to be installed. 

You will also need two API keys, one for the NYT API and one for the Twitter API. To acquire the correct Twitter API key, you will need to upgrade your Twitter account to an elevated Developer account.

You will also need to create a file to store the super descriptions in. In the same directory as the program create a .txt file named desc_test.txt.

Once all the files and libraries are correctly set up, you simply need to run the program in the console and it will make the super description and tweet the output. The console should output two success codes (“200”) and say “Done” after successfully tweeting. If the code is “429,” you are making too many requests in a short amount of time and need to wait a bit before posting. If you get two success codes but the tweet did not get published, the tweet text may have exceeded the character limit. This is a rare occurrence and you can simply rerun the program.

This code was created by Ashley Dirzis for the INFO 664 class at Pratt Institute. The Twitter account created with this project is @NYTBestBot.
