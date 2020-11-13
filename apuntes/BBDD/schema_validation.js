use Amenities
// debemos crear la base de datos y no depender de lo de arriba
db.createCollection("packs", {

validator: {

$jsonSchema: {

    bsonType: "object",
    required: ["PricePack","NamePack","ContentPack","HasCupon","HasParking"],
    properties: {
        "PricePack":{
            bsonType: "integer",
            description: "The price of the Pack"
            //debe ser 0 (Free) o x (buy)
        },
        "NamePack":{
            bsonType: "string",
            description: "The name of the Pack"
        },
        "ContenPack":{
            bsonType: "array",
            items: {
                bsonType:"object",
                required: ["name","description"],
                properties:{
                    name:{
                        bsonType:"string",
                        description: "este es el nombre del elemento del pack"
                    },
                    description:{
                        bsonType:"string",
                        description: "esta es la descrición del elemento"
                    }
                }
            }
        }
    }
}}})