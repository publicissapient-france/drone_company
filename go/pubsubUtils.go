package droneCompany

import (
	"cloud.google.com/go/pubsub"
	"context"
)

func publishMessage(msg []byte) error {

	ctx := context.Background()
	t := connectTopic()

	result := t.Publish(ctx, &pubsub.Message{
		Data: []byte(msg),
	})

	id, err := result.Get(ctx)
	if err != nil {
		stderr.Fatalf("Could not publish message: %v", err)
	}

	stdout.Printf("Published a message; msg ID: %v, content: %s\n", id, msg)
	return nil
}

func connectTopic() *pubsub.Topic {
	ctx := context.Background()

	client, err := pubsub.NewClient(ctx, "jbc-atl-sal-func-techevent")
	if err != nil {
		stderr.Fatalf("Could not create pubsub Client: %v", err)
	}
	return client.Topic("drone-command")
}
