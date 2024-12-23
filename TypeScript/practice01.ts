
let userName: string = 'Alice'; // 型指定
const age: number = 25; // 定数
let isStudent = true; // 型推論

let message: string = 'Hello, TypeScript!'; // 文字列
let count: number = 42; // 数値
let isDone: boolean = true; // 真偽値
let something = "TypeScript"; // 型推論：文字列

// 配列
let numbers: number[] = [1, 2, 3];
let strings: string[] = ["apple", "banana", "cherry"];

// タプル
let tuple: [string, number] = ["Alice", 25];

// 関数
function greet(name: string): string {
  return `Hello, ${name}!`;
}

function logMessage(message: string): void {
  console.log(message);
}

logMessage(greet(userName));

// オブジェクト
let person: { name: string, age: number } = {
    name: 'Alice',
    age: 25
};

console.log(person);

// クラス
class Animal {
    name: string;

    constructor(name: string) {
        this.name = name;
    }

    speak(): void {
        console.log(`${this.name} makes a sound.`);
    }
}

let dog = new Animal('Dog');
dog.speak();

// 型のユニオン
let value: string | number;
value = "Hello";
value = 42;

// 型エイリアス
type ID = string | number;
let userID: ID = 123;
userID = "ABC";

// 型アサーション
let someValue: any = "Hello, TypeScript!";
let stringLength: number = (someValue as string).length;

function add(a: number, b: number): number {
    return a + b;
}
console.log(add(1, 2)); // 3

function toString(value: number | string): string {
    return value.toString();
}
console.log(toString(42)); // "42"

type member = { name: string, age: number };
let mem: member = { name: 'Bob', age: 30 };
console.log(mem);