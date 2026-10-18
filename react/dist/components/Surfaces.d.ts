import { type HTMLAttributes, type LiHTMLAttributes, type ReactNode } from "react";
import type { AppName } from "../tokens.js";
export type CardProps = HTMLAttributes<HTMLDivElement> & {
    /**
     * The kamon's frame: only on the one container being worked in (an editor, an edit panel, a dialog),
     * never on two in a view, on list rows or repeated items. When a dialog opens, its frame replaces this one.
     */
    frame?: boolean;
};
/** `.card` on `surface-raised` with a hairline border. */
export declare const Card: import("react").ForwardRefExoticComponent<HTMLAttributes<HTMLDivElement> & {
    /**
     * The kamon's frame: only on the one container being worked in (an editor, an edit panel, a dialog),
     * never on two in a view, on list rows or repeated items. When a dialog opens, its frame replaces this one.
     */
    frame?: boolean;
} & import("react").RefAttributes<HTMLDivElement>>;
/** `.list`, a plain list of rows. */
export declare const List: import("react").ForwardRefExoticComponent<HTMLAttributes<HTMLUListElement> & import("react").RefAttributes<HTMLUListElement>>;
export type ListRowProps = LiHTMLAttributes<HTMLLIElement> & {
    /** Selected rows take accent-tint with accent-deep text. */
    selected?: boolean;
    /** Mono text at the end of the row, such as a time. */
    meta?: ReactNode;
};
/** `.list-row`: its content on the left and `meta` on the right. */
export declare const ListRow: import("react").ForwardRefExoticComponent<LiHTMLAttributes<HTMLLIElement> & {
    /** Selected rows take accent-tint with accent-deep text. */
    selected?: boolean;
    /** Mono text at the end of the row, such as a time. */
    meta?: ReactNode;
} & import("react").RefAttributes<HTMLLIElement>>;
export type TagProps = HTMLAttributes<HTMLSpanElement> & {
    /** A selected filter takes accent-tint with accent-deep text. */
    pressed?: boolean;
};
/** `.tag`, with `radius-sm` corners: never a pill. */
export declare const Tag: import("react").ForwardRefExoticComponent<HTMLAttributes<HTMLSpanElement> & {
    /** A selected filter takes accent-tint with accent-deep text. */
    pressed?: boolean;
} & import("react").RefAttributes<HTMLSpanElement>>;
export type EmptyStateProps = HTMLAttributes<HTMLDivElement> & {
    /** Shows this app's logo at 48px above the sentence. */
    app?: AppName;
};
/** `.empty`: one sentence, a little warm, optionally under the app's logo. */
export declare const EmptyState: import("react").ForwardRefExoticComponent<HTMLAttributes<HTMLDivElement> & {
    /** Shows this app's logo at 48px above the sentence. */
    app?: AppName;
} & import("react").RefAttributes<HTMLDivElement>>;
/** `.rule`, 子持ち罫: only once per view, under the app bar. Never between sections. */
export declare const Rule: import("react").ForwardRefExoticComponent<HTMLAttributes<HTMLHRElement> & import("react").RefAttributes<HTMLHRElement>>;
