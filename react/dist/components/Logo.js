import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { forwardRef } from "react";
import { logos } from "../logos.js";
import { cx } from "./cx.js";
/**
 * The app's logo from logo/, drawn inline in its own color, which turns to its -on-dark color in dark
 * mode, data-theme included. Never recolor it: show each app's logo in that app's color.
 */
export const Logo = forwardRef(function Logo({ app, size = 32, title, className, ...rest }, ref) {
    const logo = logos[app];
    return (_jsxs("svg", { ref: ref, viewBox: "0 0 140 140", width: size, height: size, role: title ? "img" : undefined, "aria-hidden": title ? undefined : true, className: cx("logo", className), ...rest, children: [title && _jsx("title", { children: title }), _jsx("path", { fill: `var(--${logo.color})`, d: size < 32 ? logo.small : logo.full })] }));
});
