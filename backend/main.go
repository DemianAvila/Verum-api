package main

import (
	"net/http"
	"verum.com/api/endpoints"
	"verum.com/api/db_connection"
)                 



func main(){

	db_connection.CheckConnCredentials();

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