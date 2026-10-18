import { Button, Card, Checkbox, EmptyState, Field, Input, List, ListRow, Logo, Rule, Select, Switch, Tag } from "@yusai/kamon-react";
import { createRoot } from "react-dom/client";
import "../tokens/fonts.css";
import "../tokens/tokens.css";
import "../ui/ui.css";
import "./elements.css";

function Variant({ name, children }: { name: string; children: React.ReactNode }) {
  return (
    <div className="variant">
      <div className="variant-name">{name}</div>
      {children}
    </div>
  );
}

function Elements() {
  return (
    <main>
      <h1>UI elements</h1>
      <p>
        Every element is plain except where the kamon's double line comes in: the primary button, the one action per view, has
        a thin line inside its edge like the 木瓜 frame's own, and a view may have one framed container and one 子持ち罫 rule
        under its app bar.
      </p>

      <Card className="section">
        <h2>Button</h2>
        <Variant name="Primary, secondary, quiet, focused, disabled">
          <div className="row">
            <Button variant="primary">Save</Button>
            <Button>Cancel</Button>
            <Button variant="quiet">Edit</Button>
            <Button className="is-focus">Focused</Button>
            <Button variant="primary" disabled>
              Save
            </Button>
          </div>
        </Variant>
        <Variant name="The primary button enlarged four times, beside the logo its inner line comes from">
          <div className="row enlarged">
            <div className="zoom">
              <Button variant="primary">Save</Button>
            </div>
            <Logo app="brand" size={140} title="The brand logo" />
          </div>
        </Variant>
      </Card>

      <Card className="section">
        <h2>Text box</h2>
        <Variant name="Empty, filled, focused, error, disabled">
          <div className="row">
            <Field label="Title">
              <Input placeholder="Untitled" />
            </Field>
            <Field label="Title" help="Shown at the top of the entry.">
              <Input defaultValue="Weekly notes" />
            </Field>
            <Field label="Title">
              <Input className="is-focus" defaultValue="Weekly notes" />
            </Field>
            <Field label="Email" error="Enter a full email address.">
              <Input defaultValue="yusai@" />
            </Field>
            <Field label="Title">
              <Input defaultValue="Weekly notes" disabled />
            </Field>
          </div>
        </Variant>
      </Card>

      <Card className="section">
        <h2>Select</h2>
        <Variant name="Closed">
          <div className="row">
            <Field label="Kind">
              <Select>
                <option>Memo</option>
                <option>Task</option>
              </Select>
            </Field>
          </div>
        </Variant>
      </Card>

      <Card className="section">
        <h2>Checkbox and switch</h2>
        <Variant name="Off, on, focused, disabled">
          <div className="row">
            <Checkbox>Save as draft</Checkbox>
            <Checkbox defaultChecked>Save as draft</Checkbox>
            <Checkbox className="is-focus">Save as draft</Checkbox>
            <Checkbox disabled>Save as draft</Checkbox>
          </div>
          <div className="row">
            <Switch>Reminder</Switch>
            <Switch defaultChecked>Reminder</Switch>
          </div>
        </Variant>
      </Card>

      <Card className="section">
        <h2>Tag, list and empty state</h2>
        <Variant name="Tags, a list with one row selected, an empty state">
          <div className="row">
            <Tag pressed>All</Tag>
            <Tag>Work</Tag>
            <Tag>Memo</Tag>
          </div>
          <List style={{ marginTop: "var(--space-4)", maxWidth: 420 }}>
            <ListRow selected meta="10:42">
              Weekly notes
            </ListRow>
            <ListRow meta="09:15">Interview, part two</ListRow>
          </List>
          <EmptyState>No entries yet. Write your first line.</EmptyState>
        </Variant>
      </Card>

      <Card className="section">
        <h2>Frame and rule</h2>
        <Variant name="The rule under an app bar, once per view">
          <div className="appbar-demo">
            <div className="row bar-row">
              <span>App name</span>
              <span className="variant-name">Settings</span>
            </div>
            <Rule />
          </div>
        </Variant>
        <Variant name="The frame on the one container you are working in, beside a plain card">
          <div className="row frames">
            <Card frame>
              <Field label="Title">
                <Input defaultValue="Weekly notes" />
              </Field>
              <Button variant="primary">Save</Button>
            </Card>
            <Card>
              <Field label="Kind">
                <Select>
                  <option>Memo</option>
                </Select>
              </Field>
            </Card>
          </div>
        </Variant>
      </Card>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<Elements />);
