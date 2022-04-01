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

### 2. Hashing a file
```
python sha256.py -f input-file.txt
```

## Testing
The Application is tested using [Pytest](https://docs.pytest.org/en/7.1.x/)  
To run the tests:  
```
pip install -r requirements.txt  
pytest
```
