package droneCompany

type Message struct {
	TeamID                   string                    `json:"teamId"`
	Event                    string                    `json:"event"`
	DroneInfo                DroneInfo                 `json:"droneInfo"`
	AvailableParcelsForTeams []AvailableParcelsForTeam `json:"availableParcelsForTeam"`
}

type DroneInfo struct {
	Location Position `json:"location"`
	TopicURL string   `json:"topicUrl"`
	Parcels  []Parcel `json:"parcels"`
	Score    int      `json:"score"`
}
type Parcel struct {
	Location Location `json:"location"`
	ParcelID string   `json:"parcelId"`
	Score    int      `json:"score"`
	Status   string   `json:"status"`
	TeamID   string   `json:"teamId"`
	Type     string   `json:"type"`
}

type Location struct {
	Delivery Position `json:"delivery"`
	Pickup   Position `json:"pickup"`
}

type Position struct {
	Latitude  float64 `json:"latitude"`
	Longitude float64 `json:"longitude"`
}

type AvailableParcelsForTeam struct {
	TeamID   string   `json:"teamId"`
	Status   string   `json:"status"`
	Location Location `json:"location,omitempty"`
	Type     string   `json:"type"`
	Score    int      `json:"score"`
}

type Response struct {
	TeamID  string  `json:"teamId"`
	Command Command `json:"command"`
}

type Command struct {
	Name     string   `json:"name"`
	Location Position `json:"location"`
}
