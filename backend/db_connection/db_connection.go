package db_connection

import (
	"fmt"
	"os"
	"context"
	"github.com/joho/godotenv"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type MongoURIPieces struct{
	user string
	pass string
	host string
	port string
	URI string
}

func CheckConnCredentials(){
	//GET THE CURRENT DIR OF THE PROJECT
	dir, err := os.Getwd();
	if err != nil {
		panic(err);
	};
	//SET THE DIR OF THE ENV FILE WITH THE CREDENTIALS 
	dir = dir + "/db_connection/.env";
	if _, err := os.Stat(dir); err != nil {
		panic("File does not exist\n");
	};
	godotenv.Load(dir);

	mongo_uri := MongoURIPieces{
		user: os.Getenv("MONGO_USER"),
		pass: os.Getenv("MONGO_PASS"),
		host: "localhost",
		port: "91",
	}

	mongo_uri.URI = "mongodb://"+mongo_uri.user+":"+mongo_uri.pass+"@"+mongo_uri.host+":"+mongo_uri.port;

	
	// Use the SetServerAPIOptions() method to set the Stable API version to 1
	serverAPI := options.ServerAPI(options.ServerAPIVersion1)
	opts := options.Client().ApplyURI(mongo_uri.URI).SetServerAPIOptions(serverAPI)
	// Create a new client and connect to the server
	client, err := mongo.Connect(context.TODO(), opts)
	if err != nil {
		panic(err)
	}
	defer func() {
		if err = client.Disconnect(context.TODO()); err != nil {
			panic(err)
		}
	}()
	// Send a ping to confirm a successful connection
	var result bson.M
	if err := client.Database("admin").RunCommand(context.TODO(), bson.D{{"ping", 1}}).Decode(&result); err != nil {
		panic(err)
	}
	fmt.Println("Pinged your deployment. You successfully connected to MongoDB!")
}