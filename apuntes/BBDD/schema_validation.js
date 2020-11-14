//use amenities;
// debemos crear la base de datos y no depender de lo de arriba
db.createCollection("packs", {
    validator: {
        $jsonSchema: {
            bsonType: "object",
            required: ["PricePack","NamePack","ContentPack","HasCupon","HasParking"],
            properties: {
                "_id":{},
                "PricePack":{
                    bsonType: "int",
                    description: "The price of the Pack"
                    //debe ser 0 (Free) o x (buy)
                },
                "NamePack":{
                    bsonType: "string",
                    description: "The name of the Pack"
                },
                "ContentPack":{
                    bsonType: "array",
                    items: {
                        bsonType:"object",
                        required: ["name"],
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
                },
                "HasCupon":{
                    type:"boolean",
                    description:"Para saber si tiene o no descuento el pack"
                },
                "HasParking":{
                    bsonType:"bool",
                    description:"Para saber si el pack es solo para los que tienen parking"
                }
            }
        }
    }
});

db.packs.insertOne(
    {
        PricePack:NumberInt(0),
        NamePack:"Pack de Prueba",
        ContentPack:[
            {
                name:"Chuches",
                description:"esto es una bolsa de chuches"
            },
            {
                name:"golosinas",
                description:"esto e suna bolsa de golosinas"
            }
        ],
        HasCupon:false,
        HasParking:true
    }
)