## Installation

- git clone https://github.com/mercutiy/django
- python3 -m pip install Django
- python3 -m pip install djangorestframework
- cd django
- python3 manage.py makemigrations api
- python3 manage.py migrate
- python3 manage.py runserver 
- cd api

## Endpoints

Create, update products<br/>
`POST /api/v1/products/`<br/>
`curl --data @products.json  -H "Accept: application/json" -H "Content-type: application/json"  "http://127.0.0.1:8000/api/v1/products" -i`<br/>

Display all Products<br/>
`GET /api/v1/products/`<br/>
`curl -H "Accept: application/json" "http://127.0.0.1:8000/api/v1/products" | jq .`<br/>

Display the product by ID<br/>
`GET /api/v1/product/{sku}`<br/>
`curl -H "Accept: application/json" "http://127.0.0.1:8000/api/v1/product/C99900217" | jq .`<br/>

Display ids of all products with same size. _Can variate list of fields, ex: fields=sku,name_<br/>
`GET /api/v1/products/?size={size}`<br/>
`curl -H "Accept: application/json" "http://127.0.0.1:8000/api/v1/products?size=38&fields=sku" | jq .`<br/>

Display all collections<br/>
`GET /api/v1/collections/`<br/>
`curl -H "Accept: application/json" "http://127.0.0.1:8000/api/v1/collections" | jq .`<br/>

Display all products of given collections<br/>
`GET /api/v1/collection/{id}/products`<br/>
`curl -H "Accept: application/json" "http://127.0.0.1:8000/api/v1/collection/dapper/products" | jq .`<br/>
