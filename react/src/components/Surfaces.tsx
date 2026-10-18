import { forwardRef, type HTMLAttributes, type LiHTMLAttributes, type ReactNode } from "react";
import type { AppName } from "../tokens.js";
import { Logo } from "./Logo.js";
import { cx } from "./cx.js";

export type CardProps = HTMLAttributes<HTMLDivElement> & {
  /**
   * The kamon's frame: only on the one container being worked in (an editor, an edit panel, a dialog),
   * never on two in a view, on list rows or repeated items. When a dialog opens, its frame replaces this one.
   */
  frame?: boolean;
};

/** `.card` on `surface-raised` with a hairline border. */
export const Card = forwardRef<HTMLDivElement, CardProps>(function Card({ frame, className, ...rest }, ref) {
  return <div ref={ref} className={cx("card", frame && "frame", className)} {...rest} />;
});

/** `.list`, a plain list of rows. */
export const List = forwardRef<HTMLUListElement, HTMLAttributes<HTMLUListElement>>(function List({ className, ...rest }, ref) {
  return <ul ref={ref} className={cx("list", className)} {...rest} />;
});

export type ListRowProps = LiHTMLAttributes<HTMLLIElement> & {
  /** Selected rows take accent-tint with accent-deep text. */
  selected?: boolean;
  /** Mono text at the end of the row, such as a time. */
  meta?: ReactNode;
};

/** `.list-row`: its content on the left and `meta` on the right. */
export const ListRow = forwardRef<HTMLLIElement, ListRowProps>(function ListRow(
  { selected, meta, children, className, ...rest },
  ref,
) {
  return (
    <li ref={ref} className={cx("list-row", className)} aria-selected={selected || undefined} {...rest}>
      <span>{children}</span>
      {meta != null && <span className="list-meta">{meta}</span>}
    </li>
  );
});

export type TagProps = HTMLAttributes<HTMLSpanElement> & {
  /** A selected filter takes accent-tint with accent-deep text. */
  pressed?: boolean;
};

/** `.tag`, with `radius-sm` corners: never a pill. */
export const Tag = forwardRef<HTMLSpanElement, TagProps>(function Tag({ pressed, className, ...rest }, ref) {
  return <span ref={ref} className={cx("tag", className)} aria-pressed={pressed ?? undefined} {...rest} />;
});

export type EmptyStateProps = HTMLAttributes<HTMLDivElement> & {
  /** Shows this app's logo at 48px above the sentence. */
  app?: AppName;
};

/** `.empty`: one sentence, a little warm, optionally under the app's logo. */
export const EmptyState = forwardRef<HTMLDivElement, EmptyStateProps>(function EmptyState(
  { app, children, className, ...rest },
  ref,
) {
  return (
    <div ref={ref} className={cx("empty", className)} {...rest}>
      {app && <Logo app={app} size={48} />}
      {children}
    </div>
  );
});

/** `.rule`, 子持ち罫: only once per view, under the app bar. Never between sections. */
export const Rule = forwardRef<HTMLHRElement, HTMLAttributes<HTMLHRElement>>(function Rule({ className, ...rest }, ref) {
  return <hr ref={ref} className={cx("rule", className)} {...rest} />;
});
