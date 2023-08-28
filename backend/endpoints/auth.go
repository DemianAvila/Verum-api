package auth

import (
	"fmt"
	"net/http"
)       

func Login() int{
	http.HandleFunc(
		"/",
		func(w http.ResponseWriter, r *http.Request){
			fmt.Fprintf(w,  "Que pedo");
		},
	);
	return 0;
}

func RecoverPass() int{
	http.HandleFunc(
		"/recover_pass",
		func(w http.ResponseWriter, r *http.Request){
			fmt.Fprintf(w,  "Que pedo aa");
		},
	);
	return 0;
}