package db_connection

import (
	"os"
	"context"
	"verum.com/api/logger"
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

func GetMongoClient() *mongo.Client{
	//GET THE CURRENT DIR OF THE PROJECT
	dir, err := os.Getwd();
	if err != nil {
		panic(err);
	};
	//SET THE DIR OF THE ENV FILE WITH THE CREDENTIALS 
	dir = dir + "/db_connection/.env";
	if _, err := os.Stat(dir); err != nil {
		logger.LoggerType("ERROR", "File does not exist");
		panic("File does not exist\n");
	};
	godotenv.Load(dir);

	mongo_uri := MongoURIPieces{
		user: os.Getenv("MONGO_USER"),
		pass: os.Getenv("MONGO_PASS"),
		host: os.Getenv("MONGO_IP"),
		port: os.Getenv("MONGO_PORT"),
	}

	mongo_uri.URI = "mongodb://"+mongo_uri.user+":"+mongo_uri.pass+"@"+mongo_uri.host+":"+mongo_uri.port;

	
	// Use the SetServerAPIOptions() method to set the Stable API version to 1
	serverAPI := options.ServerAPI(options.ServerAPIVersion1);
	opts := options.Client().ApplyURI(mongo_uri.URI).SetServerAPIOptions(serverAPI);
	// Create a new client and connect to the server
	client, err := mongo.Connect(context.TODO(), opts);
	if err != nil {
		logger.LoggerType("ERROR", "DB was not founded, checkURI");
		logger.LoggerType("INFO", mongo_uri.URI);
		logger.LoggerType("ERROR", err.Error())
		panic(err)
	}
	defer func() {
		if err = client.Disconnect(context.TODO()); err != nil {
			logger.LoggerType("ERROR", "DB disconnection error");
			logger.LoggerType("ERROR", err.Error())
			panic(err);
		}
	}()
	// Send a ping to confirm a successful connection
	var result bson.M
	if err := client.Database("admin").RunCommand(context.TODO(), bson.D{{"ping", 1}}).Decode(&result); err != nil {
		logger.LoggerType("ERROR", err.Error());
		panic(err);
	}
	logger.LoggerType("INFO","DB succesfuly conected");
	//logger.LoggerType("INFO", reflect.TypeOf(client).String());
	return client;
}