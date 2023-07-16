const { testData, realData } = require("./input");

const stringToArray = (inputStr) => {
  const array = inputStr.split("\n");
  return array.map((item) => Number(item));
};

const challengeOne = (numArray) => {
  const checkIncrease = (num1, num2) => {
    return num1 > num2;
  };

  let increase = 0;
  for (let i = 0; i < numArray.length; i++) {
    if (i !== 0) {
      checkIncrease(numArray[i], numArray[i - 1]) ? increase++ : null;
    }
  }
  return increase;
};

const challengeTwo = (numArray) => {
  const checkIncrease = (num1, num2) => {
    return num1 < num2;
  };

  let increase = 0;
  for (let i = 0; i < numArray.length; i++) {
    if (i !== 0) {
      const sum1 = numArray[i] + numArray[i + 1] + numArray[i + 2];
      const sum2 = numArray[i + 1] + numArray[i + 2] + numArray[i + 3];

      checkIncrease(sum1, sum2) ? increase++ : null;
    }
  }
  return increase;
};

const input = stringToArray(realData);

const task1 = challengeOne(input);
const task2 = challengeTwo(input);

console.log("Task 1:", task1);
console.log("Task 2:", task2);
