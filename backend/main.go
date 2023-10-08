package main

import (
	"fmt"
	"net/http"
	"verum.com/api/endpoints"
	"verum.com/api/db_connection"
	"verum.com/api/logger"
)                 



func main(){
	//START THE LOGGEER FILE
	logger.LoggerInit();

	db_client := db_connection.GetMongoClient();
	fmt.Println(db_client)

	auth.Login()

	//STABLISH THE SERVER AT PORT 80
	var server http.Server = http.Server{
		Addr: ":8081",
	};

	server_err := server.ListenAndServe();
	if (server_err != nil){
		panic(server_err)
	}
}