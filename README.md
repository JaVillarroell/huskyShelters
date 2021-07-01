# Animal Adoption
Husky Shelters is an animal adoption agency. They operate globally with the goal of providing shelter and happiness to stray dogs and cats.

## Infrastructure
![Infraestructura](https://user-images.githubusercontent.com/27901732/124200511-89b81880-daa3-11eb-88b4-dda6a820c767.jpeg)

## Deploy
It is necessary to change the name of the `DEPLOYMENT_BUCKET` found in `project-name/deployment.sh`

For deploying the app is necesary to make this steps.

### Build

    ./deployment.sh -b

### Package

    ./deployment.sh -p

### Deploy

    ./deployment.sh -d

## API

The API of adoption is described below.

### Update Information and Image of pets

#### Request

`PUT /pets/{petID}?SK=dog`

Body:
    
    {
        "HealthStatus":"Weak",
        "Age":"6",
        "LocationPet":"Pando, Bolivia",
        "Pictures":["Image in Base64"],
        "PictureNames":["imageName1.jpg"]
    }
---
### Delete an Image of pets

#### Request

`PUT /pets/deleteImage/{petID}?imageName=imageName1`

---
### Receive request of Adoption

This endpoint solicits an adoption (creates a topic with the email and saves it on dynamodb)
#### Request

`/pets/solicitAdoption/{adoptID}?email=example@gmail.com`

Body:
    
    {
        "Adopted": "False",
        "Email":"holamundo@gmail.com"
    }
---
### Aprove Adoption


#### Request

`PUT /pets/approveAdoption/{adoptID}:`


---
## Autors ✒️

_This are the people that collaborated in the project._

* **Alejandro Ledezma** - *Adoption API*
* **Camila Medina** - *Data Migration*
* **Mathias Nieva** - *Public WebSite*
* **Carlos Paredes** - *Husky Shelters API*
* **Javier Villarroel** - *Data Migration*


