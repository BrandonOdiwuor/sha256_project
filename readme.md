# The SHA-256 Project
Python Implementation of the SHA-256 Secure Hashing Algorithm defined in [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final). 

- SHA-256 - An Implementation of Secure Hashing Algorithm 2 (SHA-2) with 256-bit digest. 
- This implementation is based on the pseudocode algorithm from [Wikipedia](https://en.wikipedia.org/wiki/SHA-2#Pseudocode) and [The SHA-256 Project](https://github.com/oconnor663/sha256_project)

## Usage
![sha256_help](https://user-images.githubusercontent.com/15610188/161290119-fe83155f-33a4-4c8c-a420-8f61985554c6.PNG)

### 1. Hashing a string
```
python sha256.py -s 'message string'
```
#### Screenshot example - String hashing compared with Python's Hashlib sha256 result
![sha256_string_hash_latest](https://user-images.githubusercontent.com/15610188/161417365-ac2d728e-3916-4376-be5a-882554877434.PNG)


### 2. Hashing a file
```
python sha256.py -f input-file.txt
```
#### Screesnhot example - File hashing
![sha256_file_hash](https://user-images.githubusercontent.com/15610188/161234743-39caa934-4d88-472c-a7a8-2c4c2a576eee.PNG)


## Testing
The Application is tested using [Pytest](https://docs.pytest.org/en/7.1.x/)  
To run the tests:  
```
pip install -r requirements.txt  
pytest
```
