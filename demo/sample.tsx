import { Button, Card, Checkbox, EmptyState, Field, Input, List, ListRow, Logo, Rule, Select, Switch, Tag } from "@yusai/kamon-react";
import { createRoot } from "react-dom/client";
import "../tokens/tokens.css";
import "../ui/ui.css";
import "./sample.css";

function Sample() {
  return (
    <main>
      <div className="bar">
        <span className="brand">
          <Logo app="kikitori" />
          Kikitori
        </span>
        <Button variant="quiet">設定</Button>
      </div>
      <Rule />
      <h1>記録</h1>
      <Input placeholder="記録を検索" aria-label="記録を検索" />
      <div className="tags">
        <Tag pressed>すべて</Tag>
        <Tag>仕事</Tag>
        <Tag>メモ</Tag>
      </div>

      <h2>最近の記録</h2>
      <Card>
        <List>
          <ListRow selected meta="10:42">週次ミーティング</ListRow>
          <ListRow meta="09:15">インタビュー 後半</ListRow>
          <ListRow meta="昨日">読書メモ</ListRow>
        </List>
      </Card>

      <h2>新しい記録</h2>
      <Card frame className="form">
        <Field label="タイトル">
          <Input defaultValue="週次ミーティング" />
        </Field>
        <Field label="種類">
          <Select>
            <option>メモ</option>
            <option>タスク</option>
          </Select>
        </Field>
        <Switch defaultChecked>リマインダー</Switch>
        <Checkbox>下書きとして保存</Checkbox>
        <div className="actions">
          <Button variant="primary">保存</Button>
          <Button>キャンセル</Button>
        </div>
      </Card>

      <h2>アーカイブ</h2>
      <Card>
        <EmptyState app="kikitori">まだ記録がありません。最初の一行を書いてみましょう。</EmptyState>
      </Card>
    </main>
  );
}

createRoot(document.getElementById("root")!).render(<Sample />);
