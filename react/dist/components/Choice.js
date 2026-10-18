import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { forwardRef } from "react";
import { cx } from "./cx.js";
/** `.check`: a checkbox with its label after it. `className` goes on the label, the rest on the input. */
export const Checkbox = forwardRef(function Checkbox({ children, className, ...rest }, ref) {
    return (_jsxs("label", { className: cx("check", className), children: [_jsx("input", { ref: ref, type: "checkbox", ...rest }), children] }));
});
/** `.switch`: a squared on/off track with its label before it. `className` goes on the label. */
export const Switch = forwardRef(function Switch({ children, className, ...rest }, ref) {
    return (_jsxs("label", { className: cx("switch", className), children: [children, _jsx("input", { ref: ref, type: "checkbox", role: "switch", ...rest })] }));
});
