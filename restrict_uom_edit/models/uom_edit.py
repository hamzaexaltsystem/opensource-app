from odoo import api, models,_
from odoo.exceptions import UserError
 
class ProductUom(models.Model):
    _inherit = "uom.uom"

    def write(self, vals):
        if not self.user_has_groups('restrict_uom_edit.group_user_uom_edit'):
            raise UserError(
                        _("You are not allowed to edit UOM!"))
        return super(ProductUom, self).write(vals)
    
    @api.model
    def create(self, vals):
        if not self.user_has_groups('restrict_uom_edit.group_user_uom_edit'):
            raise UserError(
                        _("You are not allowed to Create UOM! Please Contact Administrator"))
        return super(ProductUom, self).create(vals)
    
    
class ProductUomCateg(models.Model):
    _inherit = "uom.category"
    
    
    def write(self, vals):
        if not self.user_has_groups('restrict_uom_edit.group_user_uom_edit'):
            raise UserError(
                        _("You are not allowed to edit UOM!"))
        return super(ProductUomCateg, self).write(vals)
    
    @api.model
    def create(self, vals):
        if not self.user_has_groups('restrict_uom_edit.group_user_uom_edit'):
            raise UserError(
                        _("You are not allowed to Create UOM! Please Contact Administrator"))
        return super(ProductUomCateg, self).create(vals)

        
