import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { createContext, forwardRef, useContext, useId, } from "react";
import { cx } from "./cx.js";
const FieldContext = createContext(null);
/** `.field`: a label above one control, with help or an error under it, wired up for screen readers. */
export const Field = forwardRef(function Field({ label, help, error, children, className, ...rest }, ref) {
    const id = useId();
    const helpId = help ? `${id}-help` : undefined;
    const errorId = error ? `${id}-error` : undefined;
    const describedBy = [helpId, errorId].filter(Boolean).join(" ") || undefined;
    return (_jsxs("label", { ref: ref, className: cx("field", className), ...rest, children: [_jsx("span", { className: "field-label", children: label }), _jsx(FieldContext.Provider, { value: { describedBy, invalid: Boolean(error) }, children: children }), help && (_jsx("span", { id: helpId, className: "field-help", children: help })), error && (_jsx("span", { id: errorId, className: "field-error", children: error }))] }));
});
function useFieldProps(invalid, describedBy) {
    const field = useContext(FieldContext);
    return {
        "aria-invalid": (invalid ?? field?.invalid) ? true : undefined,
        "aria-describedby": describedBy ?? field?.describedBy,
    };
}
/** `.input`, the text box. */
export const Input = forwardRef(function Input({ invalid, className, ...rest }, ref) {
    const aria = useFieldProps(invalid, rest["aria-describedby"]);
    return _jsx("input", { ref: ref, className: cx("input", className), ...rest, ...aria });
});
/** `.select` in its `.select-wrap`, which draws the arrow. `className` goes on the select. */
export const Select = forwardRef(function Select({ invalid, className, ...rest }, ref) {
    const aria = useFieldProps(invalid, rest["aria-describedby"]);
    return (_jsx("span", { className: "select-wrap", children: _jsx("select", { ref: ref, className: cx("select", className), ...rest, ...aria }) }));
});
