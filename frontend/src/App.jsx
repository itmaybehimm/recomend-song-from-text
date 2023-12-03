import { useState } from "react";
import "./App.css";
import Background from "./components/Background";
import axios from "axios";
// import Form from "./components/Form";
// import Form1 from "./components/Form1";

// import Background from "./components/Background";

const backendUrl = "http://127.0.0.1:8000/";

function App() {
  const [feel, setFeel] = useState("");
  const [username, setUsername] = useState("");

  const [formState, setFormState] = useState(0);

  function handleSubmit1(e) {
    e.preventDefault();
  }
  function handleSubmit(e) {
    e.preventDefault();
    setFormState(2);
    const data = {
      feel: feel,
      username: username,
    };
    console.log(data);
    axios
      .post(backendUrl + "mood/", data)
      .then((res) => {
        console.log(res);
        setFormState(3);
      })
      .catch((e) => {
        console.log(e);
      });
  }

  return (
    <>
      <div
        id="home-page"
        className="h-[100vh] w-[100vw] flex justify-center items-center"
      >
        <Background />
        {formState == 0 && (
          <form
            className="flex flex-col items-center justify-center gap-10"
            onSubmit={handleSubmit1}
          >
            <p className="text-[#eb5967] text-6xl ">Enter spotify username</p>
            <input
              className="h-[40px] w-[500px] bg-[#0e202f] text-center text-[#FA7268] placeholder:text-[#eb5967]"
              name="string"
              placeholder="..."
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            ></input>
            <button
              className="border-[1px] border-[#eb5967] rounded-full text-[#eb5967] px-4 py-2 hover:text-white hover:bg-[#eb5967] transition-all"
              onClick={() => setFormState(1)}
            >
              Continue
            </button>
          </form>
        )}
        {formState == 1 && (
          <form
            className="flex flex-col items-center justify-center gap-10"
            onSubmit={handleSubmit}
          >
            <p className="text-[#eb5967] text-6xl ">
              Tell us how you are feeling
            </p>
            <input
              className="h-[40px] w-[500px] bg-[#0e202f] text-center text-[#FA7268] placeholder:text-[#eb5967]"
              name="string"
              placeholder="..."
              value={feel}
              onChange={(e) => setFeel(e.target.value)}
            ></input>
            <button
              className="border-[1px] border-[#eb5967] rounded-full text-[#eb5967] px-4 py-2 hover:text-white hover:bg-[#eb5967] transition-all"
              type="submit"
            >
              Continue
            </button>
          </form>
        )}
        {formState == 2 && (
          <p className="text-[#eb5967] text-4xl ">
            Please wait we are creating your playlist....
          </p>
        )}
        {formState == 3 && (
          <p className="text-[#eb5967] text-4xl ">
            Your spotify playlist is ready
          </p>
        )}
      </div>
    </>
  );
}

export default App;
