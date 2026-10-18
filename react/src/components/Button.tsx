import { forwardRef, type ButtonHTMLAttributes } from "react";
import { cx } from "./cx.js";

export type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  /**
   * `primary` is the one accent-filled action in a view, with the kamon's inner line; use it once.
   * `quiet` stays out of the way: in toolbars, beside a primary, inside rows. The default is secondary.
   */
  variant?: "primary" | "secondary" | "quiet";
};

/** `.button` from ui.css. `type` defaults to "button"; pass `type="submit"` in a form. */
export const Button = forwardRef<HTMLButtonElement, ButtonProps>(function Button(
  { variant = "secondary", type = "button", className, ...rest },
  ref,
) {
  return (
    <button
      ref={ref}
      type={type}
      className={cx("button", variant === "primary" && "button-primary", variant === "quiet" && "button-quiet", className)}
      {...rest}
    />
  );
});
