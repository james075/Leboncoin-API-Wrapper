# Leboncoin API Wrapper
[![Build Status](https://travis-ci.com/Shinyhero36/leboncoin-python-api-wrapper.svg?token=gYFzK1AozWjEsD9nL4UH&branch=master)](https://travis-ci.com/Shinyhero36/leboncoin-python-api-wrapper)
![Coverage Badge](coverage.svg)
[![GitHub issues](https://img.shields.io/github/issues/Shinyhero36/LeboncoinApiWraper)](https://github.com/Shinyhero36/LeboncoinApiWraper/issues)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Shinyhero36/LeboncoinApiWraper)

[![Build Status](https://img.shields.io/github/forks/Shinyhero36/LeboncoinApiWraper.svg)](https://github.com/Shinyhero36/LeboncoinApiWraper)
[![Build Status](https://img.shields.io/github/stars/Shinyhero36/LeboncoinApiWraper.svg)](https://github.com/Shinyhero36/LeboncoinApiWraper)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Shinyhero36/LeboncoinApiWraper)

Allow easy acces to leboncoin api using python

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
from Payload.Payload import Payload
from Response.Response import *


pl = Payload()
pl.setLimit(1)
pl.maxPrice(200)
pl.setDepartement("tarn")
pl.searchFor("google home", True)
response = Response(**pl.build())

print(response)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)