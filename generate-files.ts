import fs from "fs";

// const start_data = `import fs from "fs";

// const data = fs.readFileSync("./input.txt", "utf-8").split("\\n");

// `;

const py_start_data = `import sys
sys.path.append("..")
from helpers import *  # noqa

# Parse input
data = parse_input("./input.txt", Parse.lines)
ans1 = 0
ans2 = 0


`;

for (let i = 1; i <= 12; i++) {
  const folder = `day${String(i).padStart(2, "0")}`;
  fs.mkdir(folder, () => {
    fs.writeFileSync(`${folder}/input.txt`, "");
    // fs.writeFileSync(`${folder}/index.ts`, start_data);
    fs.writeFileSync(`${folder}/main.py`, py_start_data);
  });
}
