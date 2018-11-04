const PubSub = require('@google-cloud/pubsub');

const pubsub = new PubSub();


exports.publishInTopic = async (message, topicName) => {
  console.log(`will send to topic ${topicName} : ${message}`)
  const dataBuffer = Buffer.from(message);
  try {
    const messageId = await pubsub
      .topic(topicName)
      .publisher()
      .publish(dataBuffer);
    console.log(`Message ${messageId} published.`);
  } catch(err) {
    console.err('error:', err);
  }
};