# File Provider
A sample of a simple project based on Django Rest Framework API.

## Solve app
A simple app receiving CSV file with basic math function to apply to values:

* receive CSV file via API

| function  | value1  | value2  |
| --------- | ------- | ------- |
| SUM       |     10  |     20  |
| DIV       |     10  |     15  |
| SUB       |     10  |      3  |
| MUL       |      5  |      2  |

* check data validity
* store (into Postgresql db) received data on 'input' table and any validation error on 'validations' table
* solve 
* store solutions to 'solutions' table

### API interface:
solutions: POST, GET, DELETE
validations: GET




Run

```sh
python manage.py runserver
```

App served on http://127.0.0.1:8000/ 

