# Song Lyrics Analyzer

## Requirements  
[Python 3](https://www.python.org/download/releases/3.0/)  
[Genius API Client Access Token](https://genius.com/api-clients)

## Install  
* Clone this Repo
``` git clone https://github.com/getraid/SongLyricsAnalyzer.git ```
* Install pip packages 
``` pip install -r requirements.txt ```
* Insert Client Access Token into 
```1-AllSongsGetAllJson.py``` 
* Change the song count and artist
* Now click on ```1-AllSongsGetAllJson.py```, after it finished execute ```2-AllSongsGenerateAllInOne.py``` and lastly ```3-AllSongsWordCount.py```

## Custom Dictonary  
Lastly you can make a custom dictonary if you wish to.  
* Open Notepad++ and use ctrl + f to pop the find and replace window up.
* Use the regex.txt file to format the file into a single word on a line format
* Click on ```DictonaryCreator.py```
