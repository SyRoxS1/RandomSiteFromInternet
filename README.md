# RandomSiteFromInternet

Here is the live version on my website : https://random.syroxs.online

When someone send a POST request to the api with the right data the programms will generate a group of randoms IP to scan and look for a website, it will first send to TCP packet to the 80 or 443 port depending on the HTTP or HTTPS request, then if the server anwsers it, I do a get request using requests library on python, and if the response code is between 200 and 299 it will send back the ip to the user

I also made a programme that send the data of the website to chat gpt api in gpt_webtxtanalyst.py, to scan large ammount of website without the need to manually check them.
