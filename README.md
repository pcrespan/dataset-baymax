# BayMED

## How to run? (Linux)
- `python3 -m venv .venv`
- `cd .venv`
- `. bin/activate`
- `pip install -r requirements.txt`
- `cd ..`
- `flask --app main run`

## DEV: To generate new 'requirements.txt'
-  `pip freeze > requirements.txt`

# API Docs

## Get symptons [GET]
API GET Endpoint to retrieve array key => values with all symptons from dataset.

**Endpoint:** `https://api-baymed.onrender.com/api/symptons`  
**Method:** `GET`  
**Params:** `None`  
**Response: Object collection**   

``` 
[
    {
        "key": "symptom_key_1",
        "en": "symptom_english_label_1",
        "ptbr": "symptom_portuguese_label_1",
    },

    ...

    {
        "key": "symptom_key_N",
        "en": "symptom_english_label_N",
        "ptbr": "symptom_portuguese_label_N",
    },
];
```

## Send symptons to prediction [POST]
API POST Endpoint to receive symptons from front-end and predict prognosis

**Endpoint:** `https://api-baymed.onrender.com/api/prediction`  
**Method:** `POST`  
**Params:** `Array: ['sympton_key_1', 'sympton_key_2', 'sympton_key_3', ... , 'sympton_key_N']`  
**Response: Object collection**   
``` 
[
    {
        "method": "MethodName1",
        "prognosis": "prognosis_1",
        "accuracy": "acc_prognosis_1",
    },

    ...

    {
        "method": "MethodNameN",
        "prognosis": "prognosis_N",
        "accuracy": "acc_prognosis_N",
    },
];
```
