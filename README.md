# Password Obfuscator

## Generate a simple, shareable randomized string with _manual_ decoding instructions

_Allows for a LOW-SECURITY password to be shared without being visually decoded/memorized. Useful for remotely sharing a laptop password or password that requires a one-time use_
<br>
<br>

```python
Enter a string: Example2-Pa$sworD+98
Obfuscated password: E?jxmaamp,=lqe|_2m[-POai$\s]woLrZHD5-+c^9D18Vi
Directions:
    ['DEL', 'DEL', '←', 'DEL', 'DEL', '←', 'DEL', 'DEL', '←', 'DEL', 'DEL', '←', 'DEL', 'DEL', '←', 'DEL', '←', '←', 'DEL', '←', 'DEL', '←', 'DEL', '←',
     'DEL', '←', '←', 'DEL', 'DEL', '←', 'DEL', 'DEL', '←', 'DEL', '←', 'DEL', 'DEL', '←', '←', 'DEL', '←', 'DEL', '←', 'DEL', 'DEL', '←']
```

## How it works:

1. When prompted, provide a password string that you'd like to share<br>

2. Program will randomly pad the string with random ASCII characters and output decoding instructions<br>

3. Share obfuscated password and decoding instructions (start decoding from end of string)<br>
