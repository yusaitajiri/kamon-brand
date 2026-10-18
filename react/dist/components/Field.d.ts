import { type InputHTMLAttributes, type LabelHTMLAttributes, type ReactNode, type SelectHTMLAttributes } from "react";
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
export declare const Field: import("react").ForwardRefExoticComponent<Omit<LabelHTMLAttributes<HTMLLabelElement>, "children"> & {
    label: ReactNode;
    /** A line of help under the control. */
    help?: ReactNode;
    /** What went wrong, in words. It marks the control invalid; never show an error by color alone. */
    error?: ReactNode;
    /** One Input or Select. */
    children: ReactNode;
} & import("react").RefAttributes<HTMLLabelElement>>;
export type InputProps = InputHTMLAttributes<HTMLInputElement> & {
    /** Marks the input invalid. Inside a Field with an `error` this is set for you. */
    invalid?: boolean;
};
/** `.input`, the text box. */
export declare const Input: import("react").ForwardRefExoticComponent<InputHTMLAttributes<HTMLInputElement> & {
    /** Marks the input invalid. Inside a Field with an `error` this is set for you. */
    invalid?: boolean;
} & import("react").RefAttributes<HTMLInputElement>>;
export type SelectProps = SelectHTMLAttributes<HTMLSelectElement> & {
    invalid?: boolean;
};
/** `.select` in its `.select-wrap`, which draws the arrow. `className` goes on the select. */
export declare const Select: import("react").ForwardRefExoticComponent<SelectHTMLAttributes<HTMLSelectElement> & {
    invalid?: boolean;
} & import("react").RefAttributes<HTMLSelectElement>>;
