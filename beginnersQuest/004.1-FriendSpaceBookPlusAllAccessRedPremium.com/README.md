 FriendSpaceBookPlusAllAccessRedPremium.com

Result after 1 hour computation plus some guess work 
http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/
that website even though cute had nothing to offer

that code is at program and vm.py

so the code needs to go faster!
u need to optimize the code!
but it is highly opaque!

replacing the code with a simple awk script and map to make it more readable 


see replace.sh and map


now working up and down the stack and program execution .... hours! (and a lot of FU)
trying things .... but sadly that VM is no FSM. it utilizes pointer aritmethics ! :roll_eyes: wonder how they have created the code in the first place !


one hint: look at the stack!

looking at the stack at xor, right before the print_top: 
at first it seems primes but then 11 then 101 ... that seems odd
after some time of observation it seems its palindromes 

2,3,5,7,11,101,131,151,181,191,313,353,373,383,727,757,787

oeis sais it is palindromes and primes!  https://oeis.org/A002385


now it is "only" the matter of finding a ready made implementation in python  ;) as my python skilz are untraceable
https://stackoverflow.com/questions/36263254/how-to-generate-prime-palindromes-in-python-3


identifying the closest start primes of the 3 parts by try and error (xor  should be less than 256 )

see palindrome.py

gladly i made the programm readable before, so i can change it as easily too!  (maybe not the best solution though)
so i add a prime function to the VM and change the code, as well the initilaziation registers


xvm.py and xprogram

got it!
http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/
http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/humans_and_cauliflowers_network/amber.html 

CTF{Peace_from_Cauli!}









