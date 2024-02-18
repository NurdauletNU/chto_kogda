import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import axios from "axios";

function CounterOnConsole() {
  let num = 6;

  function multiply() {
    num = num * 2;
    console.log(num);
  }

  function divide() {
    num = num / 2;
    console.log(num);
  }

  return (
    <div>
      <div className={"header"}>{num}</div>
      <div className={"body"}>
        <button onClick={multiply}>*</button>
      </div>
      <div className={"footer"}>
        <button onClick={divide}>-</button>
      </div>
    </div>
  );
}

//   return (
//     <div>
//       <div className={"header"}>{num}</div>
//       <div className={"body"}>
//         <button onClick={multiply}>*</button>
//       </div>
//       <div className={"footer"}>
//         <button onClick={divide}>-</button>
//       </div>
//     </div>
//   );
// }

function Calculator() {
  const [display, setDisplay] = useState<string>("");

  function handleClick(value: string | number) {
    if (typeof value === "number" || value === ".") {
      setDisplay(display + value);
    } else if (value === "=") {
      try {
        setDisplay(eval(display).toString());
      } catch {
        setDisplay("Ошибка");
      }
    } else if (value === "C") {
      setDisplay("");
    } else {
      setDisplay(display + " " + value + " ");
    }
  }

  return (
    <div className="calculator">
      <input type="text" value={display} readOnly />
      <div className="buttons">
        {[7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, ".", "=", "C"].map(
          function (value) {
            return (
              <button
                key={value}
                onClick={function () {
                  handleClick(value);
                }}
              >
                {value}
              </button>
            );
          },
        )}
      </div>
    </div>
  );
}

function App() {
  async function getData() {
    try {
      const response = await axios.get("http://127.0.0.1:8000/api_data");
      console.log("data: ", response.data, new Date());
    } catch (error) {
      console.error("ошибка: ", error, new Date());
    }
  }
  return (
    // - design
    <div style={{ marginLeft: "20px" }}>
      <button onClick={getData}>Click me!</button>
      <hr />
      <Calculator />
    </div>
  );
}

createRoot(document.getElementById("root")!).render(
  //<React.StrictMode>
  <App />,
  //</React.StrictMode>
);

function Adm() {
  // - logic
  // ...
  // ...
  return <div>101</div>; // -дизайн
}

createRoot(document.getElementById("adm")!).render(<Adm />);
