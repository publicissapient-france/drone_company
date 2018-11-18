import test from 'ava';
import proxyquire from 'proxyquire';
const sinon = require('sinon');

let eventMsg = {
  "teamId": "black-543",
  "event": "WAITING_FOR_COMMAND",
  "droneInfo": {
    "location": {
      "latitude": 48.86439099043799,
      "longitude": 2.3426746801338623
    },
    "topicUrl": "https://europe-west1-...",
    "parcels": [
      {
        "teamId": "black-543",
        "status": "AVAILABLE",
        "location": {
          "pickup": {
            "latitude": 48.90524759169551,
            "longitude": 2.2657060097635626
          },
          "delivery": {
            "latitude": 48.867271697034234,
            "longitude": 2.273857921355812
          }
        },
        "type": "CLASSIC",
        "score": 50
      },
    ],
    "score": 0
  },
  "availableParcelsForTeam": [
    {
      "teamId": "black-543",
      "status": "AVAILABLE",
      "location": {
        "pickup": {
          "latitude": 48.90524759169551,
          "longitude": 2.2657060097635626
        },
        "delivery": {
          "latitude": 48.867271697034234,
          "longitude": 2.273857921355812
        }
      },
      "type": "CLASSIC",
      "score": 50
    },
    {
      "teamId": "black-543",
      "status": "AVAILABLE",
      "location": {
        "pickup": {
          "latitude": 48.90524759169551,
          "longitude": 2.2657060097635626
        }
      },
      "type": "SPEED_BOOST",
      "score": 0.1
    }
  ]
};


test('receiving WAITING_FOR_COMMAND event', async t => {
  let msgSent;
  const index = proxyquire.load(
    './index', {
      './pubsubUtils' : {
        'publishInTopic': async (message, topicName) => {
          msgSent = JSON.parse(message);
          console.log('publishInTopic called')
          return
        }
      }
    }
  );
  eventMsg.event = 'WAITING_FOR_COMMAND';
  const req = {
    body: {
      ...eventMsg
    }
  };
  const res = { send: sinon.stub() };

  // when
  await index.onDroneEventHttp(req, res);

  // then
  t.true(res.send.calledOnce);
  if (msgSent && msgSent.command.name === 'MOVE') {
    t.true(msgSent.command.location.latitude != undefined);
    t.true(msgSent.command.location.longitude != undefined);
  }
});


test('receiving MOVING event', async t => {
  let msgSent;
  const index = proxyquire.load(
    './index', {
      './pubsubUtils' : {
        'publishInTopic': async (message, topicName) => {
          msgSent = JSON.parse(message);
          console.log('publishInTopic called')
          return
        }
      }
    }
  );

  eventMsg.event = 'MOVING';
  const req = {
    body: {
      ...eventMsg
    }
  };
  const res = { send: sinon.stub() };

  // when
  await index.onDroneEventHttp(req, res);

  t.true(res.send.calledOnce);
});
