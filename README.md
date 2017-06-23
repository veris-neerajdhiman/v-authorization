## About

- v-authorization is an `AM (access management)` micro-service.
- It is being used by following micro-services to manage access.
- [User](https://github.com/veris-neerajdhiman/v-user)
- [Crew](https://github.com/veris-neerajdhiman/v-crew)
- [Vault](https://github.com/veris-neerajdhiman/v-serviceVault)

## Prerequisites

#### Environment Variables : 

 - DATABASE_NAME_AUTH
 - DATABASE_USER
 - DATABASE_PASSWORD
 - DATABASE_HOST
 - DATABASE_PORT
 - SECRET_KEY
 
     
## Rules OR Conditions

- Following format is used to Manage access and identify `resource` & `target` :
 
1 ) Source 
```
SAMPLE_RGX_MATCHED_SOURCE = [
							'organization:2db95648-b5ea-458a-9f07-a9ef51bbca21:',
                             'organization-member:2db95648-b5ea-458a-9f07-a9ef51bbca21:',
                             ]
```
  - First elemnt in list menas source is `organization` with unique identifier `2db95648-b5ea-458a-9f07-a9ef51bbca21`.
  - Second element means source is `organization member`  with unique identifier `2db95648-b5ea-458a-9f07-a9ef51bbca21`.
                  
```                  
RESOURCE_RGX_MATCHED_RESOURCE = ['
								vrn:resource:organization:',
                                'vrn:resource:organization:2db95648-b5ea-458a-9f07-a9ef51bbca21:'
                                ]
```
- First elemnt means `resource` is `organization` 
- Second element means `resource` is  `2db95648-b5ea-458a-9f07-a9ef51bbca21` and its type is `organization`

**Note :** `vrn` in `Resource` rgx is common in all `resources` , it is important to define and every `resource`
 must starts with `vrn` but have no significance in deciding the access. 

### Example : 

```json
{
    "source":"organization:2db95648-b5ea-458a-9f07-a9ef51bbca21:",
    "source_permission_set":[
    	{
    	"target":"vrn:resource:member:",
    	"create": true,
    	"read":true,
    	"update":true,
    	"delete":true
    	}]

}
```

- Above json is post format of our create policy API, you can see our API's [here](https://swaggerhub.com/apis/veris-neerajdhiman/authorization-am_ser_ver/0.1).
- It means an `organization` source with unique identifier `2db95648-b5ea-458a-9f07-a9ef51bbca21` 
have `CURD` permissions on `resource` of type `member`. In short organization `2db95648-b5ea-458a-9f07-a9ef51bbca21` 
can add, update, fetch & delete `Members`.

## Installation :

1 ) Clone this repo

2 ) Setup virtual environment
```
cd <path-to-repo>/v-authorization/

virtualenv -p /usr/bin/python3 env

```

3 ) Activate Virtual environment
```
source env/bin/activate
```
4 ) Install requirements

- Base Requirements

```
pip install -r requirements/base.txt

```
- Testing Requirements
```
pip install -r requirements/test.txt

```
- Local requirements
```
pip install -r requirements/local.txt

```
- Production requirements

```
pip install -r requirements/production.txt

```
5 ) Prerequisites
- Makes sure above `Prerequisites` we mentioned above must be defined and fulfilled.

6 ) Run Server 
```
python manage.py runserver
```

## API Reference : 

- API documentation is hosted on [Swagger hub](https://swaggerhub.com/apis/veris-neerajdhiman/authorization-am_ser_ver/0.1) 
and is public.

 
## Tests : 

- Run tests using 
```
make test
```
 
 