from odoo import models, fields, api

class firstmod(models.Model):
    
    ## Inherit the stock.quant model
    
    _inherit = 'stock.quant'

    ## field for force quantity float
    
    force_qty = fields.Float(string="Force Qty")

                
    ## any change in force_qty field will update the quantity and reserved_quantity fields
    
    @api.constrains('force_qty')
    def _update_quantity(self):
        self.quantity = self.force_qty
        self.reserved_quantity = self.force_qty

    def _get_inventory_fields_write_or_create(self):
        res = super(firstmod, self)._get_inventory_fields_write_or_create()
        res += ['force_qty']
        return res




