/** @odoo-module **/

import { FormController } from "@web/views/form/form_controller";
import { patch } from "@web/core/utils/patch";

// Patch the FormController to override the canCreate property for the digizilla.digizilla model.
// This will hide the "Create" button in the control panel when viewing a form of this model.
patch(FormController.prototype, "digizilla.FormControllerPatch", {
    get canCreate() {
        if (this.props.resModel === 'digizilla.digizilla') {
            return false;
        }
        return super.canCreate;
    },
});
