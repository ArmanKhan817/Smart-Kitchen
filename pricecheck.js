const AWS = require('aws-sdk');
var docClient = new AWS.DynamoDB.DocumentClient();
var tableName = "price";

exports.handler = (event, context, callback) => {
 console.log(event.products)
 var params = {
     TableName : tableName,
     Key : {
        "products" : event.products
        }
}
docClient.get(params, function(err, data) {
    callback(err, data);
    })
};