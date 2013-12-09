What four-letter word is the same when it is read 
forwards, backwards and upside down?

http://richardwiseman.wordpress.com/2013/12/06/its-the-friday-puzzle-236/

My [first solution](solution1.py) scans all words in an online [english word list](http://www-personal.umich.edu/~jlawler/wordlist.html)
and the result is:

	$ python solution1.py 
	NOON

and my [second solution](solution1.py) prints out all potential candidates
assuming that we need at least one consonant and that
four times the same letter is not a solution:

	$ python solution2.py 
	 1 HIIH 
	 2 HOOH 
	 3 IHHI 
	 4 INNI 
	 5 ISSI 
	 6 IXXI 
	 7 IZZI 
	 8 OHHO 
	 9 ONNO 
	10 OSSO 
	11 OXXO 
	12 OZZO 
	13 NIIN 
	14 NOON 
	15 SIIS 
	16 SOOS 
	17 XIIX 
	18 XOOX 
	19 ZIIZ 
	20 ZOOZ 

If you want to run the code, [paste it into](http://www.compileonline.com/execute_python_online.php)
