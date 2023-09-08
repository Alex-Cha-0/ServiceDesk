// var express = require('express');
// var app = express();
//
// app.get('/', function (req, res) {
//
//     var sql = require("mssql");
//
//     // config for your database
//     var config = {
//         user: 'alex',
//         password: 'Renovation21;',
//         server: '1c\\mssql2016',
//         database: 'alex',
//         pool: {
//             max: 10,
//             min: 0,
//             idleTimeoutMillis: 30000
//         },
//         options: {
//             encrypt: false, // for azure
//             trustServerCertificate: false // change to true for local dev / self-signed certs
//         }
//     };
//
//     // connect to your database
//     sql.connect(config, function (err) {
//
//         if (err) console.log(err);
//
//         // create Request object
//         var request = new sql.Request();
//
//         // query to the database and get the records
//         request.query('select content from chat where chat_id = 1451', function (err, recordset) {
//
//             if (err) console.log(err)
//
//             // send records as a response
//             res.send(recordset);
//
//         });
//     });
// });
//
// var server = app.listen(5000, function () {
//     console.log('Server is running..');
// });

// const sql = require('mssql')
// const sqlConfig = {
//   user: 'alex',
//   password: 'Renovation21;',
//   database: 'alex',
//   server: '1c\\mssql2016',
//   pool: {
//     max: 10,
//     min: 0,
//     idleTimeoutMillis: 30000
//   },
//   options: {
//     encrypt: false, // for azure
//     trustServerCertificate: false // change to true for local dev / self-signed certs
//   }
// }
//
// async () => {
//  try {
//      value = 26
//   // make sure that any items are correctly URL encoded in the connection string
//   await sql.connect(sqlConfig)
//   const result = await sql.query`select * from chat where message_id = ${value}`
//   console.dir(result)
//  } catch (err) {
//   // ... error checks
//  }
// }
