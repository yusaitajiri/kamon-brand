import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import { forwardRef } from "react";
import { Logo } from "./Logo.js";
import { cx } from "./cx.js";
/** `.card` on `surface-raised` with a hairline border. */
export const Card = forwardRef(function Card({ frame, className, ...rest }, ref) {
    return _jsx("div", { ref: ref, className: cx("card", frame && "frame", className), ...rest });
});
/** `.list`, a plain list of rows. */
export const List = forwardRef(function List({ className, ...rest }, ref) {
    return _jsx("ul", { ref: ref, className: cx("list", className), ...rest });
});
/** `.list-row`: its content on the left and `meta` on the right. */
export const ListRow = forwardRef(function ListRow({ selected, meta, children, className, ...rest }, ref) {
    return (_jsxs("li", { ref: ref, className: cx("list-row", className), "aria-selected": selected || undefined, ...rest, children: [_jsx("span", { children: children }), meta != null && _jsx("span", { className: "list-meta", children: meta })] }));
});
/** `.tag`, with `radius-sm` corners: never a pill. */
export const Tag = forwardRef(function Tag({ pressed, className, ...rest }, ref) {
    return _jsx("span", { ref: ref, className: cx("tag", className), "aria-pressed": pressed ?? undefined, ...rest });
});
/** `.empty`: one sentence, a little warm, optionally under the app's logo. */
export const EmptyState = forwardRef(function EmptyState({ app, children, className, ...rest }, ref) {
    return (_jsxs("div", { ref: ref, className: cx("empty", className), ...rest, children: [app && _jsx(Logo, { app: app, size: 48 }), children] }));
});
/** `.rule`, 子持ち罫: only once per view, under the app bar. Never between sections. */
export const Rule = forwardRef(function Rule({ className, ...rest }, ref) {
    return _jsx("hr", { ref: ref, className: cx("rule", className), ...rest });
});
