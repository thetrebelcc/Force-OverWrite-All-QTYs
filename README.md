# Introduction
This module modifies the functionality of the stock.quant model in Odoo. A new field called force_qty is introduced, which allows the user to input a quantity value that will be used to update both the quantity and reserved_quantity fields of the stock.quant model.


## Usage
To use this module, first install it on your Odoo system. Then, go to the Quantities tab of the Inventory menu. You should see a new column called Force Quantity in the list of quant records.
To update the quantity and reserved_quantity fields, input a value in the Force Quantity field and click the Save button. This will allow you to deal with the "It is not possible to unreserve more products of ... than you have in stock." bug, allowing you to close/cancel stock.picking that is bugged. 



## Notes
Currently there is no security/user limit, I will add a way to only have the admin be abel to use this module. 


![Before Input ](https://github.com/thetrebelcc/Force-OverWrite-All-QTYs/blob/master/Screenshot%20(603).png)

![After Input](https://github.com/thetrebelcc/Force-OverWrite-All-QTYs/blob/master/Screenshot%20(604).png)
