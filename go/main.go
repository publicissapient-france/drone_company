package droneCompany

import (
	"encoding/json"
	"errors"
	"log"
	"net/http"
	"os"
)

var (
	stdout = log.New(os.Stdout, "", 0)
	stderr = log.New(os.Stderr, "", 0)
)

func OnDroneEventHttp(w http.ResponseWriter, r *http.Request) {

	stdout.Println(r.Body)
	var message Message

	if err := json.NewDecoder(r.Body).Decode(&message); err != nil {
		stdout.Println(err)
		w.WriteHeader(500)
		return
	}

	err := publishWhenNoError(analyseMessage(message))
	if err != nil {
		stdout.Println(err)
		w.WriteHeader(500)
		return
	}

	return
}

func analyseMessage(message Message) (response Response, err error) {

	if message.Event == "WAITING_FOR_COMMAND" {
		return onWaitingForCommandEvent(message)
	}
	if message.Event == "MOVING" {
		return onMovingEvent(message)
	}
	if message.Event == "MOVE_LOCATION_ERROR" {
		return onMoveLocationError(message)
	}
	return Response{}, errors.New("Not implemented")
}

func onWaitingForCommandEvent(message Message) (response Response, err error) {

	response = Response{
		TeamID: message.TeamID,
		Command: Command{Name: "MOVE",
			Location: message.AvailableParcelsForTeams[0].Location.Pickup,
		},
	}

	return response, nil
}

func onMovingEvent(message Message) (response Response, err error) {

	return Response{}, errors.New("Not implemented")
}

func onMoveLocationError(message Message) (response Response, err error) {

	return Response{}, errors.New("Not implemented")
}

func publishWhenNoError(response Response, err error) error {

	if err == nil {
		responseInByte, err := json.Marshal(&response)
		if err == nil {
			return publishMessage(responseInByte)
		}
	}
	return errors.New("Failed to analyse")
}
