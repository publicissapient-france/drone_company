/*eslint-disable semi, no-empty-label, no-undef, no-extra-semi, no-undef-expression, no-unused-params, no-use-before-define*/
const { publishInTopic } = require('./pubsubUtils');
const turf = require('@turf/turf');


exports.onDroneEventHttp = async (req, res) => {

  console.log(`receiving: ${JSON.stringify(req.body)}`);

  const droneEvent = req.body;

  if (!droneEvent && !droneEvent.event) {
    console.error('bad droneEvent received');
    res.status(500).send('bad droneEvent received');
    return;
  }

  let command = null;

  if (droneEvent.event === 'WAITING_FOR_COMMAND') {
    command = onWaitingForCommandEvent(droneEvent);
  } else if (droneEvent.event === 'MOVING') {
    command = onMovingEvent(droneEvent);
  } else if (droneEvent.event === 'MOVE_LOCATION_ERROR') {
    command = onMoveLocationError(droneEvent);
  }

  if (command !== null) {
  	await publishInTopic(JSON.stringify(command), 'projects/jbc-atl-sal-func-techevent/topics/drone-command');
  }


  res.send('ok');
};

function onWaitingForCommandEvent(droneEvent) {
  let command = null;

  /*
  example of a move command:

  command = {
    teamId: droneEvent.teamId,
    command: {
      name: 'MOVE',
      location: {
        latitude: x,
        longitude: y
      },
    }
  };
  */


  // write your code here

  return command;
}

function onMovingEvent(droneEvent) {
  // write your code here
  return null;
}

function onMoveLocationError(droneEvent) {
  // write your code here
  return null;
}

const distance = (locationA, locationB) => {
  const itemATurfLocation = turf.point([locationA.latitude, locationA.longitude]);
  const itemBTurfLocation = turf.point([locationB.latitude, locationB.longitude]);
  return turf.distance(itemATurfLocation, itemBTurfLocation, {});
};