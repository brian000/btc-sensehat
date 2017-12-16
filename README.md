# btc-sensehat
stupid little script to watch a BTC address and blink lights on a RPi SenseHat if the balance is greater than 0

Prereqs:  

`pip install blockchain`  
`apt-get install sense-hat`


Run with:  

`python btc-sensehat.py <address to watch>`

For best results, add to your crontab  

`*/10 * * * * python ~/btc-sensehat/btc-sensehat.py <youraddress>`


Donations to `328b82wtCvPfv7F8VgxHRTwQkAZxdoBHC7` or `0xb217d7609430951AB677e333cc0fcC39F3B47Aba` are appreciated!
