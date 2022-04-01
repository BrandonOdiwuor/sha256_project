# The SHA-256 Project
Implementation of the SHA-256 algorithm in Python. 

- SHA-256 - An Implementation of Secure Hashing Algorithm 2 (SHA-2) with 256-bit digest. 
- Secure Hashing Algorithm is defined in [FIPS 180-4](https://csrc.nist.gov/publications/detail/fips/180/4/final)
- This implementation is based on the pseudocode algorithm from [Wikipedia](https://en.wikipedia.org/wiki/SHA-2#Pseudocode) and [The SHA-256 Project](https://github.com/oconnor663/sha256_project)

## Usage

### 1. Hashing a string
```
python sha256.py -s 'message string'
```
#### Screenshot example - String hashing compared with Python's Hashlib sha256 result
![sha256_string_hash](https://user-images.githubusercontent.com/15610188/161234423-394f05cb-c45c-4da2-9471-85cf7d088391.PNG)

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
