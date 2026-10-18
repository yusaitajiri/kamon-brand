import { jsx as _jsx } from "react/jsx-runtime";
import { forwardRef } from "react";
import { cx } from "./cx.js";
/** `.button` from ui.css. `type` defaults to "button"; pass `type="submit"` in a form. */
export const Button = forwardRef(function Button({ variant = "secondary", type = "button", className, ...rest }, ref) {
    return (_jsx("button", { ref: ref, type: type, className: cx("button", variant === "primary" && "button-primary", variant === "quiet" && "button-quiet", className), ...rest }));
});
