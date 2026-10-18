import {
  createContext,
  forwardRef,
  useContext,
  useId,
  type InputHTMLAttributes,
  type LabelHTMLAttributes,
  type ReactNode,
  type SelectHTMLAttributes,
} from "react";
import { cx } from "./cx.js";

const FieldContext = createContext<{ describedBy?: string; invalid: boolean } | null>(null);

export type FieldProps = Omit<LabelHTMLAttributes<HTMLLabelElement>, "children"> & {
  label: ReactNode;
  /** A line of help under the control. */
  help?: ReactNode;
  /** What went wrong, in words. It marks the control invalid; never show an error by color alone. */
  error?: ReactNode;
  /** One Input or Select. */
  children: ReactNode;
};

/** `.field`: a label above one control, with help or an error under it, wired up for screen readers. */
export const Field = forwardRef<HTMLLabelElement, FieldProps>(function Field(
  { label, help, error, children, className, ...rest },
  ref,
) {
  const id = useId();
  const helpId = help ? `${id}-help` : undefined;
  const errorId = error ? `${id}-error` : undefined;
  const describedBy = [helpId, errorId].filter(Boolean).join(" ") || undefined;
  return (
    <label ref={ref} className={cx("field", className)} {...rest}>
      <span className="field-label">{label}</span>
      <FieldContext.Provider value={{ describedBy, invalid: Boolean(error) }}>{children}</FieldContext.Provider>
      {help && (
        <span id={helpId} className="field-help">
          {help}
        </span>
      )}
      {error && (
        <span id={errorId} className="field-error">
          {error}
        </span>
      )}
    </label>
  );
});

function useFieldProps(invalid: boolean | undefined, describedBy: string | undefined) {
  const field = useContext(FieldContext);
  return {
    "aria-invalid": (invalid ?? field?.invalid) ? true : undefined,
    "aria-describedby": describedBy ?? field?.describedBy,
  };
}

export type InputProps = InputHTMLAttributes<HTMLInputElement> & {
  /** Marks the input invalid. Inside a Field with an `error` this is set for you. */
  invalid?: boolean;
};

/** `.input`, the text box. */
export const Input = forwardRef<HTMLInputElement, InputProps>(function Input({ invalid, className, ...rest }, ref) {
  const aria = useFieldProps(invalid, rest["aria-describedby"]);
  return <input ref={ref} className={cx("input", className)} {...rest} {...aria} />;
});

export type SelectProps = SelectHTMLAttributes<HTMLSelectElement> & {
  invalid?: boolean;
};

/** `.select` in its `.select-wrap`, which draws the arrow. `className` goes on the select. */
export const Select = forwardRef<HTMLSelectElement, SelectProps>(function Select({ invalid, className, ...rest }, ref) {
  const aria = useFieldProps(invalid, rest["aria-describedby"]);
  return (
    <span className="select-wrap">
      <select ref={ref} className={cx("select", className)} {...rest} {...aria} />
    </span>
  );
});
