package auth

import (
	"fmt"
	"net/http"
	"encoding/json"
)       

type LoginReqBody struct{
	User string
	Pass string
}

type LoginResError struct{
	Description string
}

func Login() int{
	http.HandleFunc(
		"/login",
		func(w http.ResponseWriter, r *http.Request){
			w.Header().Set("Content-Type", "application/json");
			switch r.Method {
			case http.MethodPost:
				fmt.Fprintf(w,  "Que pedo aa");
			default:
				w.WriteHeader(http.StatusMethodNotAllowed);
				loginError, _:=json.Marshal(
					LoginResError{
						Description: "Incorrect method",
					},
				);
				w.Write(loginError);
			}
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