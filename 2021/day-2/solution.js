const { testInput, realInput } = require("./input");

// split by new line

const stringToArray = (inputStr) => {
  return inputStr.split("\n");
};

const challenge1 = (commands) => {
  // create a horizonal and vertical variable
  let horizonal = 0;
  let vertical = 0;

  // loop round the commands array
  commands.forEach((command) => {
    // split by space to get command & number
    // conditionaly increase or decrease the correct variable
    const splitCommand = command.split(" ");
    const cmd = splitCommand[0];
    const num = Number(splitCommand[1]);
    switch (cmd) {
      case "forward":
        horizonal += num;
        break;
      case "down":
        vertical += num;
        break;
      case "up":
        vertical -= num;
        break;
    }
  });
  return horizonal * vertical;
};

const challenge2 = (commands) => {
  // create a horizonal and vertical variable
  let horizonal = 0;
  let aim = 0;
  let depth = 0;

  // loop round the commands array
  commands.forEach((command) => {
    // split by space to get command & number
    // conditionaly increase or decrease the correct variable
    const splitCommand = command.split(" ");
    const cmd = splitCommand[0];
    const num = Number(splitCommand[1]);
    switch (cmd) {
      case "forward":
        horizonal += num;
        depth += num * aim;
        break;
      case "down":
        aim += num;
        break;
      case "up":
        aim -= num;
        break;
    }
  });
  return horizonal * depth;
};

const inputArray = stringToArray(realInput);
const task1 = challenge1(inputArray);
const task2 = challenge2(inputArray);

console.log("Task 1:", task1);
console.log("Task 2:", task2);
