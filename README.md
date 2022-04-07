# The SHA-256 Project - [PyPI](#)
Python package implementing of the SHA-256 Secure Hashing Algorithm defined in [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final) with a command-line interface. 

- SHA-256 - An Implementation of Secure Hashing Algorithm 2 (SHA-2) with 256-bit digest. 
- This implementation is based on the pseudocode algorithm from [Wikipedia](https://en.wikipedia.org/wiki/SHA-2#Pseudocode) and [The SHA-256 Project](https://github.com/oconnor663/sha256_project)

## Usage
![sha256_help](https://user-images.githubusercontent.com/15610188/162286498-a33fa01f-b4b1-453f-8701-5395d5baf6ba.PNG)


### 1. Hashing a string
```
python sha256.py -s 'message string'
```
#### Screenshot example - String hashing compared with Python's Hashlib sha256 result
![sha256_string_hash](https://user-images.githubusercontent.com/15610188/162286572-111878f7-2a76-4158-91d6-c62ae892ae90.PNG)


### 2. Hashing a file
```
python sha256.py -f input-file.txt
```
#### Screesnhot example - File hashing
![sha256_file_hash](https://user-images.githubusercontent.com/15610188/162286838-15487283-e8e8-4d06-824a-3ffa8d0bf72a.PNG)


## Testing
The Application is tested using [Pytest](https://docs.pytest.org/en/7.1.x/)  
To run the tests:  
```
pip install -r requirements.txt  
pytest
```
