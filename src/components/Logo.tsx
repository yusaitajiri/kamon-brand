import { forwardRef, type SVGAttributes } from "react";
import { logos } from "../logos.js";
import type { AppName } from "../tokens.js";
import { cx } from "./cx.js";

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
export const Logo = forwardRef<SVGSVGElement, LogoProps>(function Logo({ app, size = 32, title, className, ...rest }, ref) {
  const logo = logos[app];
  return (
    <svg
      ref={ref}
      viewBox="0 0 140 140"
      width={size}
      height={size}
      role={title ? "img" : undefined}
      aria-hidden={title ? undefined : true}
      className={cx("logo", className)}
      {...rest}
    >
      {title && <title>{title}</title>}
      <path fill={`var(--${logo.color})`} d={size < 32 ? logo.small : logo.full} />
    </svg>
  );
});
