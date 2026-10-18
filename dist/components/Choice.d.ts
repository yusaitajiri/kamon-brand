import { type InputHTMLAttributes, type ReactNode } from "react";
export type ChoiceProps = Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "children"> & {
    /** The label text. */
    children?: ReactNode;
};
/** `.check`: a checkbox with its label after it. `className` goes on the label, the rest on the input. */
export declare const Checkbox: import("react").ForwardRefExoticComponent<Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "children"> & {
    /** The label text. */
    children?: ReactNode;
} & import("react").RefAttributes<HTMLInputElement>>;
/** `.switch`: a squared on/off track with its label before it. `className` goes on the label. */
export declare const Switch: import("react").ForwardRefExoticComponent<Omit<InputHTMLAttributes<HTMLInputElement>, "type" | "children"> & {
    /** The label text. */
    children?: ReactNode;
} & import("react").RefAttributes<HTMLInputElement>>;
