package droneCompany

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestHandler(t *testing.T) {
	t.Run("receiving waiting for command", func(t *testing.T) {
		message := newMessage("WAITING_FOR_COMMAND")

		result, _ := analyseMessage(message)

		assert.Equal(t, result.Command.Name, "MOVE")
		assert.Equal(t, result.Command.Location, Position{
			Latitude:  48.90524759169551,
			Longitude: 2.2657060097635626,
		})
		assert.Equal(t, "black-543", result.TeamID)
	})

	t.Run("receiving moving", func(t *testing.T) {
		message := newMessage("MOVING")

		_, err := analyseMessage(message)
		assert.Error(t, err)
	})

	t.Run("receiving waiting for command", func(t *testing.T) {
		message := newMessage("MOVE_LOCATION_ERROR")

		_, err := analyseMessage(message)
		assert.Error(t, err)
	})
}

func newMessage(eventType string) Message {
	message := Message{
		TeamID: "black-543",
		Event:  eventType,
		DroneInfo: DroneInfo{Location: Position{
			Latitude:  48.86439099043799,
			Longitude: 2.3426746801338623},
			Parcels: []Parcel{{
				TeamID: "black-543",
				Status: "AVAILABLE",
				Location: Location{
					Pickup: Position{
						Latitude:  48.90524759169551,
						Longitude: 2.2657060097635626,
					},
					Delivery: Position{
						Latitude:  48.867271697034234,
						Longitude: 2.273857921355812,
					},
				},
				Type:  "CLASSIC",
				Score: 50,
			},
				{
					TeamID: "all",
					Status: "AVAILABLE",
					Location: Location{
						Pickup: Position{
							Latitude:  46.90524759169551,
							Longitude: 46.2657060097635626,
						},
						Delivery: Position{
							Latitude:  46.867271697034234,
							Longitude: 44.273857921355812,
						},
					},
					Type:  "CLASSIC",
					Score: 50,
				}},
		},
		AvailableParcelsForTeams: []AvailableParcelsForTeam{
			{TeamID: "black-543",
				Status: "AVAILABLE",
				Location: Location{
					Pickup: Position{
						Latitude:  48.90524759169551,
						Longitude: 2.2657060097635626,
					},
					Delivery: Position{
						Latitude:  48.867271697034234,
						Longitude: 2.273857921355812,
					},
				},
				Type:  "CLASSIC",
				Score: 50},
		},
	}
	return message
}
