## Home Computer forensics


mount FS 

``` ntfs-3g  family.ntfs ./Familiy/ ``` 


Find Files 

``` find . -type f -size +0c ```



``` cat ./Users/Family/Documents/credentials.txt
I keep pictures of my credentials in extended attributes.
``` 

Mehh


https://medium.com/@stdout_/accessing-ntfs-extended-attributes-from-linux-f79552947981

``` 
getfattr -R . 2>/dev/null
# file: Users/Family/Documents/credentials.txt
user.FILE0
``` 

``` 
getfattr -Rn user.FILE0 Users/Family/Documents/credentials.txt 
# file: Users/Family/Documents/credentials.txt
user.FILE0=0siVBORw0KGg ...... 
``` 

``` 
getfattr -Rn user.FILE0 Users/Family/Documents/credentials.txt | tail -n2| head -n1|  cut -c 12-   > "../file0.dat"
``` 

fu b64 decode not working ----> hint: use getfattr flags 

``` 
getfattr -Rn user.FILE0 -e text Users/Family/Documents/credentials.txt | tail -n2| head -n1|  cut -c 12-   > "../file0.png"
``` 


``` 

getfattr -Rn user.FILE0 -e hex Users/Family/Documents/credentials.txt | tail -n2| head -n1|  cut -c 14-   > "../file0.hex"
xxd -r -p ../file0.hex > ../file0.png

``` 

Flag: CTF{congratsyoufoundmycreds}









