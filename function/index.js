/*eslint-disable semi, no-empty-label, no-undef, no-extra-semi, no-undef-expression, no-unused-params, no-use-before-define*/
const PubSub = require('@google-cloud/pubsub');

const pubsub = new PubSub();


exports.onDroneEventHttp = async (req, res) => {
  
  console.log(`receiving: ${JSON.stringify(req.body)}`);

  const droneEvent = req.body;
  let command = null;
  
  if (droneEvent && droneEvent.event === 'INIT') {
  	
  	  command = {
	    teamId: 'yellow',
	    command: {
	      name: 'READY',
	      topicUrl : 'https://...',
	    }
	  };
  }
  
  if (command !== null) {
  	await publishInTopic(JSON.stringify(command), 'projects/jbc-atl-sal-func-techevent/topics/drone-command');
  }
  
  res.send('ok');
};


const publishInTopic = async (message, topicName) => {
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