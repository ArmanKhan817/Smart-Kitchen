const AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();
var tableName = "customer";

exports.handler = (event, context, callback) => {
 console.log(event.customerid)
 var params = {
     TableName : tableName,
     Key : {
        "customerid" : event.customerid
        }
}
docClient.get(params, function(err, data) {
    callback(err, data);
    })
};

