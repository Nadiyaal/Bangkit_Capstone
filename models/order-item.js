const mysql = require('mysql');

const orderItemSchema = mysql.Schema({
    quantity: {
        type: Number,
        required: true
    },
    product: {
        type: mysql.Schema.Types.ObjectId,
        ref: 'Product'
    }
})

exports.OrderItem = mysql.model('OrderItem', orderItemSchema);