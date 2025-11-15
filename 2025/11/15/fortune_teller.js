// fortune_teller.js
// 2025-11-15 - おみくじ付き今日の運勢占い

const fortunes = [
  { level: "大吉", message: "最高の1日になるよ！", lucky: "青色" },
  { level: "中吉", message: "良いことありそう！", lucky: "緑色" },
  { level: "吉", message: "まあまあ良い日だね。", lucky: "黄色" },
  { level: "小吉", message: "ちょっとした幸運が転がってくるかも？", lucky: "オレンジ色" },
  { level: "末吉", message: "控えめにね。", lucky: "ピンク色" },
  { level: "凶", message: "今日は慎重に…", lucky: "白色" }
];

console.log("=== 今日の運勢占い ===\n");

const randomIndex = Math.floor(Math.random() * fortunes.length);
const todayFortune = fortunes[randomIndex];

console.log(`運勢: ${todayFortune.level}`);
console.log(`メッセージ: ${todayFortune.message}`);
console.log(`ラッキーカラー: ${todayFortune.lucky}`);

const luckyNumber = Math.floor(Math.random() * 100) + 1;
console.log(`ラッキーナンバー: ${luckyNumber}`);

console.log("\n今日も1日頑張ろうね！")
