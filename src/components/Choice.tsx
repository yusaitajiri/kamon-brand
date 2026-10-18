import { forwardRef, type InputHTMLAttributes, type ReactNode } from "react";
import { cx } from "./cx.js";

export type ChoiceProps = Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "children"> & {
  /** The label text. */
  children?: ReactNode;
};

/** `.check`: a checkbox with its label after it. `className` goes on the label, the rest on the input. */
export const Checkbox = forwardRef<HTMLInputElement, ChoiceProps>(function Checkbox({ children, className, ...rest }, ref) {
  return (
    <label className={cx("check", className)}>
      <input ref={ref} type="checkbox" {...rest} />
      {children}
    </label>
  );
});

/** `.switch`: a squared on/off track with its label before it. `className` goes on the label. */
export const Switch = forwardRef<HTMLInputElement, ChoiceProps>(function Switch({ children, className, ...rest }, ref) {
  return (
    <label className={cx("switch", className)}>
      {children}
      <input ref={ref} type="checkbox" role="switch" {...rest} />
    </label>
  );
});
