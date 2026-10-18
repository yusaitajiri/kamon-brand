import { type SVGAttributes } from "react";
import type { AppName } from "../tokens.js";
export type LogoProps = Omit<SVGAttributes<SVGSVGElement>, "children"> & {
    app: AppName;
    /** Size in px. Below 32 it draws the -small logo, made for small sizes. Defaults to 32. */
    size?: number;
    /** A name for screen readers. Leave it out when the app's name is written next to the logo. */
    title?: string;
};
/**
 * The app's logo from logo/, drawn inline in its own color, which turns to its -on-dark color in dark
 * mode, data-theme included. Never recolor it: show each app's logo in that app's color.
 */
export declare const Logo: import("react").ForwardRefExoticComponent<Omit<SVGAttributes<SVGSVGElement>, "children"> & {
    app: AppName;
    /** Size in px. Below 32 it draws the -small logo, made for small sizes. Defaults to 32. */
    size?: number;
    /** A name for screen readers. Leave it out when the app's name is written next to the logo. */
    title?: string;
} & import("react").RefAttributes<SVGSVGElement>>;
