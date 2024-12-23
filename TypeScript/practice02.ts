let score: number = 50;

if (score >= 90) {
    console.log('Excellent');
} else if (score >= 70) {
    console.log('Good');
} else {
    console.log('Keep trying');
}

let day: string = "Sunday";

switch (day) {
    case "Monday":
        console.log("Start of the week!");
        break;
    case "Friday":
        console.log("Almost weekend!");
        break;
    default:
        console.log("Another day");
}

for (let i = 0; i < 5; i++) {
    console.log(`Count: ${i}`);
}

let colors: string[] = ['red', 'green', 'blue'];

for (let color of colors) {
    console.log(color);
}

//let psn = { name: "Alice", age: 25 };

// for (let key in psn) {
//     console.log(`${key}: ${psn[key]}`);
// }

let sum: number = 0;
for (let i = 1; i < 11; i++){
    sum += i;
}
console.log(sum)

let today: string = "Saturday";
switch (today) {
    case "Saturday":
        console.log("Weekend");
        break;
    case "Sunday":
        console.log("Weekend");
        break;
    default:
        console.log("Weekday");
}

function parseJson(jsonString: string): void {
    try {
        let result = JSON.parse(jsonString);
        console.log("Parsed JSON:", result);
    } catch(error) {
        if (error instanceof Error) {
            console.error("Failed to parse JSON:", error.message);
        } else {
            console.error("An unknown error occurred");
        }
    }
}
parseJson('{"name": "Alice", "age": }');