import { Card, List, Logo, Rule } from "@yusai/kamon-react";
import { createRoot } from "react-dom/client";
import "../tokens/tokens.css";
import "../ui/ui.css";
import "./index.css";

const pages = [
  ["elements.html", "UI elements", "Every component in each of its states."],
  ["sample.html", "Sample screen", "A phone-width screen in Kikitori's color."],
  ["dashboard.html", "Project board", "A board and a table view on the brand's own page."],
];

function Index() {
  return (
    <main>
      <div className="bar">
        <span className="brand">
          <Logo app="brand" />
          kamon-react
        </span>
      </div>
      <Rule />
      <h1>kamon-react</h1>
      <p>The demo pages for the React kit, built from its components.</p>
      <Card>
        <List>
          {pages.map(([href, name, about]) => (
            <li key={href} className="list-row">
              <a href={href}>{name}</a>
              <span className="about">{about}</span>
            </li>
          ))}
        </List>
      </Card>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<Index />);
