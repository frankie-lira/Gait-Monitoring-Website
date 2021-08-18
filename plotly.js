// connect to Raspberry Pi via websocket
var ws = new WebSocket("ws://192.168.0.199:5678/");

// when the websocket connection is opened, create an empty graph
ws.onopen = function()
{
  var data = [{
    y: [],
    type: 'line',
    line: {color: '#000000'}
  }]

  var layout = {
    xaxis: {
      autorange: true
    },
    yaxis: {
      range: [0,4],
      type: 'linear'
    }
  };

  Plotly.react('myDiv', data, layout);
};

// when the client receives a message, split the message (one string with many data points) into an array with data points & plot onto empty graph
ws.onmessage = function (evt)
{
    var datalist = evt.data.split(/\r\n|\n\r|\n|\r/);
    //console.log(datalist);

    Plotly.extendTraces('myDiv',{y:[datalist]}, [0]);
};
