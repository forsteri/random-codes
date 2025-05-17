// JavaScriptの基本サンプル

// -----------------------------------------------------
// 基本的な変数宣言と演算
// -----------------------------------------------------

// 変数宣言（let, const）
let message = "こんにちは、JavaScript!";
const PI = 3.14159;

// コンソールに出力
console.log(message);
console.log("円周率の値は " + PI + " です。");

// 基本的な演算
let x = 10;
let y = 5;

console.log("x + y = " + (x + y));  // 加算
console.log("x - y = " + (x - y));  // 減算
console.log("x * y = " + (x * y));  // 乗算
console.log("x / y = " + (x / y));  // 除算
console.log("x % y = " + (x % y));  // 剰余

// 文字列操作
let firstName = "太郎";
let lastName = "山田";
let fullName = lastName + " " + firstName;
console.log("フルネーム: " + fullName);

// テンプレートリテラル（バッククォートを使用）
let greeting = `こんにちは、${fullName}さん！今日の気温は${20 + 5}度です。`;
console.log(greeting);

// -----------------------------------------------------
// データ型と配列、オブジェクト
// -----------------------------------------------------

// 配列
let fruits = ["りんご", "バナナ", "オレンジ", "ぶどう"];
console.log(fruits[0]);  // 最初の要素にアクセス
console.log(fruits.length);  // 配列の長さ

// 配列のループ処理
console.log("フルーツリスト:");
for (let i = 0; i < fruits.length; i++) {
    console.log(`${i + 1}. ${fruits[i]}`);
}

// forEachを使ったループ
console.log("forEach使用:");
fruits.forEach(function(fruit, index) {
    console.log(`${index + 1}. ${fruit}`);
});

// オブジェクト
let person = {
    firstName: "太郎",
    lastName: "山田",
    age: 30,
    hobbies: ["読書", "旅行", "プログラミング"],
    address: {
        city: "東京",
        postalCode: "123-4567"
    }
};

console.log(person.firstName);  // プロパティへのアクセス
console.log(person.hobbies[2]);  // ネストした配列へのアクセス
console.log(person.address.city);  // ネストしたオブジェクトへのアクセス

// -----------------------------------------------------
// 条件分岐
// -----------------------------------------------------

let hour = 14;

// if文
if (hour < 12) {
    console.log("おはようございます！");
} else if (hour < 18) {
    console.log("こんにちは！");
} else {
    console.log("こんばんは！");
}

// switch文
let day = "月曜日";
switch (day) {
    case "月曜日":
        console.log("週の始まりです");
        break;
    case "金曜日":
        console.log("週末が近いです");
        break;
    case "土曜日":
    case "日曜日":
        console.log("週末です");
        break;
    default:
        console.log("平日です");
}

// 三項演算子
let age = 20;
let status = age >= 18 ? "成人" : "未成年";
console.log(status);

// -----------------------------------------------------
// 関数
// -----------------------------------------------------

// 関数宣言
function greet(name) {
    return `こんにちは、${name}さん！`;
}

console.log(greet("花子"));

// デフォルトパラメータ
function greetWithTime(name, time = "昼") {
    if (time === "朝") {
        return `おはようございます、${name}さん！`;
    } else if (time === "昼") {
        return `こんにちは、${name}さん！`;
    } else {
        return `こんばんは、${name}さん！`;
    }
}

console.log(greetWithTime("一郎", "朝"));
console.log(greetWithTime("二郎"));  // デフォルトパラメータ使用

// アロー関数
const multiply = (a, b) => a * b;
console.log(`5 x 3 = ${multiply(5, 3)}`);

// 高階関数（関数を引数として受け取る関数）
function doOperation(x, y, operation) {
    return operation(x, y);
}

const add = (a, b) => a + b;
const subtract = (a, b) => a - b;

console.log(doOperation(10, 5, add));      // 15
console.log(doOperation(10, 5, subtract)); // 5

// -----------------------------------------------------
// DOM操作の基本（HTMLファイルと一緒に使うコード）
// -----------------------------------------------------

// ページ読み込み後に実行する関数
document.addEventListener('DOMContentLoaded', () => {
    // HTML要素の取得
    const title = document.getElementById('title');
    const button = document.querySelector('.btn');
    const items = document.querySelectorAll('.item');
    
    // コンテンツの変更
    if (title) {
        title.textContent = 'JavaScriptでタイトルを変更しました！';
    }
    
    // イベントリスナーの追加
    if (button) {
        button.addEventListener('click', () => {
            alert('ボタンがクリックされました！');
        });
    }
    
    // 複数の要素に対する処理
    if (items.length > 0) {
        items.forEach((item, index) => {
            item.style.color = index % 2 === 0 ? 'blue' : 'red';
        });
    }
    
    // 新しい要素の作成と追加
    const container = document.querySelector('.container');
    if (container) {
        const newParagraph = document.createElement('p');
        newParagraph.textContent = 'これはJavaScriptで動的に追加された段落です。';
        newParagraph.classList.add('dynamic-content');
        container.appendChild(newParagraph);
    }
});

// -----------------------------------------------------
// 非同期処理の基本
// -----------------------------------------------------

// setTimeout（一定時間後に実行）
console.log("処理を開始します");

setTimeout(() => {
    console.log("3秒後に実行される処理");
}, 3000);

console.log("他の処理を続行します");

// Promiseの基本
function fetchData() {
    return new Promise((resolve, reject) => {
        // 擬似的な非同期処理（実際のAPIリクエストなど）
        setTimeout(() => {
            const success = true;
            
            if (success) {
                resolve({ id: 1, name: "サンプルデータ" });
            } else {
                reject("エラーが発生しました");
            }
        }, 2000);
    });
}

// Promiseを使った処理
fetchData()
    .then(data => {
        console.log("データの取得に成功:", data);
    })
    .catch(error => {
        console.error("エラー:", error);
    })
    .finally(() => {
        console.log("処理が完了しました");
    });

// async/awaitを使った非同期処理
async function fetchDataAsync() {
    try {
        console.log("非同期データの取得を開始...");
        const data = await fetchData();
        console.log("async/awaitでデータ取得成功:", data);
    } catch (error) {
        console.error("async/awaitでエラー:", error);
    }
}

// 非同期関数の実行
fetchDataAsync();
