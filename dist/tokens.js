// Kamon brand tokens as plain values, generated from tokens.json (kamon-brand v2.0.0) by
// scripts/generate.mjs. Don't edit. Numbers are px. On the web prefer the CSS custom properties in
// tokens/tokens.css; use these where a value is needed in code, such as a canvas or a chart.
export const brand = {
    "color": {
        "light": {
            "surface": "#F3F1EC",
            "surface-raised": "#FBFAF7",
            "surface-sunken": "#E9E6DF",
            "border": "#DCD8CF",
            "border-strong": "#C2BDB2",
            "ink": "#2A2826",
            "ink-muted": "#5E5A53",
            "ink-subtle": "#6B665E",
            "moss": "#4E6B4F",
            "moss-hover": "#435E44",
            "moss-deep": "#3A523C",
            "moss-tint": "#DDE5D9",
            "on-moss": "#F7F6F1",
            "accent": "#4E6B4F",
            "accent-hover": "#435E44",
            "accent-deep": "#3A523C",
            "accent-tint": "#DDE5D9",
            "on-accent": "#F7F6F1",
            "shu": "#B0501F",
            "shu-hover": "#9A451A",
            "shu-deep": "#7F3A16",
            "shu-tint": "#F5E0D3",
            "on-shu": "#F7F6F1",
            "ai": "#3B5878",
            "ai-hover": "#324B66",
            "ai-deep": "#2C4460",
            "ai-tint": "#DCE3EC",
            "on-ai": "#F7F6F1",
            "budo": "#6E4C6E",
            "budo-hover": "#5F415F",
            "budo-deep": "#553A55",
            "budo-tint": "#E8DEE7",
            "on-budo": "#F7F6F1",
            "tetsu": "#2F6265",
            "tetsu-hover": "#285457",
            "tetsu-deep": "#224A4C",
            "tetsu-tint": "#D7E6E5",
            "on-tetsu": "#F7F6F1",
            "sage": "#C3CFBF",
            "blush": "#E3B7A6",
            "danger": "#A3473A",
            "danger-tint": "#F3E1DC",
            "success": "#4E6B4F",
            "warning": "#80591A",
            "warning-tint": "#F4EAD6"
        },
        "dark": {
            "surface": "#1C1E1B",
            "surface-raised": "#252824",
            "surface-sunken": "#151714",
            "border": "#363A34",
            "border-strong": "#4A4F47",
            "ink": "#ECE9E2",
            "ink-muted": "#B0ABA1",
            "ink-subtle": "#99948A",
            "moss": "#8FB08F",
            "moss-hover": "#A2BFA1",
            "moss-deep": "#B5CDB3",
            "moss-tint": "#2C382C",
            "on-moss": "#172016",
            "accent": "#8FB08F",
            "accent-hover": "#A2BFA1",
            "accent-deep": "#B5CDB3",
            "accent-tint": "#2C382C",
            "on-accent": "#172016",
            "shu": "#EBA57E",
            "shu-hover": "#F0B796",
            "shu-deep": "#F4C9AF",
            "shu-tint": "#3B2A20",
            "on-shu": "#1F140D",
            "ai": "#93AACB",
            "ai-hover": "#A6BAD6",
            "ai-deep": "#BACAE0",
            "ai-tint": "#26303B",
            "on-ai": "#141A22",
            "budo": "#C29FC2",
            "budo-hover": "#CDB0CD",
            "budo-deep": "#D8C1D8",
            "budo-tint": "#33293A",
            "on-budo": "#1E161E",
            "tetsu": "#86B7B5",
            "tetsu-hover": "#9AC4C2",
            "tetsu-deep": "#AED1CF",
            "tetsu-tint": "#223434",
            "on-tetsu": "#122020",
            "sage": "#4C5C4A",
            "blush": "#C99A8A",
            "danger": "#E39A8C",
            "danger-tint": "#3A2622",
            "success": "#8FB08F",
            "warning": "#D9B46A",
            "warning-tint": "#3A311F"
        }
    },
    "space": {
        "1": 4,
        "2": 8,
        "3": 12,
        "4": 16,
        "6": 24,
        "8": 32,
        "12": 48,
        "16": 64
    },
    "radius": {
        "sm": 6,
        "md": 8,
        "lg": 12,
        "full": 9999
    },
    "apps": {
        "brand": {
            "color": "moss",
            "logo": "logo/brand.svg"
        },
        "kikitori": {
            "color": "shu",
            "logo": "logo/kikitori.svg"
        },
        "explorer": {
            "color": "ai",
            "logo": "logo/explorer.svg"
        }
    },
    "type": {
        "display": {
            "size": 40,
            "lineHeight": 48,
            "weight": 500
        },
        "title": {
            "size": 28,
            "lineHeight": 36,
            "weight": 500
        },
        "heading": {
            "size": 20,
            "lineHeight": 28,
            "weight": 500
        },
        "body": {
            "size": 16,
            "lineHeight": 27,
            "weight": 400
        },
        "body-small": {
            "size": 14,
            "lineHeight": 22,
            "weight": 400
        },
        "label": {
            "size": 14,
            "lineHeight": 20,
            "weight": 500
        },
        "caption": {
            "size": 12,
            "lineHeight": 18,
            "weight": 400
        },
        "mono": {
            "size": 13,
            "lineHeight": 20,
            "weight": 400
        }
    },
    "font": {
        "sans": "Zen Kaku Gothic New",
        "mono": "IBM Plex Mono"
    }
};
/** The theme's colors with accent set to the app's own color. */
export function appColors(app, theme) {
    const c = brand.color[theme];
    const k = brand.apps[app].color;
    return {
        ...c,
        accent: c[k],
        "accent-hover": c[`${k}-hover`],
        "accent-deep": c[`${k}-deep`],
        "accent-tint": c[`${k}-tint`],
        "on-accent": c[`on-${k}`],
    };
}
