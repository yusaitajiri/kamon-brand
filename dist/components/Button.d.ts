import { type ButtonHTMLAttributes } from "react";
export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
    /**
     * `primary` is the one accent-filled action in a view, with the kamon's inner line; use it once.
     * `quiet` stays out of the way: in toolbars, beside a primary, inside rows. The default is secondary.
     */
    variant?: "primary" | "secondary" | "quiet";
};
/** `.button` from ui.css. `type` defaults to "button"; pass `type="submit"` in a form. */
export declare const Button: import("react").ForwardRefExoticComponent<ButtonHTMLAttributes<HTMLButtonElement> & {
    /**
     * `primary` is the one accent-filled action in a view, with the kamon's inner line; use it once.
     * `quiet` stays out of the way: in toolbars, beside a primary, inside rows. The default is secondary.
     */
    variant?: "primary" | "secondary" | "quiet";
} & import("react").RefAttributes<HTMLButtonElement>>;
