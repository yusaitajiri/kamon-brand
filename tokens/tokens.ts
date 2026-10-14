// Kudagitsune brand tokens — plain values for React / React Native / Expo.
// Numbers are px. See ../README.md for when to use each token.
export const kudagitsune = {
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
    "seal": 14,
    "full": 9999
  },
  "font": {
    "sans": "Zen Kaku Gothic New",
    "mono": "IBM Plex Mono",
    "seal": "Zen Old Mincho"
  }
} as const;

export type ThemeName = keyof typeof kudagitsune.color;
