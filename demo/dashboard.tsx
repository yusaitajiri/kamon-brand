import { Button, Card, EmptyState, Input, Logo, Rule, Tag } from "@yusai/kamon-react";
import { useState, type KeyboardEvent } from "react";
import { createRoot } from "react-dom/client";
import "../tokens/tokens.css";
import "../ui/ui.css";
import "./dashboard.css";

// Mock data and behavior only: a project board like GitHub Projects, on the brand's own page.

type Item = { ref: string; title: string; labels: { text: string; warning?: boolean }[]; who?: "YT" | "MO" };

const people = { YT: "Yusai Tajiri", MO: "Mika Ono" };

const columns: { name: string; items: Item[] }[] = [
  {
    name: "Todo",
    items: [
      { ref: "kamon-brand #14", title: "Pick a motif for the next app", labels: [{ text: "logo" }], who: "YT" },
      { ref: "kamon-brand #15", title: "Add tetsu and budo to the sample screens", labels: [{ text: "ui" }, { text: "color" }] },
      { ref: "kikitori #8", title: "Bundle the fonts in the iOS build", labels: [{ text: "ios" }], who: "YT" },
    ],
  },
  {
    name: "In progress",
    items: [
      { ref: "kamon-brand #12", title: "Project board sample page", labels: [{ text: "ui" }], who: "YT" },
      { ref: "explorer #21", title: "Tray icon on light Windows taskbars", labels: [{ text: "windows" }], who: "MO" },
      { ref: "kikitori #9", title: "Offline message for sync", labels: [{ text: "Blocked: waiting on copy", warning: true }] },
    ],
  },
  { name: "In review", items: [] },
  {
    name: "Done",
    items: [
      { ref: "kamon-brand #6", title: "Double line on the primary button", labels: [{ text: "ui" }], who: "YT" },
      { ref: "kamon-brand #5", title: "Migrate every logo to the 木瓜 frame", labels: [{ text: "logo" }], who: "YT" },
      { ref: "kamon-brand #4", title: "Dark-mode values for every app color", labels: [{ text: "color" }] },
      { ref: "kamon-brand #2", title: "Type tokens for web and React Native", labels: [{ text: "type" }], who: "MO" },
    ],
  },
];

const rows: [string, string, string, Item["who"], string][] = [
  ["kamon-brand #12", "Project board sample page", "In progress", "YT", "10:42"],
  ["explorer #21", "Tray icon on light Windows taskbars", "In progress", "MO", "09:15"],
  ["kikitori #9", "Offline message for sync", "Blocked", undefined, "Oct 15"],
  ["kamon-brand #14", "Pick a motif for the next app", "Todo", "YT", "Oct 14"],
  ["kamon-brand #15", "Add tetsu and budo to the sample screens", "Todo", undefined, "Oct 14"],
  ["kikitori #8", "Bundle the fonts in the iOS build", "Todo", "YT", "Oct 12"],
  ["kamon-brand #6", "Double line on the primary button", "Done", "YT", "Oct 17"],
  ["kamon-brand #5", "Migrate every logo to the 木瓜 frame", "Done", "YT", "Oct 16"],
  ["kamon-brand #4", "Dark-mode values for every app color", "Done", undefined, "Oct 10"],
  ["kamon-brand #2", "Type tokens for web and React Native", "Done", "MO", "Oct 3"],
];

function Avatar({ who, titled }: { who: keyof typeof people; titled?: boolean }) {
  return (
    <span className="avatar" title={titled ? people[who] : undefined}>
      {who}
    </span>
  );
}

function Dashboard() {
  const [view, setView] = useState<"board" | "table">("board");
  const [selected, setSelected] = useState("kamon-brand #12");
  const tab = (name: typeof view, label: string) => (
    <li
      className="view"
      role="tab"
      tabIndex={0}
      aria-selected={view === name}
      onClick={() => setView(name)}
      onKeyDown={(e: KeyboardEvent) => {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          setView(name);
        }
      }}
    >
      {label}
    </li>
  );

  return (
    <main>
      <div className="bar">
        <span className="brand">
          <Logo app="brand" />
          kamon-brand
        </span>
        <Button variant="quiet">Settings</Button>
      </div>
      <Rule />

      <div className="head">
        <div>
          <h1>Brand kit</h1>
          <p className="summary">
            <span className="num">4</span> of <span className="num">10</span> items done, last updated today.
          </p>
        </div>
        <Button variant="primary">New item</Button>
      </div>

      <ul className="views" role="tablist">
        {tab("board", "Board")}
        {tab("table", "Table")}
      </ul>

      <div className="tools">
        <Input placeholder="Filter by title, label or assignee" aria-label="Filter items" />
        <div className="tags">
          <Tag pressed>All</Tag>
          <Tag>Mine</Tag>
          <Tag>Blocked</Tag>
        </div>
      </div>

      {view === "board" ? (
        <section className="board">
          {columns.map((column) => (
            <div className="column" key={column.name}>
              <div className="column-head">
                <h2>{column.name}</h2>
                <span className="count">{column.items.length}</span>
              </div>
              {column.items.length === 0 ? (
                <EmptyState app="brand" className="card">
                  Nothing waiting for review.
                </EmptyState>
              ) : (
                <ul className="items">
                  {column.items.map((item) => (
                    <li
                      key={item.ref}
                      className="card item"
                      tabIndex={0}
                      aria-selected={selected === item.ref || undefined}
                      onClick={() => setSelected(item.ref)}
                    >
                      <span className="item-ref">{item.ref}</span>
                      <span>{item.title}</span>
                      <span className="item-foot">
                        <span className="labels">
                          {item.labels.map((label) => (
                            <Tag key={label.text} className={label.warning ? "tag-warning" : undefined}>
                              {label.text}
                            </Tag>
                          ))}
                        </span>
                        {item.who && <Avatar who={item.who} titled />}
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          ))}
        </section>
      ) : (
        <Card className="table-wrap">
          <table>
            <thead>
              <tr>
                <th>Item</th>
                <th>Title</th>
                <th>Status</th>
                <th>Assignee</th>
                <th>Updated</th>
              </tr>
            </thead>
            <tbody>
              {rows.map(([ref, title, status, who, updated]) => (
                <tr key={ref}>
                  <td className="mono">{ref}</td>
                  <td>{title}</td>
                  <td>{status === "Blocked" ? <Tag className="tag-warning">Blocked</Tag> : status}</td>
                  <td>
                    {who && (
                      <span className="who">
                        <Avatar who={who} />
                        {people[who]}
                      </span>
                    )}
                  </td>
                  <td className="mono">{updated}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>
      )}
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<Dashboard />);
