// 2025-11-22: - TypeScript greeting generator

type Greeting = {
  time: string;
  message: string;
};

const greetings: Greeting[] = [
  { time: "morning", message: "おはよう！今日も頑張ろうね☀️" },
  { time: "afternoon", message: "こんにちは！調子はどう？😊" },
  { time: "evening", message: "こんばんは！お疲れ様🌙" },
  { time: "night", message: "まだ起きてるの？早く寝なよ〜💤" }
];

function getRandomGreeting(): Greeting {
  const randomIndex = Math.floor(Math.random() * greetings.length);
  return greetings[randomIndex];
}

function greet(name: string): void {
  const greeting = getRandomGreeting();
  console.log(`[${greeting.time}] ${greeting.message}`);
  console.log(`${name}さん、また会おうね！👋`);
}

// 実行
greet("forsteri");